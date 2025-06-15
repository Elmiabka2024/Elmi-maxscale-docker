# File: Dockerfile
FROM ubuntu:bionic

# Optional metadata for debugging
ARG VERSION
ARG GIT_COMMIT
ARG GIT_TREE_STATE
ARG BUILD_TIME

# Add MariaDB MaxScale repository
COPY maxscale.list /etc/apt/sources.list.d/maxscale.list.tmp

# Install MaxScale and required tools
RUN apt-get -y update && \
    apt-get -y install gnupg2 ca-certificates procps && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "0x135659e928c12247" && \
    mv /etc/apt/sources.list.d/maxscale.list.tmp /etc/apt/sources.list.d/maxscale.list && \
    apt-get -y update && \
    apt-get -y install maxscale && \
    rm -rf /var/lib/apt/lists/* && \
    if [ ! -z $VERSION ] && [ ! -z $GIT_COMMIT ] && [ ! -z $BUILD_TIME ]; then \
       printf "Version:    $VERSION\nGit commit: $GIT_COMMIT$GIT_TREE_STATE\nBuilt:      $BUILD_TIME\n" > /opt/image_details; fi

# Optional: custom entrypoint script (mount this from host if needed)
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh && \
    ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh

# Start MaxScale via entrypoint (respects config from volume)
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]

