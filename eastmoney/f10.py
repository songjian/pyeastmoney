import requests
import json
import datetime


def shareholder_research(code, date=None) -> dict:
    """股东研究

    Keyword arguments:
    code -- 股票代码，例如: SH603288
    date -- 日期，例如: 2022-03-31

    Returns:
    gdrs -- 股东人数
    sdltgd_date -- 十大流通股东变动日期
    sdgd_date -- 十大股东变动日期
    sjkzr -- 实际控制人
    jgcc_date -- 机构持仓变动日期
    sdgdcgbd -- 十大股东持股变动
    jjcg_date -- 基金持股变动日期
    xsjj -- 新进基金
    sdltgd -- 十大流通股东
    ltgf -- 流通股份
    sdgd -- 十大股东
    jgcc -- 机构持股
    jjcg -- 基金持股
    """

    if date is None:
        date = datetime.date.today().strftime('%Y-%m-%d')

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

    params = {
        'code': code,
        'date': date
    }


    url='http://emweb.securities.eastmoney.com/PC_HSF10/ShareholderResearch/PageAjax'
    r=requests.get(url, params=params, headers=headers)
    return json.loads(r.text)

