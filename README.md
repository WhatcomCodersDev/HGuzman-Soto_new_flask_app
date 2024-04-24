# bootstrap_python_example

Brief description of what your application does and what problem it solves.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Installing

pip install -r requirements.txt

### Running

gunicorn -b localhost:8000 run:app
