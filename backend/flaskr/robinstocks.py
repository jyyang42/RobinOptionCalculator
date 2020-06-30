import os
import robin_stocks

from dotenv import load_dotenv

load_dotenv()
username = os.environ['ROBIN_USERNAME']
password = os.environ['ROBIN_PASSWORD']
robin_stocks.login(username,password)
