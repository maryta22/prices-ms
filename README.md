# 🐳 Prices-MS – Ejecutar con Docker Compose

Este proyecto levanta una API Django llamada **Prices-MS**, encargada de la gestión de productos, precios, promociones y tiendas. Usa `docker-compose` para facilitar la ejecución en cualquier entorno.

---

## ⚙️ Requisitos

- Docker
- Docker Compose

---

## 🚀 Cómo levantar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/maryta22/prices-ms.git
cd prices-ms
```

### 3. Construir y levantar los servicios

```bash
docker-compose up --build
```

## 🛑 Detener los contenedores

```bash
docker-compose down
```



## ♻️ Reconstruir todo desde cero

```bash
docker-compose down -v --remove-orphans
docker-compose build --no-cache
docker-compose up
```

Esto elimina volúmenes, reconstruye imágenes y levanta contenedores limpios.

---

## 📬 Accesos rápidos

- **API Django**: [http://localhost:8000]
- **Admin de Django**: [http://localhost:8000/admin]

---

## 📄 Licencia

Atado al autor