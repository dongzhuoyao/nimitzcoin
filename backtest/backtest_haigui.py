# Author: Tao Hu <taohu620@gmail.com>

import os
from dotenv import load_dotenv
load_dotenv()

start_date = '20180701'
end_date='20180801'

# 此处填写APIKEY
TOKEN = os.getenv("TOKEN")
import tushare as ts
ts.set_token(TOKEN)
pro = ts.pro_api()
df = pro.coinbar(exchange='huobi', symbol='rdneth', freq='daily', start_date=start_date, end_date=end_date)
print(df)