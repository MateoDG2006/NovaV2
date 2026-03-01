<p align="center">
  <img src="https://img.shields.io/badge/Nova-v2-8b5cf6?style=for-the-badge&labelColor=1e1b4b" alt="Nova v2" />
</p>

```
  ███╗   ██╗ ██████╗ ██╗   ██╗ █████╗ 
  ████╗  ██║██╔═══██╗██║   ██║██╔══██╗
  ██╔██╗ ██║██║   ██║██║   ██║███████║
  ██║╚██╗██║██║   ██║╚██╗ ██╔╝██╔══██║
  ██║ ╚████║╚██████╔╝ ╚████╔╝ ██║  ██║
  ╚═╝  ╚═══╝ ╚═════╝   ╚═══╝  ╚═╝  ╚═╝
         ██╗   ██╗███████╗██████╗ ███████╗██╗ ██████╗ ███╗   ██╗
         ██║   ██║██╔════╝██╔══██╗██╔════╝██║██╔═══██╗████╗  ██║
         ██║   ██║█████╗  ██████╔╝███████╗██║██║   ██║██╔██╗ ██║
         ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██║██║   ██║██║╚██╗██║
          ╚████╔╝ ███████╗██║  ██║███████║██║╚██████╔╝██║ ╚████║
           ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

> ✨ **API y chat con modelos locales** vía Ollama · FastAPI

---

## 📋 Requisitos previos

| Requisito | Descripción |
|-----------|-------------|
| 🐍 **Python 3.8+** | Intérprete de Python |
| 🤖 **Ollama** | Opcional; para usar el chat: [ollama.ai](https://ollama.ai) |

---

## 🚀 Setup paso a paso

### 1️⃣ Clonar el repositorio (si aplica)

```bash
git clone <url-del-repo>
cd NovaV2
```

### 2️⃣ Crear y activar un entorno virtual

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno

Copia el archivo de ejemplo y edítalo según tu entorno:

```bash
# En la raíz del proyecto
copy envs\.local.env .env
```

O crea un `.env` en la raíz con al menos:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=phi
```

| Variable | Descripción |
|----------|-------------|
| **OLLAMA_BASE_URL** | URL del servidor Ollama (por defecto `http://localhost:11434`) |
| **OLLAMA_MODEL** | Nombre del modelo en Ollama (ej. `phi`, `llama3`, `mistral`) |

Otras variables opcionales (ver `nova/settings.py`): `DEBUG`, `SECRET_KEY`, `DATABASE_URL`, `ALLOWED_HOSTS`, `ENVIRONMENT`, `APP_NAME`, `APP_VERSION`.

### 5️⃣ (Opcional) Levantar Ollama

Si usas Ollama en la misma máquina:

```bash
# Ejecutar servidor Ollama con un modelo (ej. phi)
make run-ollama MODEL=phi
```

O manualmente:

```bash
ollama run phi --host 0.0.0.0 --port 11434
```

Asegúrate de tener el modelo descargado (`ollama pull phi`).

### 6️⃣ Ejecutar la aplicación

```bash
make run
```

O directamente:

```bash
python -m nova
```

La API quedará disponible en **http://localhost:8000**.

### 7️⃣ Probar

- 🌐 **Web:** http://localhost:8000/ y http://localhost:8000/chat
- 📤 **API chat (JSON):** `POST /chat` con body `{"content": "tu mensaje"}`
- 📡 **API chat (streaming):** `POST /chat-stream` con body `"tu mensaje"` (texto)

---

## 📁 Estructura del proyecto

```
NovaV2/
├── nova/
│   ├── __main__.py   # Punto de entrada (python -m nova)
│   ├── api.py        # FastAPI app y rutas
│   ├── llm.py        # Cliente Ollama y modelos
│   ├── settings.py   # Configuración desde .env
│   └── views.py      # Vistas HTML del chat
├── envs/
│   └── .local.env    # Ejemplo de variables de entorno
├── requirements.txt
├── Makefile
└── README.md
```

---

## ⌨️ Comandos útiles

| Comando | Descripción |
|--------|-------------|
| `make run` | Inicia la API en http://localhost:8000 con reload |
| `make run-ollama MODEL=phi` | Inicia Ollama con el modelo indicado |

---

## 🔧 Resolución de problemas

| Problema | Solución |
|----------|----------|
| **Ollama no responde** | Comprueba que Ollama esté en marcha y que `OLLAMA_BASE_URL` en `.env` coincida (puerto 11434 por defecto). |
| **Modelo no encontrado** | Ejecuta `ollama pull <nombre_modelo>` y usa ese nombre en `OLLAMA_MODEL`. |
| **Error al cargar .env** | El paquete correcto es `python-dotenv`; reinstala con `pip install -r requirements.txt`. |

---

<p align="center">
  <sub>Hecho con FastAPI · Ollama</sub>
</p>
