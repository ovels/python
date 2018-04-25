# python

# pyenv

## Install:

    $ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

## Update:

    $ pyenv update

## Uninstall:

pyenv is installed within $PYENV_ROOT (default: ~/.pyenv). To uninstall, just remove it:

    $ rm -fr ~/.pyenv

and remove these three lines from .bashrc:

    export PATH="~/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

# pyenv-virtualenv

## Install:

    pip install pyenv-virtualenv

## Create virtualenv:

    `$ pyenv virtualenv [version] [name]`

## Activate virtualenv:

    pyenv activate <name>
    pyenv deactivate

python web demo
python3 + flask + uWSGI + jinja2 + Bootstrap