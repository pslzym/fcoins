#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fcoin
#from fcoin.dataapi import DataAPI
import json
import sys
import time

def get_ft_price(api):
    prices = api.get_ticker("fteth")
    return prices["data"]["ticker"][0]

def buy_ft(api, price):
    try:
        res = api.buy("fteth", price, 5)
        if res["status"] == 0:
            return True
        else:
            return False
    except:
        print "buy ft failed"

def get_eth_balance(api):
    balance = api.get_balance()
    if balance.has_key("data"):
        for i in balance["data"]:
            if i["currency"] == "eth":
                return i["balance"]
    else:
        return 0

def get_ft_balance(api):
    balance = api.get_balance()
    if balance.has_key("data"):
        for i in balance["data"]:
            if i["currency"] == "ft":
                return i["balance"]
    else:
        return 0

def sell_ft(api, price):
    try:
        res = api.sell("fteth", price, 5)
        if res["status"] == 0:
            return True
        else:
            return False
    except:
        print "sell_ft failed"


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "python fcoin.py api.key api.secret number"
        sys.exit(-1)
    api = fcoin.authorize(sys.argv[1],sys.argv[2])
    #api = DataAPI(sys.argv[1],sys.argv[2])
    ft_price = get_ft_price(api)

    for i in range(1, int(sys.argv[3])):
        ft_price = get_ft_price(api)
        eth_balance = get_eth_balance(api)

        print "----start buy ft coins----"
        print "eth of balance : ", eth_balance
        print "ft price : ", ft_price
        if float(ft_price) * 5 < eth_balance:
            print "buy 5 ft coins."
            buy_ft(api, ft_price)
        else:
            print "eth coins is not enough."
            continue

        time.sleep(5)

        print "----start sell ft coins----"
        ft_price = get_ft_price(api)
        ft_count = get_ft_balance(api)
        if ft_count > 5:
            print "sell 5 ft coins."
            sell_ft(api, ft_price)
        else:
            print "ft coins is not enough."
            continue
