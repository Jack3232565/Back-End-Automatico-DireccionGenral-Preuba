from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa CORSMiddleware
from fastapi.staticfiles import StaticFiles  # Importa StaticFiles

from routes.persona import persona
from routes.usuarios import usuario
from routes.users import user
from routes.persons import person
from routes.roles import roles
from routes.tbb_usuarios import tbb_usuarios_router
from routes.usuario_roles import usuario_roles_router
from routes.areas_medicas import areas_medicas
from routes.tbc_servicios_medicos import servicios_medicos
from routes.tbc_departamentos import departamentos  
from routes.tbb_personal_medico import personal_medico
from routes.tbb_pacientes import tbb_pacientes
from routes.tbd_solicitudes import tbd_solicitudes_router
from routes.tbb_aprobaciones import tbb_aprobaciones
from routes.bitacora import bitacora
import logging

# Importa database.py para que se ejecuten las funciones de creación de tablas
from models.database import create_tables  # Importa create_tables aquí
create_tables()  # Asegúrate de que las tablas se crean al iniciar la aplicación

app = FastAPI()


# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes de origen cruzado. Puedes especificar una lista de dominios permitidos.
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)

# Registrar los routers
app.include_router(persona, tags=["Personas"])
app.include_router(usuario, tags=["Usuarios"])
app.include_router(user)
app.include_router(person)
app.include_router(roles)
app.include_router(tbb_usuarios_router)
app.include_router(usuario_roles_router)
app.include_router(areas_medicas)
app.include_router(servicios_medicos)
app.include_router(departamentos)
app.include_router(personal_medico)
app.include_router(tbb_pacientes)
app.include_router(tbd_solicitudes_router)
app.include_router(tbb_aprobaciones)
app.include_router(bitacora)

# Configurar el directorio de archivos estáticos
app.mount("/uploads", StaticFiles(directory="uploads", html=False), name="uploads")

# Mensaje de bienvenida usando logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Bienvenido a mi aplicación")
