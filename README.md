# 东方财富网数据

# 例：从Eastmoney获得实际控制人

```python
from eastmoney.eastmoney import F10
a = F10()
b=a.shareholder_research(code="SH600161", date="2022-03-31")
b['sjkzr'][0]['HOLDER_NAME']
```