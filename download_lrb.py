import pandas as pd
from eastmoney import f10
import os
import datetime
from utils.date_utils import get_last_days_of_previous_quarters
from tqdm import tqdm

# 读取CSV文件
df = pd.read_csv('tdx_stocks.csv', dtype={'股票代码': str})
today = datetime.date.today()
dates = get_last_days_of_previous_quarters(today.strftime("%Y-%m-%d"), 5)

# 创建保存数据的目录
if not os.path.exists('lrb'):
    os.makedirs('lrb')

# 获取df的行数
total_rows = len(df)

# 循环遍历每行数据
for index, row in tqdm(df.iterrows(), total=total_rows):
    # 拼接得到股票代码
    stock_code = row['交易所简码'] + row['股票代码']

    # 请求利润表数据
    data = f10.lrb(code=stock_code, dates=dates)

    # 将data字段转换为DataFrame并保存为CSV文件，如果文件存在则追加
    try:
        pd.DataFrame(data['data']).to_csv(f'lrb/{stock_code}.csv', index=False, mode='a', header=not os.path.exists(f'lrb/{stock_code}.csv'))
    except KeyError:
        print(f"股票代码{stock_code}的利润表数据不存在")
