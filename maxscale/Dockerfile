FROM ubuntu:bionic

# Add MariaDB MaxScale APT repo
COPY maxscale.list /etc/apt/sources.list.d/maxscale.list

# Install MaxScale and procps (fixes missing `pgrep` issue)
RUN apt-get update && \
    apt-get install -y gnupg2 ca-certificates procps && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x135659e928c12247 && \
    apt-get update && \
    apt-get install -y maxscale && \
    rm -rf /var/lib/apt/lists/*

# Add MaxScale config file
COPY maxscale.cnf /etc/maxscale.cnf

# Use root user as required by Python script (user=root, password=maxpwd)
# Create a dummy `maxscale` Linux user to match `-U maxscale` argument
RUN useradd -ms /bin/bash maxscale && \
    mkdir -p /var/run/maxscale && \
    chown -R maxscale:maxscale /etc/maxscale.cnf /var/run/maxscale

USER maxscale

# Start MaxScale with user 'maxscale'
ENTRYPOINT ["maxscale", "-d", "-U", "maxscale", "-l", "stdout"]

