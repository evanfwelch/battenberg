# milhoja

[![image](https://img.shields.io/pypi/v/milhoja.svg)](https://pypi.python.org/pypi/milhoja)

[![image](https://img.shields.io/travis/rmedaer/milhoja.svg)](https://travis-ci.org/rmedaer/milhoja)

Battenberg is a tool built atop of Cookiecutter to keep Cookiecut projects in sync with their parent templates.
Under the hood, Battenberg relies on Git to manage the merging, diffing, and conflict resolution story. The first
goal of Battenberg is to provide an *upgrade* feature to Cookiecutter.

## Usage

Install a [Cookiecutter](https://github.com/audreyr/cookiecutter)
template on current directory:

    ```bash
    milhoja install <your cookiecutter>
    ```

Specify a target reference (branch, tag, commit):

    ```bash
    milhoja install -c v1.0.0 <your cookiecutter>
    ```

Show installed template:

    ```bash
    milhoja show
    ```

Install a [Cookiecutter](https://github.com/audreyr/cookiecutter) template on your existing Git repository:

    ```bash
    milhoja -C <your repo path> install <your cookiecutter>
    ```

Upgrade your repository with last version of template:

    ```bash
    milhoja -C <your repo path> upgrade
    ```

## Development

To get set up run:

    ```bash
    python3 -m venv env
    source env/bin/activate

    # Install in editable mode so you get the updates propagated.
    pip install -e .

    # If you want to be able to run tests & linting install via:
    pip install -e ".[dev]"
    ```

Then to actually perform any operations just use the `milhoja` command which should now be on your `$PATH`.

To run tests:

    ```bash
    pytest
    ```

To run linting:

    ```bash
    flake8 --config flake8.cfg milhoja
    ```

## Credits

[Original code](https://github.com/rmedaer/milhoja) written by [Raphael Medaer](https://github.com/rmedaer) from an [original
idea](https://github.com/cookiecutter/cookiecutter/issues/784) of [Abdó Roig-Maranges](https://github.com/aroig).

## License

Free software: Apache Software License 2.0