import os
import robin_stocks
import logging
from . import utils
from . import formula
from datetime import date, datetime
from dotenv import load_dotenv


import functools
from werkzeug.exceptions import BadRequest
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

bp = Blueprint('robin', __name__, url_prefix='/robin')
load_dotenv()
username = os.environ['ROBIN_USERNAME']
password = os.environ['ROBIN_PASSWORD']
robin_stocks.login(username, password)
print('Login as ' + username)


@bp.route('/calc', methods=(['POST']))
def calc():
    company = request.form['company']
    expirationDate = request.form['expirationDate']
    optionType = request.form['optionType']
    error = None

    if not company:
        error = 'company is required.'
    elif not expirationDate:
        error = 'expirationDate is required.'
    elif not optionType:
        error = 'optionType is required.'

    if error is None:
        optionData = robin_stocks.options.find_options_by_expiration(
            company, expirationDate=expirationDate, optionType=optionType)

        result = {}
        for item in optionData:
            item = dict(item)
            print(' price -', item['strike_price'], ' exp - ', item['expiration_date'], ' symbol - ',
                  item['chain_symbol'], ' delta - ', item['delta'], ' theta - ', item['theta'])
            p0 = float(item['mark_price'])
            x = float(item['strike_price'])
            t = utils.days_between(datetime.strptime(
                item['expiration_date'], "%Y-%m-%d"), datetime.today())
            
            if (item['implied_volatility'] is not None) and (item['rho'] is not None):
                sigma = float(item['implied_volatility'])
                rho = float(item['rho'])
                d1 = formula.get_d1(p0, x, t, sigma, rho)
                result[p0] = d1

        return {"d1": result}

    raise BadRequest(error)
    

