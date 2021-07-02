# singer-gitlab-to-gsheet

## requirements

install singer-python:

`$ pipenv install singer-python`


install gspread and oauth2client lib:

`$ pipenv install google-api-python-client oauth2client`


make sure to set `config.json` file:

| File | Description |
| --- | --- |
| `tap-github/config.json` | Contain configuration to run the github tap script. Can refer [here](https://github.com/firdausraginda/develop-tap-github) to see detail about each items. |
| `target-gsheet/config.json` | Contain configuration to run the gsheet target script. Can refer [here](https://github.com/firdausraginda/develop-target-gsheet) to see detail about each items. |

## usage

to extract **repositories** data and store to spreadsheet:

`$ pipenv run python tap-github/tap_repositories.py -c ./tap-github/config.json -s ./tap-github/state.json | pipenv run python target-gsheet/main.py -c ./target-gsheet/config.json`

to extract **commits** data and store to spreadsheet:

`$ pipenv run python tap-github/tap_commits.py -c ./tap-github/config.json -s ./tap-github/state.json | pipenv run python target-gsheet/main.py -c ./target-gsheet/config.json`

to extract **branches** data and store to spreadsheet:

`$ pipenv run python tap-github/tap_branches.py -c ./tap-github/config.json -s ./tap-github/state.json | pipenv run python target-gsheet/main.py -c ./target-gsheet/config.json`
