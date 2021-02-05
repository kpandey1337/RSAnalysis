import requests
import re
import csv
import datetime
import pandas as pd
from bs4 import BeautifulSoup

row_list = []
dict1 = {}
itemCount = 0

url = "https://runescape.wiki/w/Category:Grand_Exchange_items"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

#isttags = soup.find_all('li')
#for soups in listtags:
#    print(soups)
#print("size of list is: ", len(listtags))




complete_item_list = []


for x in range(0, 1):
    categorylist = soup.find_all('div', attrs={"class": "mw-category-group"})
    for category in categorylist:
        itemlist = category.find_all('li')
        for item in itemlist:
            a_attribute = item.find('a')
            a_content = a_attribute.contents
            htmlitem = "".join(a_content)
            correctitem = re.sub('[\[\]\']','',htmlitem)
            correctitem_nospace = re.sub(' ', '_',correctitem)
            complete_item_list.append(correctitem_nospace)


    print("size of item list: ", len(itemlist))
    nextpage = soup.find_all('a', attrs={"title": "Category:Grand Exchange items"})
    for eachoption in nextpage:
        option = str(eachoption.text);
        print(option)
        if option == 'next page':
            url = eachoption['href']
            print("going to url : https://runescape.wiki/" + url )
            page = requests.get("https://runescape.wiki/" + url)

            soup = BeautifulSoup(page.content, 'html.parser')
            print(url)

############
#Whip#
############
    # url = "https://runescape.wiki/w/Module:Exchange/Abyssal_whip/Data?action=raw"
    # page = requests.get(url)
    # open('data.txt', 'w').close()
    # f = open("data.txt", "w")
    # rsdata = page.text
    # rsdata = re.sub('[return\{\'\}\\t]','',rsdata)
    # f.write(rsdata)
    # f.close()
    # myfile = open("data.txt", "r")
    # time = ""
    # print (item)
    # for line in myfile:
    #     if re.search('.*:.*:.*', line):
    #         line = re.sub('(:[0-9]*\.[0-9],)$', '' , line)
    #         line = re.sub(':', ',',line)
    #         line = re.sub(r'\s*','', line)
    #     else:
    #         line = re.sub(':', ',',line)
    #         line = re.sub(r'\s*','', line)
    #         if line.endswith(','):
    #             line = line[:-1]
    #     date_price=line.split(",")
    #     date=(date_price[0])
    #     if date != '':
    #         time = str(datetime.datetime.utcfromtimestamp(int(date)).strftime('%Y-%m-%d'))
    #         price = date_price[1]
    #         if time in dict1.keys():
    #             if len(dict1[time]) == itemCount:
    #                 dict1[time].append(price)
    #         else:
    #             dict1[time] = [price]
    #         date = ''
    #         time = ''
    # itemCount += 1

        deletedCount=1

for item in complete_item_list:
        url = "https://runescape.wiki/w/Module:Exchange/"+ item +"/Data?action=raw"
        page = requests.get(url)
        open('data.txt', 'w').close()
        f = open("data.txt", "w")
        rsdata = page.text
        rsdata = re.sub('[return\{\'\}\\t]','',rsdata)
        f.write(rsdata)
        f.close()
        myfile = open("data.txt", "r")
        time = ""
        print (item)
        skipped = True
        for line in myfile:
            skipped = False
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
                time = str(datetime.datetime.utcfromtimestamp(int(date)).strftime('%Y-%m-%d'))
                price = date_price[1]
                if time in dict1.keys():
                    if len(dict1[time]) == itemCount:
                        dict1[time].append(price)
                else:
                    dict1[time] = [price]
                date = ''
                time = ''
        if skipped == True:
            print ("deleted item:" + item + " deleted item count:" + str(deletedCount))

            deletedCount+=1
            complete_item_list.remove(item)
            if item in complete_item_list:
                print (item)
        else:
            itemCount += 1
        myfile.close()




df = pd.DataFrame.from_dict(dict1, orient='index', columns=complete_item_list)
df.to_csv(r'/Users/sebinyoon/Documents/self/RSAnalysis/file_name.csv')





#data_file.close()
#(date:price:volume,)x
#([0-9]+:[0-9]+(:*)?,)+
# with open('finished_data.csv', mode='w') as data_file:
#     data_writer = csv.writer(data_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     data_writer.writerow([])
# ^[0-9]+