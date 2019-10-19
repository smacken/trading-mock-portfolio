''' prices tests '''
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from mockportfolio import Prices
# import pandas as pd
import sys
import os
from datetime import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "mockportfolio"))


def test_ctor_prices():
    p = Prices()
    assert p is not None


def test_prev_weekday():
    # sat should become friday
    day = '2019-10-19'
    start_datetime = datetime.strptime(day, "%Y-%m-%d")
    p = Prices()
    weekday = p.prev_weekday(start_datetime)
    assert weekday == datetime.strptime('2019-10-18', "%Y-%m-%d")


def test_prev_weekday_for_weekday():
    # sat should become friday
    day = '2019-10-18'
    start_datetime = datetime.strptime(day, "%Y-%m-%d")
    p = Prices()
    weekday = p.prev_weekday(start_datetime)
    assert weekday == datetime.strptime('2019-10-18', "%Y-%m-%d")
