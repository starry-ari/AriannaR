Flask Web-app Portfolio Site

## Introduction

This is a portfolio project from Week 1 of Summer 2022 MLH Fellowship Product Engineering track. It uses Bootstrap components and Jinja to dynamically display the site.

## Installation

Clone this repository into your local environment.

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

If an error message comes up saying "No module named 'dotenv', try

```bash
$ python -m pip install python-dotenv
```
Then deactivate the virtual environment
```bash
$ source deactivate
```
And open the virtual environment again using the instructions from above. Run `flask run` again and see if it works then.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
