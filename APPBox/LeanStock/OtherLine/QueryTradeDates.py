
# 参数含义：

# start_date：开始日期，为空时默认为2015-01-01。
# end_date：结束日期，为空时默认为当前日期。
# 返回示例数据
# calendar_date	is_trading_day
# 2017-01-01	0
# 2017-01-02	0
# 2017-01-03	1
# 返回数据说明
# 参数名称	参数描述
# calendar_date	日期
# is_trading_day	是否交易日(0:非交易日;1:交易日)


import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取交易日信息 ####
rs = bs.query_trade_dates(start_date="2017-01-01", end_date="2017-06-30")
print('query_trade_dates respond error_code:'+rs.error_code)
print('query_trade_dates respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####   
result.to_csv("D:\\trade_datas.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()