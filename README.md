# Proyecto Final – Automation Testing

Framework de automatización de pruebas desarrollado en Python como trabajo final integrador.

## 🚀 Tecnologías Utilizadas
- Python
- Pytest
- Selenium WebDriver
- Requests
- Pytest-HTML
- WebDriver Manager

## 📁 Estructura del Proyecto

proyecto-final-automation-testing-mario-cabral/
│
├── tests/
│ ├── ui/
│ │ └── test_sauce_demo.py
│ └── api/
│ └── test_api_jsonplaceholder.py
│
├── reports/
│ ├── screens/
│ └── reporte_completo.html
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md

markdown
Copiar código

## 🧪 Pruebas de UI
- Automatización sobre https://www.saucedemo.com
- Flujos cubiertos:
  - Login exitoso
  - Agregar producto al carrito
- Selenium + Pytest
- Captura automática de screenshots en caso de fallo

## 🔗 Pruebas de API
- API pública: JSONPlaceholder
- Métodos cubiertos:
  - GET
  - POST
  - DELETE
- Validación de status codes y contenido JSON

## 📊 Reportes
- Reporte HTML generado con pytest-html
- Incluye estado de los tests y evidencias visuales

## ▶️ Ejecución del Proyecto

1. Crear entorno virtual:
python -m venv venv

cpp
Copiar código

2. Activar entorno virtual:
venv\Scripts\activate

markdown
Copiar código

3. Instalar dependencias:
pip install -r requirements.txt

markdown
Copiar código

4. Ejecutar tests:
pytest

css
Copiar código

5. Generar reporte HTML:
pytest --html=reports/reporte_completo.html --self-contained-html

shell
Copiar código

## ✅ Autor
Mario Cabral
