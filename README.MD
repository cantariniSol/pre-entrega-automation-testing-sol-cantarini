# Pre-entrega Automation Testing

Automatización de [saucedemo.com](https://www.saucedemo.com/) con **Python, Pytest y Selenium WebDriver**, usando Page Object Model.

## Instalación

```bash
python -m venv venv
source venv/Scripts/activate      # Git Bash en Windows
pip install -r requirements.txt
```

Requiere Google Chrome instalado. El driver se descarga solo con `webdriver-manager`.

## Ejecución

```bash
pytest                                                    # todos los tests
pytest --html=reports/reporte.html --self-contained-html  # con reporte HTML
```

## Casos de prueba

| Archivo | Qué valida |
|---|---|
| `tests/test_login.py` | Login válido (`/inventory.html`, "Products", título "Swag Labs") y login con contraseña incorrecta |
| `tests/test_catalogo.py` | Título, presencia de productos, nombre y precio del primero, detalle y agregar/quitar |
| `tests/test_carrito.py` | Agregar, quitar y verificar productos en el carrito |
| `tests/test_compra.py` | Compra completa hasta "Thank you for your order!" |

Los tests son independientes: cada uno abre su propio navegador.

## Estructura

```
configs/   constantes (URL, usuario, timeout)
helpers/   clic con espera explícita
pages/     Page Objects (login, inventario, carrito, checkout)
tests/     casos de prueba y fixtures (conftest.py)
reports/   reporte HTML
```

# Logs de ejecución: 
logs/ejecucion.log

## Autora

Sol Cantarini