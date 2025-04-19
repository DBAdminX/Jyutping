pip freeze > requirements.txt

pip install -r requirements.txt

pyinstaller --onefile --windowed `
           --name "Jyutping" `
           --add-data="venv/Lib/site-packages/jyutping/data/*;jyutping/data" `
           --hidden-import="jyutping.data" `
           --hidden-import="pkg_resources.py2_warn" `
           --clean `
           jyut.py