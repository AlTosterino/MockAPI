PROJ_PTH=$(dir $(abspath $(lastword $(MAKEFILE_LIST))))
PYTHON_EXEC?=python
APP_PATH = src/mock_api

LINT_PATHS = \
$(APP_PATH) \
tests \

lint:
	$(PYTHON_EXEC) -m autoflake --in-place --recursive --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables --remove-all-unused-imports $(LINT_PATHS)
	$(PYTHON_EXEC) -m black $(LINT_PATHS)
	$(PYTHON_EXEC) -m isort $(LINT_PATHS)
	$(PYTHON_EXEC) -m mypy $(APP_PATH) --ignore-missing-imports

test-ci:
	$(PYTHON_EXEC) -m autoflake --check --recursive --ignore-init-module-imports --remove-duplicate-keys --remove-unused-variables --remove-all-unused-imports $(LINT_PATHS) > /dev/null
	$(PYTHON_EXEC) -m isort --check-only $(LINT_PATHS)
	$(PYTHON_EXEC) -m black --check $(LINT_PATHS)
	$(PYTHON_EXEC) -m mypy $(APP_PATH) --ignore-missing-imports
	$(PYTHON_EXEC) -m tox

test:
	$(PYTHON_EXEC) -m pytest
