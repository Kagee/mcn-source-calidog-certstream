#! /bin/bash
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SOURCE_DIR" || exit
source config.sh

if [ ! -d "./certstream-python" ]; then
  git clone https://github.com/CaliDog/certstream-python.git
else
  cd "./certstream-python"
  git pull
  cd ..
fi
