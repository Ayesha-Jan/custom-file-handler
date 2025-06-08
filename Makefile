.PHONY: test lint format clean

test:
	pytest

lint:
	flake8 main.py test_main.py

format:
	black main.py test_main.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -f combined_files.txt multi_combined_files.txt