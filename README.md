# airoh
_Because reproducible science takes good tea and clean tasks_

**airoh** is a lightweight Python task library built with [`invoke`](https://www.pyinvoke.org/), designed for reproducible research workflows. It provides pre-written, modular task definitions that can be easily reused in your own `tasks.py` file — no boilerplate, just useful automation.

## Installation

For local deployment:

```bash
git clone https://github.com/simexp/airoh.git
cd airoh
pip install -e .
```

## Usage

You can use `airoh` in your project simply by importing tasks in your `tasks.py` file. 

### Minimal Example

```python
# tasks.py
from airoh.utils import run_figures, setup_env_python
```

Now you can call:

```bash
invoke run-figures
invoke setup-env-python
```

## Available Tasks

### From `containers.py`

* `docker-build` — Build a Docker image from a Dockerfile
* `docker-archive` — Archive the Docker image to `.tar.gz`
* `docker-setup` — Download and load a Docker image from URL
* `docker-run` — Run an `invoke` task inside Docker
* `apptainer-archive` — Build an Apptainer image from Docker
* `apptainer-run` — Run an `invoke` task inside Apptainer

### From `utils.py`

* `setup-env-python` — Install Python dependencies from a file
* `run-figures` — Run Jupyter notebooks to generate figures
* `clean_folder(...)` — Utility to recursively delete directories (not a task)

## Requirements

* Python ≥ 3.8
* [`invoke`](https://www.pyinvoke.org/) ≥ 2.0
* Docker (for container tasks)
* Apptainer (optional, for `.sif` support)
* `jupyter` (if using `run-figures`)

## Philosophy

Inspired by Uncle Iroh from *Avatar: The Last Airbender*, `airoh` aims to bring simplicity, reusability, and clarity to research infrastructure — one well-structured task at a time. It is meant to support a concrete implementation of the [YODA principles](https://handbook.datalad.org/en/latest/basics/101-127-yoda.html).

## License

MIT © Lune Bellec
