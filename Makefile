test:
	pytest tests --cov=gbcli --cov-report=term-missing

format-code:
	black .
	ruff . --fix