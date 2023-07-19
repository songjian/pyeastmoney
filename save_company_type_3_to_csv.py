import os
import csv

# 要处理的目录路径
dir_path = 'zcfzb'

# 结果文件的路径
output_path = 'company_type_3_stocks.csv'

# 初始化一个列表来存储结果
results = []

# 遍历目录中的所有文件
for filename in os.listdir(dir_path):
    # 拆分文件名的前两个字符和后面的内容
    prefix = filename[:2]
    remainder = filename[2:-4]  # 去掉文件的后缀.csv
    
    # 把结果保存到列表中
    results.append([prefix, remainder])

# 把结果保存到CSV文件中
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # 写入列名
    writer.writerow(["交易所简码", "股票代码"])
    # 写入文件名数据
    writer.writerows(results)
