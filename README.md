# FastAPI AI Project

This is a FastAPI project template designed to run an AI model. The template provides a structured and organized way to build and deploy a FastAPI application that integrates AI capabilities.


## Project Structure

The project is organized as follows:

```
fastapi-ai-project/
├── run_server.py
├── src/
│ ├── app/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── models.py
│ │ ├── router.py
│ │ ├── services/
│ │ │ ├── init.py
│ │ │ ├── ai_model.py
│ │ └── utils/
│ │ ├── init.py
│ │ └── helper.py
│ ├── entry/
│ │ ├── init.py
│ │ └── entry_point.py
├── .pre-commit-config.yaml
├── .github/
│ └── workflows/
│ └── ci.yml
├── pyproject.toml
├── poetry.lock
├── README.md
└── .gitignore
```

```perl

- **`run_server.py`**: Entry point to run the server.
- **`src/app/`**: Contains the FastAPI application code.
  - **`main.py`**: Main FastAPI application.
  - **`models.py`**: Pydantic models for request and response schemas.
  - **`router.py`**: API routes.
  - **`services/`**: Contains the AI model logic.
    - **`ai_model.py`**: AI model prediction logic.
  - **`utils/`**: Utility functions.
- **`src/entry/`**: Entry point related code.
  - **`entry_point.py`**: Initialization and configuration code.
- **`.pre-commit-config.yaml`**: Configuration for pre-commit hooks.
- **`.github/workflows/ci.yml`**: GitHub Actions workflow for continuous integration.
- **`pyproject.toml`**: Poetry configuration file.
- **`poetry.lock`**: Poetry lock file.
- **`README.md`**: Project documentation.
- **`.gitignore`**: Git ignore file to exclude unnecessary files.

## Getting Started

### Prerequisites

Make sure you have Python 3.12+ and Poetry installed on your system. You can install Poetry by following the [official instructions](https://python-poetry.org/docs/#installation).
```

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/hslrock/fastapi-ai-project.git
   cd fastapi-ai-project
```


2. Install the dependencies:

```bash
poetry install
```
3. Activate the virtual environment:

```bash
poetry shell
```
4. Install pre-commit hooks:

```bash
pre-commit install
```
5. Running the Server
To run the server, execute the following command:
```bash
python run_server.py
#The server will start on http://0.0.0.0:8000.
```


## Running with Docker
### Building the Docker Image
To build the Docker image, run the following command:

```
docker build -t fastapi-ai-project .
docker run -p 8000:8000 fastapi-ai-project
```

## Reference:

All these are made from ChatGPT 4o, and any mistakes are not my fault (well my fault beliving OpenAI) but ChatGPT4o. lol.

Feel free to leave any comment, if any improvement suggested.
