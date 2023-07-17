# 参数含义：

# start_date：开始日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空；
# end_date：结束日期，格式XXXX-XX-XX，发布日期在这个范围内，可以为空。
# 返回示例数据
# date	shiborON	shibor1W	shibor2W	shibor1M	shibor3M	shibor6M	shibor9M	shibor1Y
# 2015-01-04	3.640000	4.883000	5.794000	5.629000	5.138000	4.753700	4.624600	4.738500
# 2015-01-05	3.421000	4.725000	5.665000	5.364000	5.125000	4.747800	4.627600	4.742900
# 返回数据说明
# 参数名称	参数描述
# date	日期
# shiborON	隔夜拆借利率
# shibor1W	1周拆放利率
# shibor2W	2周拆放利率
# shibor1M	1个月拆放利率
# shibor3M	3个月拆放利率
# shibor6M	6个月拆放利率
# shibor9M	9个月拆放利率
# shibor1Y	1年拆放利率



import baostock as bs
import pandas as pd

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

# 获取银行间同业拆放利率
rs = bs.query_shibor_data(start_date="2015-01-01", end_date="2015-12-31")
print('query_shibor_data respond error_code:'+rs.error_code)
print('query_shibor_data respond  error_msg:'+rs.error_msg)

# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
# 结果集输出到csv文件
result.to_csv("D:/shibor_data.csv", encoding="gbk", index=False)
print(result)

# 登出系统
bs.logout()