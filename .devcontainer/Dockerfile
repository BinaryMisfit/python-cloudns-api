FROM python:3
ENV DEBIAN_FRONTEND=noninteractive
COPY ./.devcontainer/requirements.txt /tmp/pip-tmp/
RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    apt-utils \
    dialog \
    2>&1 \
    && apt-get -y install --no-install-recommends \
    git \
    iproute2 \
    lsb-release \
    procps \
    2>&1 \
    && pip --disable-pip-version-check --no-cache-dir install \
    autopep8 \
    pylint \
    && pip --disable-pip-version-check --no-cache-dir install \
    -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp \
    && apt-get install -y sudo 2>&1 \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*
ENV DEBIAN_FRONTEND=
