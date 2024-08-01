# Playwright Python

### Installation using poetry

#### Installing Poetry

Poetry can be installed via python standard package manager PIP

    pip install poetry

#### Starting environment

To spawn poetry session inside your environment, write

    poetry shell

> This command starts a new shell and activates the virtual environment.
> As such, exit should be used to properly exit the shell and the virtual environment instead of deactivate.

#### Adding dependencies

To add a new dependency to your project, use the add command:

    poetry add <package>

This will add the requests package to your project and update the pyproject.toml file.

#### Installing dependencies

To install dependencies defined in `pyproject.toml`, simply run

    poetry install

### Pre-commit

Pre-commit is a framework used for pre-commits git hooks management. It allows to define actions that confirm that
written code is formatted and configured properly according to defined practices.


#### Running pre-commit automatically

To run validation automatically before each commit, please use:

    pre-commit install

This will add pre-commit to git hooks and perform all the checks defined in `.pre-commit-config.yaml`

#### Running pre-commit manually

To check stying in all files, please use:

    pre-commit run -a


## Running tests

This project uses `pytest` with `pytest-playwright` as a test runner.

### Defining test choice

#### Running all

To run all the scripts with default setting simply type:

    pytest

#### Running specific test

    pytest tests/test_xxxx.py::test_xxx_xxx


### Developer friendly run commands

This will run tests in a headed browser with a delay of 500 milliseconds between actions. It will make observing browser
behaviour easier.

    pytest --headed --slowmo 500

### Running Tests on Specific Browsers

To run tests on specific browsers, use the Pytest command with the --browser option:

    pytest --browser firefox

This will run tests on Firefox. You can also specify multiple browsers:

    pytest --browser firefox --browser chromium

### Other running options

#### Parallel execution

This repo uses `pytest-xdist` package to allow multiple test being performed in parallel.
Here is an example of running 5 parallel sessions on 3 browsers:

    pytest --base-url https://automationexercise.com -n 5 --browser chromium --browser firefox --browser webkit

#### Artifacts

Playwright comes with video recording and screen capturing out of the box. The results are saved in test-results
directory by default.

    pytest --screenshot={on,off,only-on-failure}

    pytest --video={on,off,retain-on-failure}

## GitHub Actions

The purpose of Continuous integration in this repo is to:

1. Validate created Pull Requests - confirm the pre-commit and test are passing
2. Create a template for regularly launched tasks that will Test the targeted environment

