# python-template
- Poetry-based Python project template
- Includes tool settings to maintain code quality

## Requirements
- Python>=3.10
- Poetry>=1.2.2
- [Optional] Pyenv>=2.3.8

## Install
- [Optional] Python Environment Settings(Using pyenv)
```
pyenv install 3.10
```
- Poetry
```
poetry install
```
- Pre Commit
```
poetry shell
pre-commit install
```

## Tools
- pycln
```
pycln .
```
- isort
```
isort .
```
- black
```
black .
```
- pylint
```
pylint **/*.py
```
- pytest
```
pytest
```
- mypy
```
mypy .
```

## Structure
```
python-template
│
├── .github/ - github settings directory
│   ├── CODEOWNER
│   ├── PULL_REQUEST_TEMPLATE.md
├── app_name/ - source code root(used by renaming)
│   ├── __init__.py
│   ├── name.py - sample code
├── tests/ - test code root
│   ├── __init__.py
│   ├── test_name.py - sample test code
├── .gitignore
├── .pre-commit-config.yml - pre-commit configuration file
├── poetry.lock
├── pyproject.toml - project configuration file
├── README.md
```