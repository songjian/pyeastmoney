# 获取东方财富网数据

## 例：从Eastmoney获得实际控制人

```python
from eastmoney.f10 import shareholder_research

shareholder = shareholder_research(code="SH600161")

print(shareholder)
```

返回数据
```csv
{
    "gdrs": [
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_TOTAL_NUM": 61733,
            "TOTAL_NUM_RATIO": -10.3747,
            "AVG_FREE_SHARES": 26692,
            "AVG_FREESHARES_RATIO": 11.575656456028,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 24.82,
            "AVG_HOLD_AMT": 662508.427148527,
            "HOLD_RATIO_TOTAL": 60.63434256,
            "FREEHOLD_RATIO_TOTAL": 60.63434256
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2022-12-31 00:00:00",
            "HOLDER_TOTAL_NUM": 68879,
            "TOTAL_NUM_RATIO": 1.4986,
            "AVG_FREE_SHARES": 23923,
            "AVG_FREESHARES_RATIO": -1.4765022721,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 23.73,
            "AVG_HOLD_AMT": 567698.722930647,
            "HOLD_RATIO_TOTAL": 61.45287794,
            "FREEHOLD_RATIO_TOTAL": 61.45287794
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2022-09-30 00:00:00",
            "HOLDER_TOTAL_NUM": 67862,
            "TOTAL_NUM_RATIO": -9.3796,
            "AVG_FREE_SHARES": 24281,
            "AVG_FREESHARES_RATIO": 32.420500427338,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 20.19,
            "AVG_HOLD_AMT": 490248.954823318,
            "HOLD_RATIO_TOTAL": 62.50412989,
            "FREEHOLD_RATIO_TOTAL": 62.50412989
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2022-06-30 00:00:00",
            "HOLDER_TOTAL_NUM": 74886,
            "TOTAL_NUM_RATIO": -2.1303,
            "AVG_FREE_SHARES": 18336,
            "AVG_FREESHARES_RATIO": 2.176641828913,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 20.1520095776,
            "AVG_HOLD_AMT": 369524.717479865,
            "HOLD_RATIO_TOTAL": 61.45040469,
            "FREEHOLD_RATIO_TOTAL": 61.45040469
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2022-03-31 00:00:00",
            "HOLDER_TOTAL_NUM": 76516,
            "TOTAL_NUM_RATIO": -10.7758,
            "AVG_FREE_SHARES": 17946,
            "AVG_FREESHARES_RATIO": 12.077212609128,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 20.4840031456,
            "AVG_HOLD_AMT": 367610.867441033,
            "HOLD_RATIO_TOTAL": 60.37299816,
            "FREEHOLD_RATIO_TOTAL": 60.37299816
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2021-12-31 00:00:00",
            "HOLDER_TOTAL_NUM": 85757,
            "TOTAL_NUM_RATIO": 13.6351,
            "AVG_FREE_SHARES": 16012,
            "AVG_FREESHARES_RATIO": -3.669609564955,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 24.0363343232,
            "AVG_HOLD_AMT": 384879.183393442,
            "HOLD_RATIO_TOTAL": 59.70953607,
            "FREEHOLD_RATIO_TOTAL": 59.70953607
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2021-09-30 00:00:00",
            "HOLDER_TOTAL_NUM": 75467,
            "TOTAL_NUM_RATIO": 12.1952,
            "AVG_FREE_SHARES": 16622,
            "AVG_FREESHARES_RATIO": -10.869651635814,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 26.5677852792,
            "AVG_HOLD_AMT": 441619.476447024,
            "HOLD_RATIO_TOTAL": 60.37727904,
            "FREEHOLD_RATIO_TOTAL": 63.94316895
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2021-06-30 00:00:00",
            "HOLDER_TOTAL_NUM": 67264,
            "TOTAL_NUM_RATIO": 4.9786,
            "AVG_FREE_SHARES": 18649,
            "AVG_FREESHARES_RATIO": -4.742507136061,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 28.42694926,
            "AVG_HOLD_AMT": 530148.474747887,
            "HOLD_RATIO_TOTAL": 62.97293516,
            "FREEHOLD_RATIO_TOTAL": 66.05113948
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2021-03-31 00:00:00",
            "HOLDER_TOTAL_NUM": 64074,
            "TOTAL_NUM_RATIO": 22.6602,
            "AVG_FREE_SHARES": 19577,
            "AVG_FREESHARES_RATIO": -18.473951993008,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 27.0285890488,
            "AVG_HOLD_AMT": 529165.461609696,
            "HOLD_RATIO_TOTAL": 68.01572644,
            "FREEHOLD_RATIO_TOTAL": 68.01572644
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2020-12-31 00:00:00",
            "HOLDER_TOTAL_NUM": 52237,
            "TOTAL_NUM_RATIO": -8.3674,
            "AVG_FREE_SHARES": 24014,
            "AVG_FREESHARES_RATIO": 9.13145854471,
            "HOLD_FOCUS": "非常分散",
            "PRICE": 34.509864156,
            "AVG_HOLD_AMT": 828733.652191164,
            "HOLD_RATIO_TOTAL": 66.73155567,
            "FREEHOLD_RATIO_TOTAL": 66.73155567
        }
    ],
    "sdltgd_date": [
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2023-03-31 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-12-31 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-09-30 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-06-30 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-03-31 00:00:00"
        }
    ],
    "sdgd_date": [
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2023-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2022-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2021-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2021-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2021-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2021-04-23 00:00:00",
            "IS_REPORTDATE": "0"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2021-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2020-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2020-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2020-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2020-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2019-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2019-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2019-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2019-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2018-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2018-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2018-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2018-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-12-27 00:00:00",
            "IS_REPORTDATE": "0"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-10-16 00:00:00",
            "IS_REPORTDATE": "0"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-04-13 00:00:00",
            "IS_REPORTDATE": "0"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2017-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2016-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2016-12-05 00:00:00",
            "IS_REPORTDATE": "0"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2016-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2016-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2016-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2015-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2015-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2015-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2015-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2014-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2014-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2014-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2014-03-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2013-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2013-09-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2013-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2012-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2012-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2011-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2011-06-30 00:00:00",
            "IS_REPORTDATE": "1"
        },
        {
            "SECUCODE": "600161.SH",
            "END_DATE": "2010-12-31 00:00:00",
            "IS_REPORTDATE": "1"
        }
    ],
    "sjkzr": [
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "HOLDER_NAME": "中国医药集团有限公司",
            "HOLD_RATIO": null
        }
    ],
    "jgcc_date": [
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-12-31 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-09-30 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-06-30 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-03-31 00:00:00"
        }
    ],
    "sdgdcgbd": [],
    "jjcg_date": [
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-12-31 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-09-30 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-06-30 00:00:00"
        },
        {
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2022-03-31 00:00:00"
        }
    ],
    "xsjj": [],
    "sdltgd": [
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 1,
            "HOLDER_NAME": "中国生物技术股份有限公司",
            "HOLDER_TYPE": "其它",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 752083740,
            "FREE_HOLDNUM_RATIO": 45.641424124346,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 2,
            "HOLDER_NAME": "成都生物制品研究所有限责任公司",
            "HOLDER_TYPE": "其它",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 58181196,
            "FREE_HOLDNUM_RATIO": 3.530820441215,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 3,
            "HOLDER_NAME": "石雯",
            "HOLDER_TYPE": "个人",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 40829918,
            "FREE_HOLDNUM_RATIO": 2.477829934736,
            "HOLD_NUM_CHANGE": "-953900",
            "CHANGE_RATIO": -2.28294121
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 4,
            "HOLDER_NAME": "乔晓辉",
            "HOLDER_TYPE": "个人",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 35911787,
            "FREE_HOLDNUM_RATIO": 2.179365161558,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 5,
            "HOLDER_NAME": "中国工商银行股份有限公司-中欧医疗健康混合型证券投资基金",
            "HOLDER_TYPE": "证券投资基金",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 27273695,
            "FREE_HOLDNUM_RATIO": 1.655148509038,
            "HOLD_NUM_CHANGE": "-2708314",
            "CHANGE_RATIO": -9.0331305
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 6,
            "HOLDER_NAME": "全国社保基金一一二组合",
            "HOLDER_TYPE": "全国社保基金",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 25585553,
            "FREE_HOLDNUM_RATIO": 1.55270086803,
            "HOLD_NUM_CHANGE": "-4000000",
            "CHANGE_RATIO": -13.52011233
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 7,
            "HOLDER_NAME": "香港中央结算有限公司",
            "HOLDER_TYPE": "其它",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 15937211,
            "FREE_HOLDNUM_RATIO": 0.9671755523,
            "HOLD_NUM_CHANGE": "-2590742",
            "CHANGE_RATIO": -13.98288305
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 8,
            "HOLDER_NAME": "北京生物制品研究所有限责任公司",
            "HOLDER_TYPE": "其它",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 15668638,
            "FREE_HOLDNUM_RATIO": 0.950876763283,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 9,
            "HOLDER_NAME": "中国银行股份有限公司-招商国证生物医药指数分级证券投资基金",
            "HOLDER_TYPE": "证券投资基金",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 14869018,
            "FREE_HOLDNUM_RATIO": 0.90235052396,
            "HOLD_NUM_CHANGE": "-173479",
            "CHANGE_RATIO": -1.15325933
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 10,
            "HOLDER_NAME": "深圳国调招商并购股权投资基金合伙企业(有限合伙)",
            "HOLDER_TYPE": "投资公司",
            "SHARES_TYPE": "A股",
            "HOLD_NUM": 12797724,
            "FREE_HOLDNUM_RATIO": 0.776650681093,
            "HOLD_NUM_CHANGE": "新进",
            "CHANGE_RATIO": null
        }
    ],
    "ltgf": [
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLD_NUM_COUNT": 999138480,
            "LIMITED_SHARES": null,
            "OTHER_UNLIMITED_SHARES": 648671058,
            "HOLD_NUM_RATIO": 60.63,
            "LIMITED_SHARES_RATIO": null,
            "UNLIMITED_SHARES_RATIO": 39.37
        }
    ],
    "sdgd": [
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 1,
            "HOLDER_NAME": "中国生物技术股份有限公司",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 752083740,
            "HOLD_NUM_RATIO": 45.64,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 2,
            "HOLDER_NAME": "成都生物制品研究所有限责任公司",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 58181196,
            "HOLD_NUM_RATIO": 3.53,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 3,
            "HOLDER_NAME": "石雯",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 40829918,
            "HOLD_NUM_RATIO": 2.48,
            "HOLD_NUM_CHANGE": "-953900",
            "CHANGE_RATIO": -2.28294121
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 4,
            "HOLDER_NAME": "乔晓辉",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 35911787,
            "HOLD_NUM_RATIO": 2.18,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 5,
            "HOLDER_NAME": "中国工商银行股份有限公司-中欧医疗健康混合型证券投资基金",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 27273695,
            "HOLD_NUM_RATIO": 1.66,
            "HOLD_NUM_CHANGE": "-2708314",
            "CHANGE_RATIO": -9.0331305
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 6,
            "HOLDER_NAME": "全国社保基金一一二组合",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 25585553,
            "HOLD_NUM_RATIO": 1.55,
            "HOLD_NUM_CHANGE": "-4000000",
            "CHANGE_RATIO": -13.52011233
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 7,
            "HOLDER_NAME": "香港中央结算有限公司",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 15937211,
            "HOLD_NUM_RATIO": 0.97,
            "HOLD_NUM_CHANGE": "-2590742",
            "CHANGE_RATIO": -13.98288305
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 8,
            "HOLDER_NAME": "北京生物制品研究所有限责任公司",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 15668638,
            "HOLD_NUM_RATIO": 0.95,
            "HOLD_NUM_CHANGE": "不变",
            "CHANGE_RATIO": null
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 9,
            "HOLDER_NAME": "中国银行股份有限公司-招商国证生物医药指数分级证券投资基金",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 14869018,
            "HOLD_NUM_RATIO": 0.9,
            "HOLD_NUM_CHANGE": "-173479",
            "CHANGE_RATIO": -1.15325933
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "END_DATE": "2023-03-31 00:00:00",
            "HOLDER_RANK": 10,
            "HOLDER_NAME": "深圳国调招商并购股权投资基金合伙企业(有限合伙)",
            "SHARES_TYPE": "流通A股",
            "HOLD_NUM": 12797724,
            "HOLD_NUM_RATIO": 0.78,
            "HOLD_NUM_CHANGE": "新进",
            "CHANGE_RATIO": null
        }
    ],
    "jgcc": [
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "ORG_TYPE": "00",
            "TOTAL_ORG_NUM": 48,
            "TOTAL_FREE_SHARES": 947900072,
            "TOTAL_SHARES_RATIO": 57.5248565,
            "ALL_SHARES_RATIO": 57.5248565
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "ORG_TYPE": "01",
            "TOTAL_ORG_NUM": 40,
            "TOTAL_FREE_SHARES": 67323479,
            "TOTAL_SHARES_RATIO": 4.08563476,
            "ALL_SHARES_RATIO": 4.08563476
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "ORG_TYPE": "03",
            "TOTAL_ORG_NUM": 1,
            "TOTAL_FREE_SHARES": 25585553,
            "TOTAL_SHARES_RATIO": 1.55270087,
            "ALL_SHARES_RATIO": 1.55270087
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "ORG_TYPE": "04",
            "TOTAL_ORG_NUM": 2,
            "TOTAL_FREE_SHARES": 322531,
            "TOTAL_SHARES_RATIO": 0.01957332,
            "ALL_SHARES_RATIO": 0.01957332
        },
        {
            "SECUCODE": "600161.SH",
            "SECURITY_CODE": "600161",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "ORG_TYPE": "07",
            "TOTAL_ORG_NUM": 5,
            "TOTAL_FREE_SHARES": 854668509,
            "TOTAL_SHARES_RATIO": 51.86694755,
            "ALL_SHARES_RATIO": 51.86694755
        }
    ],
    "jjcg": [
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "003095",
            "HOLDER_NAME": "中欧医疗健康混合A",
            "TOTAL_SHARES": 27273695,
            "HOLD_VALUE": 676933109.9,
            "TOTALSHARES_RATIO": 1.65514851,
            "FREESHARES_RATIO": 1.65514851,
            "FREE_MARKET_CAP": 676933109.9,
            "FREE_SHARES": 27273695,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "003095",
            "FUND_DERIVECODE": "003095.OF",
            "NETVALUE_RATIO": 2.42
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "161726",
            "HOLDER_NAME": "招商国证生物医药指数(LOF)A",
            "TOTAL_SHARES": 14869018,
            "HOLD_VALUE": 369049026.76,
            "TOTALSHARES_RATIO": 0.90235052,
            "FREESHARES_RATIO": 0.90235052,
            "FREE_MARKET_CAP": 369049026.76,
            "FREE_SHARES": 14869018,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "161726",
            "FUND_DERIVECODE": "161726.SZ",
            "NETVALUE_RATIO": 3.21
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "009630",
            "HOLDER_NAME": "浦银安盛ESG责任投资混合A",
            "TOTAL_SHARES": 4920000,
            "HOLD_VALUE": 122114400,
            "TOTALSHARES_RATIO": 0.2985782,
            "FREESHARES_RATIO": 0.2985782,
            "FREE_MARKET_CAP": 122114400,
            "FREE_SHARES": 4920000,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "009630",
            "FUND_DERIVECODE": "009630.OF",
            "NETVALUE_RATIO": 8.94
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "011338",
            "HOLDER_NAME": "兴全合远两年持有混合A",
            "TOTAL_SHARES": 4919261,
            "HOLD_VALUE": 122096058.02,
            "TOTALSHARES_RATIO": 0.29853335,
            "FREESHARES_RATIO": 0.29853335,
            "FREE_MARKET_CAP": 122096058.02,
            "FREE_SHARES": 4919261,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "011338",
            "FUND_DERIVECODE": "011338.OF",
            "NETVALUE_RATIO": 3.57
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "340006",
            "HOLDER_NAME": "兴全全球视野股票",
            "TOTAL_SHARES": 3324103,
            "HOLD_VALUE": 82504236.46,
            "TOTALSHARES_RATIO": 0.20172859,
            "FREESHARES_RATIO": 0.20172859,
            "FREE_MARKET_CAP": 82504236.46,
            "FREE_SHARES": 3324103,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "340006",
            "FUND_DERIVECODE": "340006.OF",
            "NETVALUE_RATIO": 4.26
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "001417",
            "HOLDER_NAME": "汇添富医疗服务混合A",
            "TOTAL_SHARES": 3132440,
            "HOLD_VALUE": 77747160.8,
            "TOTALSHARES_RATIO": 0.19009721,
            "FREESHARES_RATIO": 0.19009721,
            "FREE_MARKET_CAP": 77747160.8,
            "FREE_SHARES": 3132440,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "001417",
            "FUND_DERIVECODE": "001417.OF",
            "NETVALUE_RATIO": 2.69
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "007066",
            "HOLDER_NAME": "浦银安盛先进制造混合A",
            "TOTAL_SHARES": 1346400,
            "HOLD_VALUE": 33417648,
            "TOTALSHARES_RATIO": 0.08170847,
            "FREESHARES_RATIO": 0.08170847,
            "FREE_MARKET_CAP": 33417648,
            "FREE_SHARES": 1346400,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "007066",
            "FUND_DERIVECODE": "007066.OF",
            "NETVALUE_RATIO": 8.91
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "010673",
            "HOLDER_NAME": "兴全中证800六个月持有指数A",
            "TOTAL_SHARES": 1182480,
            "HOLD_VALUE": 29349153.6,
            "TOTALSHARES_RATIO": 0.07176072,
            "FREESHARES_RATIO": 0.07176072,
            "FREE_MARKET_CAP": 29349153.6,
            "FREE_SHARES": 1182480,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "010673",
            "FUND_DERIVECODE": "010673.OF",
            "NETVALUE_RATIO": 2.03
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "009468",
            "HOLDER_NAME": "博时健康成长双周定期可赎回混合A",
            "TOTAL_SHARES": 1110280,
            "HOLD_VALUE": 27557149.6,
            "TOTALSHARES_RATIO": 0.06737915,
            "FREESHARES_RATIO": 0.06737915,
            "FREE_MARKET_CAP": 27557149.6,
            "FREE_SHARES": 1110280,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "009468",
            "FUND_DERIVECODE": "009468.OF",
            "NETVALUE_RATIO": 3.46
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "160211",
            "HOLDER_NAME": "国泰中小盘成长混合(LOF)",
            "TOTAL_SHARES": 843119,
            "HOLD_VALUE": 20926213.58,
            "TOTALSHARES_RATIO": 0.05116605,
            "FREESHARES_RATIO": 0.05116605,
            "FREE_MARKET_CAP": 20926213.58,
            "FREE_SHARES": 843119,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "160211",
            "FUND_DERIVECODE": "160211.SZ",
            "NETVALUE_RATIO": 3.01
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "015663",
            "HOLDER_NAME": "易米开鑫价值优选混合A",
            "TOTAL_SHARES": 750000,
            "HOLD_VALUE": 18615000,
            "TOTALSHARES_RATIO": 0.04551497,
            "FREESHARES_RATIO": 0.04551497,
            "FREE_MARKET_CAP": 18615000,
            "FREE_SHARES": 750000,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "015663",
            "FUND_DERIVECODE": "015663.OF",
            "NETVALUE_RATIO": 7.83
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "012202",
            "HOLDER_NAME": "中加消费优选混合A",
            "TOTAL_SHARES": 651351,
            "HOLD_VALUE": 16166531.82,
            "TOTALSHARES_RATIO": 0.03952829,
            "FREESHARES_RATIO": 0.03952829,
            "FREE_MARKET_CAP": 16166531.82,
            "FREE_SHARES": 651351,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "012202",
            "FUND_DERIVECODE": "012202.OF",
            "NETVALUE_RATIO": 4.1
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "003581",
            "HOLDER_NAME": "新疆前海联合国民健康混合A",
            "TOTAL_SHARES": 523192,
            "HOLD_VALUE": 12985625.44,
            "TOTALSHARES_RATIO": 0.03175076,
            "FREESHARES_RATIO": 0.03175076,
            "FREE_MARKET_CAP": 12985625.44,
            "FREE_SHARES": 523192,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "003581",
            "FUND_DERIVECODE": "003581.OF",
            "NETVALUE_RATIO": 8.32
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "011977",
            "HOLDER_NAME": "格林研究优选混合A",
            "TOTAL_SHARES": 407340,
            "HOLD_VALUE": 10110178.8,
            "TOTALSHARES_RATIO": 0.02472009,
            "FREESHARES_RATIO": 0.02472009,
            "FREE_MARKET_CAP": 10110178.8,
            "FREE_SHARES": 407340,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "011977",
            "FUND_DERIVECODE": "011977.OF",
            "NETVALUE_RATIO": 4.43
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "015139",
            "HOLDER_NAME": "泰康医疗健康股票发起A",
            "TOTAL_SHARES": 329100,
            "HOLD_VALUE": 8168262,
            "TOTALSHARES_RATIO": 0.01997197,
            "FREESHARES_RATIO": 0.01997197,
            "FREE_MARKET_CAP": 8168262,
            "FREE_SHARES": 329100,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "015139",
            "FUND_DERIVECODE": "015139.OF",
            "NETVALUE_RATIO": 3.06
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "050018",
            "HOLDER_NAME": "博时行业轮动混合",
            "TOTAL_SHARES": 279800,
            "HOLD_VALUE": 6944636,
            "TOTALSHARES_RATIO": 0.01698012,
            "FREESHARES_RATIO": 0.01698012,
            "FREE_MARKET_CAP": 6944636,
            "FREE_SHARES": 279800,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "050018",
            "FUND_DERIVECODE": "050018.OF",
            "NETVALUE_RATIO": 3.04
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "014157",
            "HOLDER_NAME": "国泰君安创新医药混合发起",
            "TOTAL_SHARES": 217520,
            "HOLD_VALUE": 5398846.4,
            "TOTALSHARES_RATIO": 0.01320055,
            "FREESHARES_RATIO": 0.01320055,
            "FREE_MARKET_CAP": 5398846.4,
            "FREE_SHARES": 217520,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "014157",
            "FUND_DERIVECODE": "014157.OF",
            "NETVALUE_RATIO": 2.85
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "015959",
            "HOLDER_NAME": "太平嘉和三个月定开债券发起式",
            "TOTAL_SHARES": 197700,
            "HOLD_VALUE": 4906914,
            "TOTALSHARES_RATIO": 0.01199775,
            "FREESHARES_RATIO": 0.01199775,
            "FREE_MARKET_CAP": 4906914,
            "FREE_SHARES": 197700,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "015959",
            "FUND_DERIVECODE": "015959.OF",
            "NETVALUE_RATIO": 0.17
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "012027",
            "HOLDER_NAME": "光大安阳一年持有期混合A",
            "TOTAL_SHARES": 150000,
            "HOLD_VALUE": 3723000,
            "TOTALSHARES_RATIO": 0.00910299,
            "FREESHARES_RATIO": 0.00910299,
            "FREE_MARKET_CAP": 3723000,
            "FREE_SHARES": 150000,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "012027",
            "FUND_DERIVECODE": "012027.OF",
            "NETVALUE_RATIO": 0.75
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "005041",
            "HOLDER_NAME": "人保精选A",
            "TOTAL_SHARES": 126200,
            "HOLD_VALUE": 3132284,
            "TOTALSHARES_RATIO": 0.00765865,
            "FREESHARES_RATIO": 0.00765865,
            "FREE_MARKET_CAP": 3132284,
            "FREE_SHARES": 126200,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "005041",
            "FUND_DERIVECODE": "005041.OF",
            "NETVALUE_RATIO": 2.63
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "015276",
            "HOLDER_NAME": "博时均衡回报混合A",
            "TOTAL_SHARES": 81600,
            "HOLD_VALUE": 2025312,
            "TOTALSHARES_RATIO": 0.00495203,
            "FREESHARES_RATIO": 0.00495203,
            "FREE_MARKET_CAP": 2025312,
            "FREE_SHARES": 81600,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "015276",
            "FUND_DERIVECODE": "015276.OF",
            "NETVALUE_RATIO": 2.09
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "010665",
            "HOLDER_NAME": "博时高端装备混合A",
            "TOTAL_SHARES": 78500,
            "HOLD_VALUE": 1948370,
            "TOTALSHARES_RATIO": 0.0047639,
            "FREESHARES_RATIO": 0.0047639,
            "FREE_MARKET_CAP": 1948370,
            "FREE_SHARES": 78500,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "010665",
            "FUND_DERIVECODE": "010665.OF",
            "NETVALUE_RATIO": 3.01
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "009967",
            "HOLDER_NAME": "博时荣泰混合",
            "TOTAL_SHARES": 78400,
            "HOLD_VALUE": 1945888,
            "TOTALSHARES_RATIO": 0.00475783,
            "FREESHARES_RATIO": 0.00475783,
            "FREE_MARKET_CAP": 1945888,
            "FREE_SHARES": 78400,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "009967",
            "FUND_DERIVECODE": "009967.OF",
            "NETVALUE_RATIO": 2.08
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "164401",
            "HOLDER_NAME": "前海开源中证健康产业指数",
            "TOTAL_SHARES": 65660,
            "HOLD_VALUE": 1629681.2,
            "TOTALSHARES_RATIO": 0.00398468,
            "FREESHARES_RATIO": 0.00398468,
            "FREE_MARKET_CAP": 1629681.2,
            "FREE_SHARES": 65660,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "164401",
            "FUND_DERIVECODE": "164401.OF",
            "NETVALUE_RATIO": 1.1
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "002595",
            "HOLDER_NAME": "博时工业4.0主题股票",
            "TOTAL_SHARES": 63600,
            "HOLD_VALUE": 1578552,
            "TOTALSHARES_RATIO": 0.00385967,
            "FREESHARES_RATIO": 0.00385967,
            "FREE_MARKET_CAP": 1578552,
            "FREE_SHARES": 63600,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "002595",
            "FUND_DERIVECODE": "002595.OF",
            "NETVALUE_RATIO": 3.05
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "012430",
            "HOLDER_NAME": "农银瑞康6个月持有混合",
            "TOTAL_SHARES": 60000,
            "HOLD_VALUE": 1489200,
            "TOTALSHARES_RATIO": 0.0036412,
            "FREESHARES_RATIO": 0.0036412,
            "FREE_MARKET_CAP": 1489200,
            "FREE_SHARES": 60000,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "012430",
            "FUND_DERIVECODE": "012430.OF",
            "NETVALUE_RATIO": 1.64
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "014285",
            "HOLDER_NAME": "鑫元健康产业混合发起式A",
            "TOTAL_SHARES": 55300,
            "HOLD_VALUE": 1372546,
            "TOTALSHARES_RATIO": 0.00335597,
            "FREESHARES_RATIO": 0.00335597,
            "FREE_MARKET_CAP": 1372546,
            "FREE_SHARES": 55300,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "014285",
            "FUND_DERIVECODE": "014285.OF",
            "NETVALUE_RATIO": 5.49
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "003754",
            "HOLDER_NAME": "国泰普益灵活配置混合A",
            "TOTAL_SHARES": 52500,
            "HOLD_VALUE": 1303050,
            "TOTALSHARES_RATIO": 0.00318605,
            "FREESHARES_RATIO": 0.00318605,
            "FREE_MARKET_CAP": 1303050,
            "FREE_SHARES": 52500,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "003754",
            "FUND_DERIVECODE": "003754.OF",
            "NETVALUE_RATIO": 0.71
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "016756",
            "HOLDER_NAME": "中加医疗创新混合发起式A",
            "TOTAL_SHARES": 37460,
            "HOLD_VALUE": 929757.2,
            "TOTALSHARES_RATIO": 0.00227332,
            "FREESHARES_RATIO": 0.00227332,
            "FREE_MARKET_CAP": 929757.2,
            "FREE_SHARES": 37460,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "016756",
            "FUND_DERIVECODE": "016756.OF",
            "NETVALUE_RATIO": 5.95
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "001265",
            "HOLDER_NAME": "国泰兴益灵活配置混合A",
            "TOTAL_SHARES": 34100,
            "HOLD_VALUE": 846362,
            "TOTALSHARES_RATIO": 0.00206941,
            "FREESHARES_RATIO": 0.00206941,
            "FREE_MARKET_CAP": 846362,
            "FREE_SHARES": 34100,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "001265",
            "FUND_DERIVECODE": "001265.OF",
            "NETVALUE_RATIO": 0.73
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "010545",
            "HOLDER_NAME": "中加聚隆持有期混合A",
            "TOTAL_SHARES": 29200,
            "HOLD_VALUE": 724744,
            "TOTALSHARES_RATIO": 0.00177205,
            "FREESHARES_RATIO": 0.00177205,
            "FREE_MARKET_CAP": 724744,
            "FREE_SHARES": 29200,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "010545",
            "FUND_DERIVECODE": "010545.OF",
            "NETVALUE_RATIO": 0.97
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "015371",
            "HOLDER_NAME": "中加聚享增盈债券A",
            "TOTAL_SHARES": 25600,
            "HOLD_VALUE": 635392,
            "TOTALSHARES_RATIO": 0.00155358,
            "FREESHARES_RATIO": 0.00155358,
            "FREE_MARKET_CAP": 635392,
            "FREE_SHARES": 25600,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "015371",
            "FUND_DERIVECODE": "015371.OF",
            "NETVALUE_RATIO": 1.1
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "002388",
            "HOLDER_NAME": "天弘裕利灵活配置混合A",
            "TOTAL_SHARES": 25600,
            "HOLD_VALUE": 635392,
            "TOTALSHARES_RATIO": 0.00155358,
            "FREESHARES_RATIO": 0.00155358,
            "FREE_MARKET_CAP": 635392,
            "FREE_SHARES": 25600,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "002388",
            "FUND_DERIVECODE": "002388.OF",
            "NETVALUE_RATIO": 1.23
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "001922",
            "HOLDER_NAME": "国泰多策略收益灵活配置混合",
            "TOTAL_SHARES": 23200,
            "HOLD_VALUE": 575824,
            "TOTALSHARES_RATIO": 0.00140793,
            "FREESHARES_RATIO": 0.00140793,
            "FREE_MARKET_CAP": 575824,
            "FREE_SHARES": 23200,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "001922",
            "FUND_DERIVECODE": "001922.OF",
            "NETVALUE_RATIO": 0.61
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "002197",
            "HOLDER_NAME": "国泰鑫策略价值灵活配置混合",
            "TOTAL_SHARES": 14500,
            "HOLD_VALUE": 359890,
            "TOTALSHARES_RATIO": 0.00087996,
            "FREESHARES_RATIO": 0.00087996,
            "FREE_MARKET_CAP": 359890,
            "FREE_SHARES": 14500,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "002197",
            "FUND_DERIVECODE": "002197.OF",
            "NETVALUE_RATIO": 0.71
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "014327",
            "HOLDER_NAME": "格林新兴产业混合A",
            "TOTAL_SHARES": 14400,
            "HOLD_VALUE": 357408,
            "TOTALSHARES_RATIO": 0.00087389,
            "FREESHARES_RATIO": 0.00087389,
            "FREE_MARKET_CAP": 357408,
            "FREE_SHARES": 14400,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "014327",
            "FUND_DERIVECODE": "014327.OF",
            "NETVALUE_RATIO": 3.5
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "970073",
            "HOLDER_NAME": "东证融汇成长优选混合A",
            "TOTAL_SHARES": 10800,
            "HOLD_VALUE": 268056,
            "TOTALSHARES_RATIO": 0.00065542,
            "FREESHARES_RATIO": 0.00065542,
            "FREE_MARKET_CAP": 268056,
            "FREE_SHARES": 10800,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "970073",
            "FUND_DERIVECODE": "970073.OF",
            "NETVALUE_RATIO": 0.44
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "017190",
            "HOLDER_NAME": "鑫元中证1000指数增强发起式A",
            "TOTAL_SHARES": 10000,
            "HOLD_VALUE": 248200,
            "TOTALSHARES_RATIO": 0.00060687,
            "FREESHARES_RATIO": 0.00060687,
            "FREE_MARKET_CAP": 248200,
            "FREE_SHARES": 10000,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "017190",
            "FUND_DERIVECODE": "017190.OF",
            "NETVALUE_RATIO": 0.61
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "008524",
            "HOLDER_NAME": "华泰柏瑞锦瑞债券A",
            "TOTAL_SHARES": 10000,
            "HOLD_VALUE": 248200,
            "TOTALSHARES_RATIO": 0.00060687,
            "FREESHARES_RATIO": 0.00060687,
            "FREE_MARKET_CAP": 248200,
            "FREE_SHARES": 10000,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "008524",
            "FUND_DERIVECODE": "008524.OF",
            "NETVALUE_RATIO": 0.49
        },
        {
            "ORG_TYPE": "01",
            "SECUCODE": "600161.SH",
            "REPORT_DATE": "2023-03-31 00:00:00",
            "HOLDER_CODE": "015278",
            "HOLDER_NAME": "东财沪深300指数发起式A",
            "TOTAL_SHARES": 60,
            "HOLD_VALUE": 1489.2,
            "TOTALSHARES_RATIO": 3.64e-06,
            "FREESHARES_RATIO": 3.64e-06,
            "FREE_MARKET_CAP": 1489.2,
            "FREE_SHARES": 60,
            "SECURITY_CODE": "600161",
            "FUND_CODE": "015278",
            "FUND_DERIVECODE": "015278.OF",
            "NETVALUE_RATIO": 0.01
        }
    ]
}
```