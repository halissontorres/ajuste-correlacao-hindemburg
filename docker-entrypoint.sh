#!/bin/bash
set -e

echo "Iniciando aplicação na porta: $PORT"
echo "Ambiente: $FLASK_ENV"

if [ "$FLASK_ENV" = "dev" ]; then
    echo "Iniciando em modo de desenvolvimento com Flask..."
    export FLASK_APP=./service.hm_rest_service.py
    export FLASK_DEBUG=1
    exec flask run --host=0.0.0.0 --port="$PORT"
else
    echo "Iniciando em modo de produção com Gunicorn..."
    CMD_ARGS=()
    for arg in "$@"; do
        eval arg="$arg"
        CMD_ARGS+=("$arg")
    done
    exec "${CMD_ARGS[@]}"
fi