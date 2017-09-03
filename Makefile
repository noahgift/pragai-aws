setup:
	python3 -m venv ~/.pragia-aws

install:
	pip install -r requirements.txt

test:
	PYTHONPATH=. && pytest -vv --cov=paws tests/*.py

lint:
	pylint --disable=R,C paws

all: install lint test