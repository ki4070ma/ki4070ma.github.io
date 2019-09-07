#!/bin/sh

EXIT_STATUS=0
if ! python -m isort --check-only -rc . ; then
  echo "Please run command 'python -m isort -rc .' on your local and commit the result"
  EXIT_STATUS=1
fi

if ! python -m autopep8 -r --global-config .config-pep8 -i . ; then
  echo "Please run command 'python -m autopep8 -r --global-config .config-pep8 -i .' on your local and commit the result"
  EXIT_STATUS=1
fi

if ! python -m mypy . ; then
  echo "Please check and fix mypy warning"
  EXIT_STATUS=1
fi

(
  python -m pytest --capture=no --verbose --cov . --cov-report=html
)
if [[ $? -ne 0 ]] ; then
  EXIT_STATUS=1
fi

exit $EXIT_STATUS
