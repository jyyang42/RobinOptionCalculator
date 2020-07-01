import os
import robin_stocks

from dotenv import load_dotenv

load_dotenv()
username = os.environ['ROBIN_USERNAME']
password = os.environ['ROBIN_PASSWORD']
robin_stocks.login(username,password)
optionData = robin_stocks.options.find_options_by_expiration('fb', expirationDate='2020-07-17',optionType='call')
for item in optionData:
    item = dict(item)
    print(' price -',item['strike_price'],' exp - ',item['expiration_date'],' symbol - ', item['chain_symbol'],' delta - ',item['delta'],' theta - ',item['theta'])