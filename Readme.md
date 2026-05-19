# 🎫 Sistema de Gestión de Tickets (Full-Stack)<br>

Un sistema web interactivo para la creación, visualización y gestión de tickets de soporte técnico. Este proyecto fue desarrollado con una arquitectura desacoplada, conectando un frontend dinámico con un backend asíncrono y almacenamiento persistente local.

---

## 🚀 Características Clave<br>

- **Arquitectura Full-Stack:** Separación limpia entre el Frontend (Cliente) y el Backend (API).<br>
- **Backend Asíncrono:** Construido con FastAPI para un rendimiento óptimo y validación de datos automática con Pydantic.<br>
- **Persistencia de Datos:** Implementación de lectura y escritura en un archivo JSON local, asegurando que la información no se pierda al reiniciar el servidor.<br>
- **Frontend Interactivo:** Interfaz limpia estructurada en dos columnas (Formulario y Panel Activo) con consumo de API mediante JavaScript asíncrono (`fetch`, `async/await`).<br>
- **Diseño Estético y Ordenado:** Separación de estilos en archivos CSS independientes para una mejor mantenibilidad del código.<br>

---

## 🛠️ Tecnologías Utilizadas<br>

**Backend:**<br>
- Python 3<br>
- FastAPI (Framework de API web)<br>
- Uvicorn (Servidor ASGI)<br>
- Pydantic (Validación de esquemas y tipos de datos)<br>

**Frontend:**<br>
- HTML5 y CSS3 (Diseño responsivo y limpio)<br>
- JavaScript Moderno (Manipulación del DOM y peticiones HTTP asíncronas)<br>

---

## 📂 Estructura del Proyecto<br>

```text
Sistema-de-Tickets/<br>
│<br>
├── Backend/<br>
│   ├── main.py          # Servidor FastAPI y lógica de rutas (CRUD)<br>
│   └── tickets.json     # Base de datos local persistente en formato JSON<br>
│<br>
├── Frontend/<br>
│   ├── css/<br>
│   │   └── style.css    # Hojas de estilo independientes<br>
│   └── index.html       # Interfaz de usuario e inyección de JS dinámico<br>
│<br>
└── README.md            # Documentación del proyecto

## Instrucciones de Ejecución<br>
1. Clonar el repositorio<br>

git clone [https://github.com/TuUsuario/Sistema-de-Tickets.git](https://github.com/TuUsuario/Sistema-de-Tickets.git)
cd Sistema-de-Tickets

2. Levantar el Backend<br>

cd Backend
python3 -m uvicorn main:app --reload

El servidor estará disponible en: http://127.0.0.1:8000

Puedes probar la documentación interactiva en: http://127.0.0.1:8000/docs

3. Levantar el Frontend<br>
Abre el archivo Frontend/index.html utilizando la extensión Live Server en VS Code o levanta un servidor web local con Python:<br>

cd Frontend
python3 -m http.server 3000

Accede desde tu navegador a: http://127.0.0.1:3000

🎯 Próximas Mejoras (Roadmap)<br>
[ ] Implementar un sistema de actualización de estados directamente desde la interfaz del panel (Mover de Pendiente a En proceso o Resuelto).<br>

[ ] Migración del almacenamiento local JSON a una base de datos relacional (SQLite / PostgreSQL).<br>

[ ] Implementación de un buscador o filtros por nivel de prioridad en el panel.