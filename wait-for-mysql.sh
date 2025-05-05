#!/bin/sh

echo "Esperando a que MySQL esté disponible..."

while ! nc -z "$DB_HOST" 3306; do
  sleep 1
done

echo "MySQL está listo. Iniciando aplicación..."

exec "$@"
