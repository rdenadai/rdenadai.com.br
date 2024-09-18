FROM python:3.12.6-alpine3.20

WORKDIR /code

RUN apk update && \
    apk add dumb-init curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    rm -rf /var/cache/apk/*

COPY ./pyproject.toml ./README.md /code/

ENV UV_TOOL_BIN_DIR=/root/.cargo/bin/
ENV PATH=$UV_TOOL_BIN_DIR:$PATH
RUN uv sync

ENTRYPOINT ["dumb-init", "--"]
CMD ["tail", "-f", "/dev/null"]