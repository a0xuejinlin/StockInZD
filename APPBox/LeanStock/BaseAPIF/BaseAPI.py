# 登录
# login()
# 方法说明：登录系统。
# 使用示例：lg = login()
# 返回信息：
# lg.error_code：错误代码，当为“0”时表示成功，当为非0时表示失败；
# lg.error_msg：错误信息，对错误的详细解释。
# 登出
# logout()
# 方法说明：登出系统
# 使用示例：lg = logout()
# 返回信息：
# lg.error_code：错误代码，当为“0”时表示成功，当为非0时表示失败；
# lg.error_msg：错误信息，对错误的详细解释。
# 获取历史A股K线数据
# 获取历史A股K线数据：query_history_k_data_plus()
# 方法说明：通过API接口获取A股历史交易数据，可以通过参数设置获取日k线、周k线、月k线，以及5分钟、15分钟、30分钟和60分钟k线数据，适合搭配均线数据进行选股和分析。
# 返回类型：pandas的DataFrame类型。
# 能获取1990-12-19至当前时间的数据；
# 可查询不复权、前复权、后复权数据。

import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data_plus("sh.600000",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='2017-06-01', end_date='2017-12-31', 
    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
#### 结果集输出到csv文件 ####
result.to_csv("D:/history_k_data.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()