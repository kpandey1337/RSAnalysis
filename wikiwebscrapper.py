import requests
import re
import csv
import datetime


url = "https://runescape.wiki/w/Module:Exchange/Fire_rune/Data?action=raw"
page = requests.get(url)

f= open("data.txt", "w")
rsdata = page.text
rsdata = re.sub('[return\{\'\}\\t]','',rsdata)
f.write(rsdata)
f.close()
myfile = open("data.txt", "r")
g=open("finishedData.txt", "w")

with open('finished_data.csv', mode='w') as data_file:
    data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['Date','fire_rune'])
    for line in myfile:
        if re.search('.*:.*:.*', line):
            line = re.sub('(:[0-9]*\.[0-9],)$', '' , line)
            line = re.sub(':', ',',line)
            line = re.sub(r'\s*','', line)
        else:
            line = re.sub(':', ',',line)
            line = re.sub(r'\s*','', line)
            if line.endswith(','):
                line = line[:-1]
        date_price=line.split(",")
        date=(date_price[0])
        if date != '':
            data_writer.writerow([datetime.datetime.utcfromtimestamp(int(date)).strftime('%Y-%m-%d'), date_price[1]])
        g.write(line)



data_file.close()
#(date:price:volume,)x
#([0-9]+:[0-9]+(:*)?,)+
# with open('finished_data.csv', mode='w') as data_file:
#     data_writer = csv.writer(data_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     data_writer.writerow([])
# ^[0-9]+
g.close()
