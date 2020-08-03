# RobinOptionCalculator

Find the best option to buy

## Dependency

- [Robin Stocks](https://robin-stocks.readthedocs.io/en/latest/intro.html) v1.2.1
- [python-dotenv](https://pypi.org/project/python-dotenv/)

## Run the backend

1. create a `.env` file in the workspace and define the environment variables

```
ROBIN_USERNAME=
ROBIN_PASSWORD=
```

2. run the server

For Linux and Mac:
```sh
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
$ flask run
```

For Windows cmd, use set instead of export:

```cmd
> set FLASK_APP=flaskr
> set FLASK_ENV=development
> flask run
```

For Windows PowerShell, use $env: instead of export:
```powershell
> $env:PYTHONPATH=pwd
> $env:FLASK_APP = "flaskr"
> $env:FLASK_ENV = "development"
> flask run
```

3. Test API

Change the expirationDate to a future Friday

```
curl --location --request POST 'http://127.0.0.1:5000/robin/calc' \
--form 'expirationDate=2020-08-14' \
--form 'optionType=call' \
--form 'company=fb'
```
