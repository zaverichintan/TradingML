import pandas as pd
import os
import time
from datetime import datetime

path = "data/intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns = ['Date','Unix','Ticker','DE Ratio'])
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        print(1)
        ticker = each_dir.split("/")
        ticker = ticker[3]
        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())
                full_file_path = each_dir+'/'+file
                source = open(full_file_path,'r').read()
                # print(source)

                try:
                    value = source.split(gather+':</td><td class="yfnc_tabledata1">')
                    value = value[1]
                    value = value.split('</td>')
                    value = float(value[0])
                    print(date_stamp, unix_time, ticker, value)
                    df = df.append({'Date':date_stamp,'Unix':unix_time,'Ticker':ticker,'DE Ratio':value,}, ignore_index = True)
                except Exception as e:
                    print("Exception")
                    pass


    save = gather.replace(' ', '').replace(')', '').replace('(', '').replace('/', '')+('.csv')
    print(save)
    print(df)
    df.to_csv(save)

Key_Stats()

