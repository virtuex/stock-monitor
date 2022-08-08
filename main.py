import requests, json

import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

def add_exchange(shares):
    shares_str = str(shares)
    if (shares_str[:2] == "00") or (shares_str[:3] == "200") or (shares_str[:3] == "300"):
        r_data = "sz" + shares_str
    elif (shares_str[:2] == "60") or (shares_str[:2] == "51") or (shares_str[:3] == "900") or (shares_str[:2] == "68"):
        r_data = "sh" + shares_str
    else:
        r_data = ""
    return r_data


def xueqiu_analysis_return(dat):
    jdat = json.loads(dat)
    rdat = []
    for n in jdat['data']:
        ndic = {}
        ndic['name'] = get_name_by_code(n['symbol'])
        # 股票代码
        ndic['code'] = n['symbol']
        # 现价
        ndic['current'] = n['current']
        # 涨幅百分比
        ndic['percent'] = n['percent']
        # 涨幅
        ndic['chg'] = n['chg']
        # # 最高价
        # ndic['high'] = n['high']
        # # 最低价
        # ndic['low'] = n['low']
        # # 今日开盘
        # ndic['open'] = n['open']
        # # 昨日收盘
        # ndic['last_close'] = n['last_close']
        rdat.append(ndic)
    return rdat


def xueqiu_api(shares_lis):
    he = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62"
    }
    url_parameter = ""
    # 把股票代码拼起来，注意需要大写
    for shares in shares_lis:
        exchange_shares = shares["code"].upper()
        if exchange_shares != "":
            url_parameter = url_parameter + exchange_shares + ","

    # 发送API请求
    url = "https://stock.xueqiu.com/v5/stock/realtime/quotec.json?symbol=" + url_parameter[:-1]
    r = requests.get(url, headers=he)
    r_dat = r.text

    return r_dat


all_stck = [
    {"code": "SH603232", "name": "GERJ"},
    {"code": "SH603603", "name": "ST-BT"},
    {"code": "SZ002411", "name": "ST-bk"},
    {"code": "SH000001", "name": "SZZS"},
]


def get_name_by_code(name):
    for stock in all_stck:
        if stock['code'] == name:
            return stock['name']


def print_pretty(stock):
    print('%s\t%s\t%s\t%s' % (
        str(stock['name']).ljust(12, ' '), str(stock['code']).ljust(12, ' '), str(stock['current']).ljust(12, ' '),
        str(stock['percent']).ljust(12, ' ')))


print('%s\t%s\t%s\t%s' % ("Name".ljust(12, ' '), "Code".ljust(12, ' '), "Current".ljust(12, ' '), "Percent".ljust(12, ' ')))
for n in xueqiu_analysis_return(xueqiu_api(all_stck)):
    print_pretty(n)
