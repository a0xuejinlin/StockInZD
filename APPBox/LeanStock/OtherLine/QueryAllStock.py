# 参数含义：

# day：需要查询的交易日期，为空时默认当前日期。
# 返回示例数据
# code	tradeStatus	code_name
# sh.000001	1	上证综合指数
# sh.000002	1	上证A股指数
# sh.000003	1	上证B股指数
# 返回数据说明
# 参数名称	参数描述
# code	证券代码
# tradeStatus	交易状态(1：正常交易 0：停牌）
# code_name	证券名称


import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取证券信息 ####
rs = bs.query_all_stock(day="2017-06-30")
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####   
result.to_csv("D:\\all_stock.csv", encoding="gbk", index=False)
print(result)

#### 登出系统 ####
bs.logout()