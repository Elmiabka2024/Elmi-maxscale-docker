FROM ubuntu:bionic

# Add MariaDB MaxScale APT repo
COPY maxscale.list /etc/apt/sources.list.d/maxscale.list

# Install MaxScale and procps (for pgrep)
RUN apt-get update && \
    apt-get install -y gnupg2 ca-certificates && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x135659e928c12247 && \
    apt-get update && \
    apt-get install -y maxscale procps && \
    rm -rf /var/lib/apt/lists/*

# Add MaxScale config
COPY maxscale.cnf /etc/

# Create a non-root user
RUN useradd -ms /bin/bash maxscaleuser && \
    mkdir -p /var/run/maxscale && \
    chown -R maxscaleuser:maxscaleuser /etc/maxscale.cnf /var/run/maxscale

USER maxscaleuser

# Start MaxScale
ENTRYPOINT ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]

