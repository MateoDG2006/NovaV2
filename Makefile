run:
	python -m nova

# Ejemplo: make run-ollama | make run-ollama MODEL=llama3
run-ollama:
	ollama run $(MODEL) --host 0.0.0.0 --port 11434