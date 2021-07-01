# singer-gitlab-to-gsheet

## usage

install singer-python:
`pipenv install singer-python`

local run:
`pipenv run python tap-github/tap_repositories.py -c config.json -s state.json | pipenv run python target-gsheet/main.py`
