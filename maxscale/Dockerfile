# Dockerfile for the 2.4 GA version of MariaDB MaxScale
FROM ubuntu:bionic

ARG VERSION
ARG GIT_COMMIT
ARG GIT_TREE_STATE
ARG BUILD_TIME

COPY maxscale.list /etc/apt/sources.list.d/maxscale.list.tmp
RUN apt-get -y update && \
    apt-get -y install gnupg2 ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "0x135659BA7B6A9F8D" && \
    mv /etc/apt/sources.list.d/maxscale.list.tmp /etc/apt/sources.list.d/maxscale.list && \
    apt-get -y update && \
    apt-get -y install maxscale procps && \
    rm -rf /var/lib/apt/lists/* && \
    if [ ! -z "$VERSION" ] && [ ! -z "$GIT_COMMIT" ] && [ ! -z "$BUILD_TIME" ]; then \
       printf "Version:    $VERSION\nGit commit: $GIT_COMMIT$GIT_TREE_STATE\nBuild time: $BUILD_TIME\n"; \
    fi

COPY maxscale.cnf /etc/

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh && \
    ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh # backwards compatibility

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]

