import urllib2
import json
import time
 
def fetchPreMarket(symbol, exchange):
    link = "http://finance.google.com/finance/info?client=ig&q="
    url = link+"%s:%s" % (exchange, symbol)
    u = urllib2.urlopen(url)
    content = u.read()
    data = json.loads(content[3:])
    info = data[0]
    t = str(info["lt"])
    l = float(info["pcls_fix"])
    p = float(info["l"])
    return (t,l,p)
 
 
p0 = 0
while True:
    t, l, p = fetchPreMarket("GOOG","NASDAQ")
    if(p!=p0):
        p0 = p
        print("%s\t%.2f\t%.2f\t%+.2f\t%+.2f%%" % (t, l, p, p-l,
                                                 (p/l-1)*100.))
    time.sleep(1)

