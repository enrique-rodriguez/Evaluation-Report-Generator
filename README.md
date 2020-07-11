# Report Generator
This project creates a simple report of all of the evalutions files given and outputs it into a new file in a specific format (excel, pdf, etc).


## Installation

Windows, OS X & Linux:

```sh
pip3 install -r requirements.txt
```


## Usage example

### Running the GUI
```sh
python3 main.py
```

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements_dev.txt
```

Compiling the GUI executable

```sh
python3 pyinstaller -w --onefile entrypoint/gui/main.py
```

### Running the Tests

```sh
python3 -m unittest discover .
```

```
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

## Meta

Enrique Rodriguez – enrique.rodriguez9@upr.edu
Kendrick Morales – kendrick.morales@upr.edu

[https://github.com/enrique-rodriguez/report-generator](https://github.com/enrique-rodriguez/report-generator)
