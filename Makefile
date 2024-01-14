PORT = 8000
LOCALSERVER = 127.0.0.1

run:
	python src/manage.py runserver ${LOCALSERVER}:${PORT}

help:
	@echo "--------------- HELP ---------------"
	@echo "To install the project -> make install"
	@echo "To get help -> make help"
	@echo "To run localserver -> make run"
	@echo "To test the project -> make test"
	@echo "To migrate database -> make migrate"
	@echo "------------------------------------"

install:
	poetry install

migrate:
	python src/manage.py migrate

test:
	python src/manage.py test

.PHONY: install pre-commit run test
