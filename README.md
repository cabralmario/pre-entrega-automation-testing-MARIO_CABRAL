# 🧪 Pre-Entrega de Proyecto – Automation Testing con Selenium y Pytest 

👨‍💻 **Autor:**  
Mario Cabral

---

## 📝 Descripción del Proyecto

Este proyecto corresponde a mi **Pre-Entrega** del curso de Automatización con **Python y Selenium**.  
El objetivo es demostrar la capacidad para automatizar flujos básicos de navegación web utilizando **Selenium WebDriver**, **Pytest** y **esperas explícitas**, aplicando buenas prácticas de testing automatizado.

🌐 **Sitio bajo prueba:**  
https://www.saucedemo.com/

---

## ⚙️ Funcionalidades Automatizadas

### 1️⃣ Login Automático
- Abre la página de SauceDemo.  
- Ingresa usuario y contraseña válidos.  
- Valida que el login sea exitoso verificando:
  - Redirección al inventario `/inventory.html`
  - Título de la página “Products”

### 2️⃣ Interacción con el Carrito
- Agrega un producto al carrito.  
- Verifica que el contador del carrito se incremente correctamente.  
- Accede al carrito y valida que el producto agregado esté presente.

---

## 🧰 Tecnologías Utilizadas
- 🐍 **Python 3**
- 🌐 **Selenium WebDriver**
- 🧪 **Pytest**
- 📊 **Pytest-HTML** (para reportes en HTML)
- 💻 **Google Chrome / ChromeDriver**

---

## 🧱 Estructura del Proyecto

pre-entrega-automation-testing-MARIO_CABRAL/
│
├── conftest.py
│
├── tests/
│ └── test_sauce_demo.py
│
├── utils/
│
├── reports/
│ └── reporte_completo.html
│
├── venv/
│
└── README.md

yaml
Copiar código

---

## ⚙️ Instalación y Configuración

1️⃣ **Clonar este repositorio:**
```bash
git clone https://github.com/mariocabral/pre-entrega-automation-testing-MARIO_CABRAL.git
2️⃣ Entrar al proyecto:

bash
Copiar código
cd pre-entrega-automation-testing-MARIO_CABRAL
3️⃣ Crear y activar el entorno virtual:

bash
Copiar código
python -m venv venv
venv\Scripts\activate
4️⃣ Instalar dependencias:

bash
Copiar código
pip install selenium pytest pytest-html
▶️ Ejecución de Pruebas
Para ejecutar los tests y generar el reporte HTML:

bash
Copiar código
pytest --html=reports/reporte_completo.html --self-contained-html -v
📁 El reporte se genera automáticamente en la carpeta reports/
y puede abrirse en el navegador.

📊 Resultados Esperados
✔ Login exitoso
✔ Producto agregado correctamente al carrito
✔ Reporte HTML generado sin errores

🏁 Conclusión
Este proyecto demuestra la capacidad para:

✅ Implementar automatización funcional con Selenium.
✅ Usar buenas prácticas de testing con Pytest.
✅ Documentar y estructurar un proyecto de forma profesional.