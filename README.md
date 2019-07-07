# lovecraft-markov-chain-aws-lambda

A simple Lovecraft-like NLTK-based markov chain text generator as an AWS lambda.

## AWS Lambda

Having heard for some time about AWS lambda I was decided to make some experiment using that technology.

To sum up, AWS lambda allows you to run some function without any kind of server configuration, only specifying the code and its resources.

AWS lambdas are limited both in memory and time and can be accessed in multiple ways. In this example, I accessed to the result by an API Gateway.

## Requirements

- Python 3.7.
- Install a virtualenv with the requirements file.
- Make sure you have an [AWS access key and access secret key](https://docs.aws.amazon.com/en_us/general/latest/gr/managing-aws-access-keys.html). 
- [aws-cli](https://aws.amazon.com/en/cli/) tool.

## Installation

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create an AWS lambda function

I followed [this guide](https://www.fullstackpython.com/blog/aws-lambda-python-3-6.html).

## Updating the AWS lambda code

Note the code is deployed as a zip file, so we must include all libraries, the function, the lovecraft module and
a pickle object with the conditional frequency distribution of the bigrams in the texts of Lovecraft.

```bash
cd venv/lib/python3.7/site-packages/
zip -r9 ../../../../function.zip .
cd ../../../../
zip -g function.zip lambda_function.py
zip -g function.zip lovecraft.py
zip -g function.zip lovecraft_bigram_cfd.pkl
aws lambda update-function-code --function-name Lovecraft --zip-file fileb://function.zip
```

Or just

```bash
./push.sh
```

Note my AWS-lambda function is called Lovecraft and yours could be called with other name.

## Results

Once you have done it, test your aws lambda and will see something like this:

```json
{"text": "Cthulhu was a longer there was mainly from descriptions that"}
```

