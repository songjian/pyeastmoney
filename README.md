# 获取东方财富网数据

## 介绍

本项目是一个获取东方财富网数据的Python库，目前支持的数据有：

- 主要财务指标
- 资产负债表
- 利润表
- 股票实际控制人

## 安装

```shell
pip install pyeastmoney
```

## 使用

### 获得实际控制人

```python
from eastmoney.f10 import shareholder_research

shareholder = shareholder_research(code="SH600161")

print(shareholder)
```
