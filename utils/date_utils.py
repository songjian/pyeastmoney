import pandas as pd

def get_last_days_of_previous_quarters(date: str, n_quarters: int) -> str:
    """
    获取给定日期前n_quarters个季度的最后一天，返回字符串，多个日期用英文逗号分隔
    :param date: 字符串日期，格式为YYYY-MM-DD
    :param n_quarters: 前n_quarters个季度
    :return: 字符串，多个日期用英文逗号分隔
    """
    
    # 将字符串日期转换为Timestamp对象
    date = pd.to_datetime(date)
    # 将日期转换为表示该日期所在季度的Period对象
    period = date.to_period('Q')
    
    last_days = []
    # 获取给定日期前n_quarters个季度的最后一天
    for _ in range(n_quarters+1):
        # 获取季度的最后一天，并格式化为字符串
        last_day = period.end_time.strftime('%Y-%m-%d')
        # 添加到列表
        last_days.append(last_day)
        # 移动到前一个季度
        period = period - 1
        
    # 将日期用英文逗号分隔并返回
    return ','.join(last_days[1:])


# 测试函数
# print(get_last_days_of_previous_quarters('2023-05-25', 5))
