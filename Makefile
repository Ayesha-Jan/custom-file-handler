.PHONY: install test lint format clean

install:
	pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

test:
	pytest

lint:
	flake8 file_handler.py test_file_handler.py dice_simulation.py test_dice_simulation.py --max-line-length=120

format:
	black file_handler.py test_file_handler.py dice_simulation.py test_dice_simulation.py

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -f combined_files.txt multi_combined_files.txt
