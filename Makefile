install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

generate_and_push:
	python main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "GitHub Action"; \
	git add .
	git commit -m "Add generated plot and report"
	git push
	
all: install lint test format generate_and_push