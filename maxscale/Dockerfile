FROM ubuntu:bionic

# Optional metadata
ARG VERSION
ARG GIT_COMMIT
ARG GIT_TREE_STATE
ARG BUILD_TIME

COPY maxscale.list /etc/apt/sources.list.d/maxscale.list.tmp

RUN apt-get update && \
    apt-get install -y gnupg2 ca-certificates wget curl && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x135659e928c12247 && \
    mv /etc/apt/sources.list.d/maxscale.list.tmp /etc/apt/sources.list.d/maxscale.list && \
    apt-get update && \
    apt-get install -y maxscale && \
    rm -rf /var/lib/apt/lists/*

COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]
CMD ["maxscale", "-f", "/etc/maxscale.cnf.d/example.cnf", "-d"]

