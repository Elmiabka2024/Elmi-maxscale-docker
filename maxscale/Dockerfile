# Dockerfile for the 2.4 GA version of MariaDB MaxScale
FROM ubuntu:bionic

ARG VERSION
ARG GIT_COMMIT
ARG GIT_TREE_STATE
ARG BUILD_TIME

COPY maxscale.list /etc/apt/sources.list.d/maxscale.list.tmp

RUN apt-get -y update && \
    apt-get -y install gnupg2 ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "0x135659e928c12247" && \
    mv /etc/apt/sources.list.d/maxscale.list.tmp /etc/apt/sources.list.d/maxscale.list && \
    apt-get -y update && \
    apt-get -y install maxscale && \
    rm -rf /var/lib/apt/lists/* && \
    if [ -n "$VERSION" ] && [ -n "$GIT_COMMIT" ] && [ -n "$BUILD_TIME" ]; then \
      printf "Version:    %s\nGit commit: %s%s\nBuilt:      %s\n" "$VERSION" "$GIT_COMMIT" "$GIT_TREE_STATE" "$BUILD_TIME" > /opt/image_details; \
    fi

# Create non-root user and fix permissions
RUN useradd -ms /bin/bash maxscaleuser && \
    mkdir -p /var/run/maxscale && \
    chown -R maxscaleuser:maxscaleuser /etc/maxscale.cnf /var/lib/maxscale /var/log/maxscale /var/run/maxscale || true

USER maxscaleuser

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]

