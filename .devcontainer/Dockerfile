FROM danwos/sphinxneeds:latest

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
    
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
