#!/bin/bash

cd venv/lib/python3.7/site-packages/
zip -r9 ../../../../function.zip .
cd ../../../../
zip -g function.zip lambda_function.py
zip -g function.zip lovecraft.py
zip -g function.zip lovecraft_bigram_cfd.pkl
aws lambda update-function-code --function-name Lovecraft --zip-file fileb://function.zip
