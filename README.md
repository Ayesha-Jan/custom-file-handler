# 📂 Custom File Handler & 🎲 Dice Roll Simulator

This repository contains two Python projects demonstrating different features:

---

# 📂 Custom File Handler

This project demonstrates the creation of a custom Python object for file handling, with support for file reading via generators, operator overloading, decorators, inheritance, and automated testing using pytest.

---

## Features

- Custom file object with getter/setter validation
- File reading using Python generators
- Operator overloading with + to concatenate files
- Custom ANSI-colored string representation via decorators
- Inheritance with extended functionality in a subclass
- Support for concatenating multiple files
- Unit testing using pytest
- Linting and formatting with flake8 and black
- GitHub Actions CI for automated tests and formatting
- Makefile for easy development workflow

---

# 🎲 Dice Roll Simulator

Simulates dice rolls and plots their frequency distribution using matplotlib. Demonstrates generators, decorators, plotting, and automated testing.

---

## Features

- Generator function for dice rolls
- Decorator to plot roll frequency distributions
- Matplotlib visualization
- Automated tests with pytest
- Linting and formatting with flake8 and black
- Makefile commands integrated with main project

## Project Structure

<pre> custom-file-handler/ 
  ├── file_handler.py          # Core logic
  ├── test_file_handler.py     # Unit tests using pytest
  ├── dice_simulation.py       # Core simulation and plotting code
  ├── test_dice_simulation.py  # Unit tests using pytest
  ├── requirements.txt         # Python dependencies
  ├── Makefile                 # Developer commands
  ├── github/workflows/
  │   └── python_app.yml       # GitHub Actions workflow </pre>

---

## Getting Started

### Prerequisites

- Python 3.9+

### Clone the Repository 
    
    git clone https://github.com/Ayesha-Jan/custom-file-handler.git
    cd custom-file-handler

---

## How to Run Tests
Make sure you have a Python virtual environment set up:

    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt

Then run:

    make test

---

## Makefile Commands

    make test      # Run tests using pytest
    make lint      # Lint code with flake8
    make format    # Format code with black
    make clean     # Remove .pyc and cache files

---

## Author

Developed by: Ayesha A. Jan  
Email: Ayesha.Jan@stud.srh-campus-berlin.de  
🎓 BST Programming Project – 2025
