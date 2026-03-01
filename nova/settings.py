import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# Variables de configuración
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
SECRET_KEY = os.getenv('SECRET_KEY', 'tu-clave-secreta-por-defecto')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# Configuraciones de la aplicación
APP_NAME = os.getenv('APP_NAME', 'Nova')
APP_VERSION = os.getenv('APP_VERSION', '2.0')
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL')

