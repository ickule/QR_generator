# Version updater

## Description

The script generates a QR code based on user input, including IRL and optionnally add an image in the center..

## Getting Started

### Dependencies

The following instruction assumes a debian-like environement.

The programm has been developed using python 3.10 and was tested on python 3.10.

Before creating a virtual environement, ensure that you have the python3-venv package installed.

```bash
sudo apt install python3-venv
```

The command below can be used to create a virtual environement. In this example, ".venv" has been chosen as a folder name for the virtual environement but can be modified based on preference. The ```--upgrade-deps``` argument ensures that your environement uses the latest pip3 and setutools modules.

```bash
python3 -m venv .venv --upgrade-deps
```

To activate your virtual environement, change your source to the one provided in the new environement.

```bash
source .venv/bin/activate
```

The ```activate``` file assumes the use of ```bash``` or ```zsh```. If ```csh``` or ```fish``` are used, please use the ```activate.csh``` or ```activate.fish``` accordingly.
If necessary, the virtual environement can be exited with the ```deactivate``` command.

### Installing

To install the requirement for the software, run the pip3 command below.

```bash
pip3 install -r requirements.txt
```

### Executing program

The programm can be run directly and only need the data to include into the QR code to run. The data can be either text or URL. By defualt, the QR code is saved in ```dist/QR.png```.

```bash
python3 qrgenerator/qrgenerator.py "mydata"
```

For more information on the available arguments, please run the help of the program.

```bash
python3 qrgenerator/qrgenerator.py -h
```

#### Examples

A few ecamples involving parameters are listed below.

```bash
python3 qrgenerator/qrgenerator.py "Hello world!"

python3 qrgenerator/qrgenerator.py "https://github.com"

python3 qrgenerator/qrgenerator.py "https://github.com" -i "my_logo.png" -o "/path/to/output"
```

### Developement

To develop the program further, please install the developement requirements.

```bash
pip3 install -r requirements_dev.txt
```

The code is linted with pylint, mypy and flake8. While pylint and mypy have been used with their default configuration, flake8 was used with custom arguments to accomodate  additionnal modules. The additionnal modules can be found in the requirements_dev.txt.

```bash
pylint /path/to/file

mypy /path/to/file

flake8 --max-line-length=100 --extend-select=B9 --ignore=E203,E501,E722,W503 /path/to/file
```

The code is formated with black using a line limit of 100 to match pylint's default value.

```bash
black --line-length 100 /path/to/file
```

## Acknoledgements

The work in this repository is based on the following: <https://www.geeksforgeeks.org/how-to-generate-qr-codes-with-a-custom-logo-using-python/>
