venv:
	python3.10 -m venv venv
	./venv/bin/pip install -r requirements.txt
run:
	python3 src/main.py