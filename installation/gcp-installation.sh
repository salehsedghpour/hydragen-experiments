#!/bin/sh
# It insalls all required packages for running the experiments for the case when we are using GCP

python3.8 -m venv ../venv
source ../venv/bin/activate

echo 'Installing the requirements ... (it may take some minutes)'


if [[ $OSTYPE == 'darwin'* ]]; then
  echo 'You are installing this script on MacOS, the installation may differ a bit ...'
  pip install grpcio --use-pep517 &>/dev/null
fi

pip install -r ./gcp/requirements.txt &>/dev/null
