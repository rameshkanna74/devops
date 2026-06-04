mkdir -p ~/dev/

cd ~/dev

sudo apt install python3-venv

python3 -m venv py14

source py14/bin/activate

python3 -m pip install -U pip

python3 -m pip install -U ipykernel

pip freeze > requirements.txt
