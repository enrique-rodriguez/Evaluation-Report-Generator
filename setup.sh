python3 -m venv venv
. venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
python3 -m unittest discover .
