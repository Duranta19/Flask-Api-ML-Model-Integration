# Flask Application Setup Guide

This guide provides step-by-step instructions to set up this Flask application.

## Prerequisites

Make sure you have the following installed:

- Python (>= 3.6)
- pip (Python package manager)
- virtualenv (optional but recommended)

## Setup Instructions

### 1. Create a Virtual Environment

Run the following command in your project directory:

```sh
python -m venv .env
```

This will create a virtual environment named `.env`.

### 2. Activate the Virtual Environment

- **Windows (cmd/PowerShell)**:
  
  ```sh
  venv\Scripts\activate
  ```

- **Mac/Linux**:
  
  ```sh
  source venv/bin/activate
  ```

### 3. Install Required Packages

Make sure you have a `requirements.txt` file in the project directory. Then run:

```sh
pip install -r requirements.txt
```

### 4. Run the Flask Application

To start the Flask application, use:

```sh
python app.py
```

or if using Flask's built-in development server:

```sh
flask run
```

Make sure `FLASK_APP` is set correctly before running `flask run`:

```sh
export FLASK_APP=app.py  # Mac/Linux
set FLASK_APP=app.py      # Windows (cmd)
$env:FLASK_APP = "app.py" # Windows (PowerShell)
```

### Additional Tips

- To deactivate the virtual environment, run:

  ```sh
  deactivate
  ```
### Api end point
- Test server:
    ```sh
    http://localhost:5050/test
    ```
- Predict Class:
    ```sh
    http://localhost:5050/predict
    ``