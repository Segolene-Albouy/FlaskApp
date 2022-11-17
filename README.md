# Flask application skeleton

## Set-up

> Instructions are for Linux/macOS based distributions

### Pre-requisites

```bash
# Linux
sudo apt update
sudo apt install wget software-properties-common

# MacOS
sudo brew update
```
- `sudo` privileges
- `git` and [SSH access to GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) configured
```bash
sudo apt install git # Linux
git --version # MacOS
```
- `python3.9`: not working with python 3.10
```bash
# Check which python versions you have installed
ls /usr/bin/python*

# Linux
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.9

# MacOS
brew install python@3.9
```
- `pip3.9`
```bash
# Linux
sudo apt install python3.9-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
```
- `virtualenv`
```bash
apt install python3.9-dev python3.9-venv
```

### Install

1. Clone the repo and open a terminal in the folder
2. Create a virtual environment `venv` for the project
```shell
python3.9 -m venv venv
```
3. Activate the virtual environment
```shell
source venv/bin/activate
```
4. Install dependencies
```shell
python3.9 -m pip install -r requirements.txt
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
python3.9 run.py
```
3. Visit [localhost:5000](localhost:5000)
