import baostock as bs
import pandas as pd

### 基础设定 ###
#获取数据存储的所在盘符地址
DownloadData="D:/testbaostock/history_k_data1.csv"

###登录系统###
lg=bs.login()
#线上登录返回信息
print('login respond error_code:'+lg.error_code)
print('login respond error_msg:'+lg.error_code)

###获取历史K线数据###
#详细指标数据，参见“历史行情指标参数”章节
rs=bs.query_history_k_data_plus("sz.000652","date,time,code,open,high,low,close,volume,amount,adjustflag",start_date='2023-07-06',end_date='2023-07-11',frequency="5",adjustflag="3")

#frequency="d"取日K线，adjustflag="3"默认不复权
print('query_history_k_data_plus respond error_code:'+ rs.error_code)
print('query_history_k_data_plus respond error_msg:'+ rs.error_msg)
###打印结果集###
data_list =[]
while(rs.error_code =='0')& rs.next():
    #获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result=pd.DataFrame(data_list,columns=rs.fields)
####结果集输出到csv文件###
result.to_csv(DownloadData,encoding="gbk",index=False)
print(result)


### 登出系统 ###
bs.logout



