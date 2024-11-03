# Network and Database Programming - Midterm Project

- [Description](#description)
- [Installation](#installation)
- [Execution](#execution)

## Description

This project demonstrates a proof of concept for tracking machine learning experiments using a Python decorator named `track`. The `track` decorator automatically logs the parameters and results of each experiment to an SQLite database.

## Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up a virtual environment**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -e .
    ```

## Execution

1. **Run the main script**:
    ```sh
    python main.py
    ```

This will execute the `train` function with the `@track` decorator, which will track the parameters and results of the experiment and store them in an SQLite database, default to "track.db" in the root directory.