import urllib.request
import os
import time

path = "data/intraQuarter"


def Check_Yahoo():
    statspath = path + "/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]

    for e in stock_list[1:]:
        try:
            e = e.replace("data/intraQuarter/_KeyStats/", "")
            link = "http://finance.yahoo.com/q/ks?s=" + e.upper() + "+Key+Statistics"
            print(link)
            resp = urllib.request.urlopen(link).read()

            print(resp)
            save = "forward/" + str(e) + ".html"
            store = open(save, "w")
            store.write(str(resp))
            store.close()

        except Exception as e:
            print(str(e))
            time.sleep(2)


Check_Yahoo()
