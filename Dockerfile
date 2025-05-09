FROM python:3.12.10-alpine3.21

WORKDIR /code

RUN apk update && \
    apk add dumb-init curl && \
    rm -rf /var/cache/apk/*

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

COPY ./pyproject.toml ./README.md ./uv.lock /code/

RUN uv sync --frozen

# ENTRYPOINT ["dumb-init", "--"]
# CMD ["tail", "-f", "/dev/null"]