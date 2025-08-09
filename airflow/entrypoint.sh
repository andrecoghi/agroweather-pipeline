#!/bin/bash
set -e

# Cria as pastas de dados
mkdir -p /opt/airflow/data/raw /opt/airflow/data/processed

echo "Aguardando PostgreSQL ficar disponível..."
while ! pg_isready -h postgres -U admin > /dev/null 2>&1; do
  sleep 1
done

if [ ! -f /opt/airflow/airflow.cfg ]; then
  echo "Inicializando banco do Airflow..."
  airflow db init
else
  echo "Aplicando migrações no banco do Airflow..."
  airflow db upgrade
fi

# Tenta criar usuário admin
if ! airflow users list | grep -q admin; then
  echo "Criando usuário admin padrão..."
  airflow users create \
    --username admin \
    --firstname Andre \
    --lastname Coghi \
    --role Admin \
    --email andre@example.com \
    --password admin || echo "Não foi possível criar o usuário admin."
fi

echo "Iniciando serviço: $@"
exec airflow "$@"
