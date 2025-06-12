# Dockerfile for the 2.4 GA version of MariaDB MaxScale
FROM ubuntu:bionic

ARG VERSION
ARG GIT_COMMIT
ARG GIT_TREE_STATE
ARG BUILD_TIME

# Create a non-root user
RUN useradd -m -s /bin/bash maxuser

COPY maxscale.list /etc/apt/sources.list.d/maxscale.list.tmp
RUN apt-get -y update && \
    apt-get -y install gnupg2 ca-certificates curl && \
    curl -fsSL https://downloads.mariadb.com/MaxScale/maxscale-key.asc | apt-key add - && \
    mv /etc/apt/sources.list.d/maxscale.list.tmp /etc/apt/sources.list.d/maxscale.list && \
    apt-get -y update && \
    apt-get -y install maxscale && \
    rm -rf /var/lib/apt/lists/*

    if [ ! -z "$VERSION" ] && [ ! -z "$GIT_COMMIT" ] && [ ! -z "$BUILD_TIME" ]; then \
       printf "Version: %s\nGitCommit: %s\nGitTreeState: %s\nBuildTime: %s\n" "$VERSION" "$GIT_COMMIT" "$GIT_TREE_STATE" "$BUILD_TIME"; \
    fi

COPY maxscale.cnf /etc/
COPY docker-entrypoint.sh /usr/local/bin/

RUN chmod 755 /usr/local/bin/docker-entrypoint.sh && \
    ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh

# Change to non-root user
USER maxuser

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]

