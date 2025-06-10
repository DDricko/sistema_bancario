#!/bin/bash

python commit_msg_helper.py

if [ $? -ne 0 ]; then
  echo "❌ Falha ao gerar mensagem de commit."
  exit 1
fi

git add .
git commit -F .commitmsg
rm .commitmsg
