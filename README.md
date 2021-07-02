# singer-gitlab-to-gsheet

## usage

install singer-python:
`$ pipenv install singer-python`

install gspread and oauth2client lib:
`$ pipenv install google-api-python-client oauth2client`

local run:
`$ pipenv run python tap-github/tap_repositories.py -c ./tap-github/config.json -s ./tap-github/state.json | pipenv run python target-gsheet/main.py -c ./target-gsheet/config.json`
