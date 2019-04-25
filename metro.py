import urllib.request



metro = "http://www.delhimetrorail.com/metro-fares.aspx"
page = urllib.request.urlopen(metro)

print(page)