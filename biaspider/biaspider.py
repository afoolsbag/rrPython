#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bing Image Archive (2009-5-25 – Now) Spider
Src: http://istartedsomething.com/bingimages
"""

from datetime import date as Date, timedelta as TimeDelta
from enum import Enum
# from optparse import OptionParser
from os import path
from pyquery import PyQuery
from time import sleep

import requests

__author__ = 'zhengrr'


class Country(Enum):
    AUSTRALIA = 'au'
    BRAZIL = 'br'
    CANADA = 'ca'
    CHINA = 'cn'
    GERMANY = 'de'
    FRANCE = 'fr'
    JAPAN = 'jp'
    NEW_ZEALAND = 'nz'
    UNITED_KINGDOM = 'gb'
    UNITED_STATES = 'us'


def gen_biaurl(date):
    if not isinstance(date, Date):
        raise TypeError

    return 'http://www.istartedsomething.com/bingimages/?m=%02d&y=%04d' % (date.month, date.year)


def find_biaimg_from_biaurl(biaurl, date, cntry):
    if not isinstance(biaurl, str):
        raise TypeError
    if not isinstance(date, Date):
        raise TypeError
    if not isinstance(cntry, Country):
        raise TypeError

    html = PyQuery(url=biaurl)
    href = '#%04d%02d%02d-%s' % (date.year, date.month, date.day, cntry.value)

    orig = \
        html.find("[href='%s']" % href) \
            .find('.lazy') \
            .attr('data-original')

    if orig is None:
        print("Can not find %s in %04dy%02dm%02dd." % (cntry.value, date.year, date.month, date.day))
        return None

    return orig[13:-6]


def save_img_from_biaimg(biaimg, dir=''):
    if not isinstance(biaimg, str):
        raise TypeError
    if not isinstance(dir, str):
        raise TypeError

    if path.isabs(dir):
        img = path.join(dir, biaimg)
    else:
        img = path.join(path.abspath(path.curdir), dir, biaimg)
    if not path.isabs(img):
        raise TypeError('Invalid directory.')
    url = 'http://www.istartedsomething.com/bingimages/cache/' + biaimg

    with open(img, 'wb') as file:
        response = requests.get(url, stream=True)
        if not response.ok:
            print(response)
            return

        for block in response.iter_content(1024):
            if not block:
                break
            file.write(block)

        print('Succeed.')


def save_img_from_bia(date, cntry, dir=''):
    if not isinstance(date, Date):
        raise TypeError
    if not isinstance(cntry, Country):
        raise TypeError
    if not isinstance(dir, str):
        raise TypeError

    biaurl = gen_biaurl(date)
    if not biaurl:
        return
    biaimg = find_biaimg_from_biaurl(biaurl, date, cntry)
    if not biaimg:
        return
    save_img_from_biaimg(biaimg, dir)


def save_allimg_from_bia(cntry, dir='', *, start=Date(2009, 5, 25), intvl=5.0):
    if not isinstance(cntry, Country):
        raise TypeError
    if not isinstance(dir, str):
        raise TypeError
    if not isinstance(start, Date):
        raise TypeError
    if not isinstance(intvl, float):
        raise TypeError

    date = start
    while date <= Date.today():
        print('Try saving %s %s...' % (date.isoformat(), cntry.value))
        save_img_from_bia(date, cntry, dir)
        sleep(intvl)
        date += TimeDelta(days=1)


if __name__ == '__main__':
    # parser = OptionParser()
    # parser.add_option('-c', '--country', dest='Choose one: ' + ' '.join(e.value for e in Country), default='cn')
    # parser.add_option("-d", "--directory", dest="Image save directory",
    #                   help="write report to FILE", metavar="FILE")
    # parser.add_option("-q", "--quiet",
    #                   action="store_false", dest="verbose", default=True,
    #                   help="don't print status messages to stdout")
    #
    # (options, args) = parser.parse_args()
    save_allimg_from_bia(Country.CHINA, 'bia', start=Date(2014, 9, 14))
