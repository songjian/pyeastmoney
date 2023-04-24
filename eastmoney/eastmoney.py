import time
import math
import random
import json
import re
import requests

headers={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'datainterface.eastmoney.com',
    'Referer': 'https://data.eastmoney.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
    'Cookie': 'qgqp_b_id=106c8aa68fedc92e8732f6d403c9c344; HAList=ty-1-601857-%u4E2D%u56FD%u77F3%u6CB9%2Cty-1-603288-%u6D77%u5929%u5473%u4E1A%2Cty-1-600004-%u767D%u4E91%u673A%u573A%2Cty-1-600161-%u5929%u575B%u751F%u7269%2Cty-1-600519-%u8D35%u5DDE%u8305%u53F0%2Cty-1-601318-%u4E2D%u56FD%u5E73%u5B89; st_si=58447156941825; st_sn=39; st_psi=20230317233731581-113200301201-5506637370; st_asi=delete; Hm_lvt_f5b8577eb864c9edb45975f456f5dc27=1679044665; Hm_lpvt_f5b8577eb864c9edb45975f456f5dc27=1679067508; st_pvi=69032368480463; st_sp=2023-03-08%2010%3A51%3A10; st_inirUrl=https%3A%2F%2Fwww.google.com%2F'
}

class Eastmoney:

    def _loads_jsonp(self, _jsonp):
        try:
            return json.loads(re.match(".*?\((.*)\).*", _jsonp, re.S).group(1))
        except:
            raise ValueError('Invalid Input')

    def _js(self, **data):
        url='https://datainterface.eastmoney.com/EM_DataCenter/JS.aspx'
        data['cb']='jQuery' + \
            str(math.floor(1e10 * random.random())) + \
            '_' + str(int(round(time.time() * 1000)))
        data['_'] = str(int(round(time.time() * 1000)))
        data['type'] = 'GJZB'
        data['js'] = '([(x)])'
        data['p'] = '1'
        data['ps'] = '200'
        r = requests.get(url, params=data, headers=headers)
        return self._loads_jsonp(r.text)

    def hg(self, *, stat=None, mkt=None, sty='HKZB'):
        """宏观数据
        """
        data=_js(stat=stat, mkt=mkt, sty=sty)
        for i in data:
            print(i)


class F10:
    def shareholder_research(self, **data) -> dict:
        """股东研究

        Keyword arguments:
        code -- 股票代码，例如: SH603288
        date -- 日期，例如: 2022-03-31

        Returns:
        sjkzr -- 实际控制人
        jjcg -- 基金持股
        jgcc_date -- 机构持仓
        sdgd_date -- 十大股东
        sdltgd_date -- 十大流通股东
        gdrs -- 股东人数
        sdgdcgbd -- 十大股东持股变动
        """
        headers = {
            'Host': 'emweb.securities.eastmoney.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referer': 'http://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/Index?type=web&code=sh603288',
            'Cookie': 'qgqp_b_id=106c8aa68fedc92e8732f6d403c9c344; HAList=ty-1-601857-%u4E2D%u56FD%u77F3%u6CB9%2Cty-1-603288-%u6D77%u5929%u5473%u4E1A%2Cty-1-600004-%u767D%u4E91%u673A%u573A%2Cty-1-600161-%u5929%u575B%u751F%u7269%2Cty-1-600519-%u8D35%u5DDE%u8305%u53F0%2Cty-1-601318-%u4E2D%u56FD%u5E73%u5B89; st_si=58447156941825; st_sn=39; st_psi=20230317233731581-113200301201-5506637370; st_asi=delete; Hm_lvt_f5b8577eb864c9edb45975f456f5dc27=1679044665; Hm_lpvt_f5b8577eb864c9edb45975f456f5dc27=1679067508; st_pvi=69032368480463; st_sp=2023-03-08%2010%3A51%3A10; st_inirUrl=https%3A%2F%2Fwww.google.com%2F',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
        }

        url='http://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/PageAjax'
        r=requests.get(url, params=data, headers=headers)
        return json.loads(r.text)
