FROM danwos/sphinxneeds:latest

USER root

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    unzip \
    zip \
    ca-certificates \
    build-essential \
    locales \
    vim \
    nano \
    htop \
    && rm -rf /var/lib/apt/lists/*
    

RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8