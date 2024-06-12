# SAP Password bot

This robot is used to change the passwords of multiple SAP users in OpenOrchestrator.

The robot expects a list of credential names in the arguments separated by commas.
Note that any surrounding white space is stripped from the credential names.


## Linting and Github Actions

This template is also setup with flake8 and pylint linting in Github Actions.
This workflow will trigger whenever you push your code to Github.
The workflow is defined under `.github/workflows/Linting.yml`.

