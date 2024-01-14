# Educational CMS API

## Introduction

Educational Content Management System API is built with Django, designed for course creation, student enrollment, quiz administration, and progress tracking.


## Project Setup

### Dependencies

- `Django` and `djangorestframwework` for building the API
- `poetry` for managing dependencies
- `mypy` static typing
- `flake8` for linting
- `black` for code formatting
- `pre-commit` to enforces the linting and code formatting

### Code Formatting and Style

The project uses `black` for code formatting and `flake8` for linting, integrated through `pre-commit` hooks to ensure code consistency and quality.


### Running the Project

1. **Clone the Repository**
   ```bash
   git clone git@github.com:khasizadaj/edu_cms_api.git
   ```

2. **Install Dependencies**

   *Note*: This step expects `poetry` library to be installed at global scope.

   ```bash
   # in: edu_cms_api
   python3 -m poetry install

   # or
    
   python -m poetry install
   ```

3. **Environment Setup**
   ```bash
   cp .env.example .env
   # Edit .env to set your environment variables
   ```

4. Activate environment
   ```bash
   python3 -m poetry shell

   # or
    
   python -m poetry shell
   ```

5. **Install Pre-commit Hooks**
   ```bash
   pre-commit install
   ```

6. **Database Migrations**:
   ```bash
   # in: src
   make migrate
   ```

7. **Run the Server**:
   ```bash
   # in: src
   make run
   ```

8. **Access the API**:
   Available at `http://127.0.0.1:8000/`.

## Contributing

Adhere to code style guidelines and add tests for new features. Pre-commit hooks must be used to ensure code quality.

## Authors

- Javid "JAXA" Khasizada