import requests


url = "https://runescape.wiki/w/Module:Exchange/Fire_rune/Data?action=raw"
page = requests.get(url)

f= open("data.txt", "a")
f.write(page.text)
f.close()