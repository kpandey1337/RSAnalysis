import requests
import re


url = "https://runescape.wiki/w/Module:Exchange/Fire_rune/Data?action=raw"
page = requests.get(url)

f= open("data.txt", "w")
rsdata = page.text
rsdata = re.sub('[return\{\'\}\\t]','',rsdata)
f.write(rsdata)
f.close()
myfile = open("data.txt", "r")
g=open("finishedData.txt", "w")


for line in myfile:
    if re.search('.*:.*:.*', line):
        print(line)
        line = re.sub('(:[0-9]*\.[0-9],)$', ',' , line)
        print(line)
        g.write(line)
    else:
        g.write(line)

#(date:price:volume,)x
#([0-9]+:[0-9]+(:*)?,)+


# ^[0-9]+
g.close()
