FROM python:3.11-slim

WORKDIR /app

# Instala dependencias necesarias del sistema
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    build-essential \
    libpq-dev \
    libmariadb-dev-compat \
    libmariadb-dev \
    pkg-config \
    netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

# Copia y da permisos al script de espera
COPY wait-for-mysql.sh /app/wait-for-mysql.sh
RUN chmod +x /app/wait-for-mysql.sh

# Instala dependencias Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código
COPY . .

EXPOSE 8000

# Usa el script para esperar que MySQL esté listo antes de iniciar
CMD ["/app/wait-for-mysql.sh", "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
