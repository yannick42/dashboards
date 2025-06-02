Prerequisites: **python3**

`git config user.name "My Name"`

`git config user.email "johndoe@email.com"`

`git config --list --local`


### Install project locally

#### install Poetry (to manage packages)

`curl -sSL https://install.python-poetry.org | python3 -`

> will be installed in `$HOME/.local/bin`, if necessary add `export PATH=$HOME/.local/bin:$PATH` in your .bashrc file

> to have autocompletion

`poetry completions bash >> ~/.bash_completion`

> to check version

`poetry --version`

#### install all dependencies

`poetry install`

#### Run locally

`poetry run python app.py`

Then go to : http://127.0.0.1:8050

### Deploy to GCP

Automatically deployed to : https://dashboards-828112592242.europe-west9.run.app/
