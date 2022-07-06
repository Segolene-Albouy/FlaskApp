# Flask application skeleton

## Set-up

### Pre-requisites

- `python3.9`: not working with python 3.10
- `pip3`
- `conda`

### Install

1. Clone the repo and open a terminal in the folder
2. Create a virtual environment `venv` for the project
```shell
python -m venv venv
```
3. Activate the virtual environment
```shell
source venv/bin/activate
```
4. Install dependencies
```shell
python -m pip install -r requirements.txt
```
5. Enable pre-commit hooks (automatic tests and formatting on each commit)
```shell
pre-commit install
```

## Run the app
1. Activate the virtual environment
```shell
source venv/bin/activate
```
2. Launch the Flask application
```shell
python run.py
```
3. Visit [localhost:5000](localhost:5000)
