from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# El archivo de texto donde se guardará todo permanentemente
ARCHIVO_DB = "tickets.json"

class Ticket(BaseModel):
    id: Optional[int] = None
    titulo: str
    descripcion: str
    prioridad: str
    estado: str = "Pendiente"

# 💾 FUNCIÓN AYUDANTE: Guarda la lista en el archivo JSON
def guardar_datos(tickets_lista):
    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
        # Convertimos los objetos Pydantic a diccionarios para poder guardarlos
        lista_dicts = [ticket.model_dump() for ticket in tickets_lista]
        json.dump(lista_dicts, f, indent=4, ensure_ascii=False)

# 📖 FUNCIÓN AYUDANTE: Lee los datos del archivo JSON al iniciar
def cargar_datos() -> List[Ticket]:
    if not os.path.exists(ARCHIVO_DB):
        return []
    try:
        with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
            lista_dicts = json.load(f)
            return [Ticket(**d) for d in lista_dicts]
    except:
        return []

# Inicializamos la base de datos cargando lo que haya en el archivo
base_de_datos_tickets = cargar_datos()

# El ID inicial será el número más alto que ya exista + 1, o 1 si está vacío
id_actual = max([t.id for t in base_de_datos_tickets], default=0) + 1


@app.get("/")
def home():
    return {"mensaje": "¡Servidor de Tickets con persistencia activo!"}

@app.get("/tickets", response_model=List[Ticket])
def obtener_tickets():
    # Siempre cargamos del archivo para asegurar que tenemos lo último
    global base_de_datos_tickets
    base_de_datos_tickets = cargar_datos()
    return base_de_datos_tickets

@app.post("/tickets", response_model=Ticket)
def crear_ticket(ticket: Ticket):
    global id_actual, base_de_datos_tickets
    
    ticket.id = id_actual
    id_actual += 1
    
    base_de_datos_tickets.append(ticket)
    guardar_datos(base_de_datos_tickets) # <-- Guardamos en el disco duro
    return ticket

@app.put("/tickets/{ticket_id}", response_model=Ticket)
def actualizar_estado_ticket(ticket_id: int, nuevo_estado: str):
    global base_de_datos_tickets
    base_de_datos_tickets = cargar_datos()
    
    for ticket in base_de_datos_tickets:
        if ticket.id == ticket_id:
            ticket.estado = nuevo_estado
            guardar_datos(base_de_datos_tickets) # <-- Guardamos la actualización
            return ticket
            
    raise HTTPException(status_code=404, detail="Ticket no encontrado")