-- Comandos de instalación

# 1. Crear y activar entorno virtual
python -m venv venv
source venv/Scripts/activate

# 2. Actualizar pip
python -m pip install --upgrade pip

# 3. Instalar dependencias
pip install selenium pytest pytest-html webdriver-manager

# 4. Guardar dependencias
pip freeze > requirements.txt

# 5. (En otra máquina) reinstalar desde el archivo
pip install -r requirements.txt

# 6. Formatear código Python (indentación)
pip install ruff
ruff format .
ruff check . --fix

# 7.Comando para ejecutar test 
source venv/Scripts/activate
pytest tests -v
pytest tests/test_login.py -s
pytest tests/test_catalogo.py -s
pytest tests/test_carrito.py -s
pytest tests/test_compra.py -s

# 8.Comando para ejecutar reporte
pytest --html=reports/reporte.html --self-contained-html