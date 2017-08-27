setup:
	python3 -m venv ~/.pragia-aws

install:
	pip install -r requirements.txt

test:
	#cd src/chapter7; py.test --nbval-lax notebooks/*.ipynb

lint:
	#cd src/chapter7; pylint --disable=W,R,C *.py

lint-warnings:
	#pylint --disable=R,C *.py