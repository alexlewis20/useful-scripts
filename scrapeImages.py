import urllib.request
import requests

url = input("URL to scrape for images:")


response = requests.get(url)

html = response.text.split("\n")

imgLines = []

for x in range(len(html)):
    if "data-src=" in html[x]:
        inChar = html[x].find("data-src=") + 10
        outChar = html[x].find(".jpg") + 4
        imgUrl = html[x][inChar:outChar]
        imgLines.append(imgUrl)


# Test print
# for i in imgLines:
#     print(i)
#     print('\n**********\n')

def scrape(imgUrl, filename):
    """scrapes and saves the url to the given name"""
    folder = input("Output folder path:")
    outputPath = folder + "/" + filename
    urllib.request.urlretrieve(imgUrl, outputPath)
    return outputPath
    
    
for z in range(len(imgLines)):
    try:
        if len(imgLines[z]) > 0:
            scrape(imgLines[z], str(z) + ".jpg" )
    except Exception as e:
        print(e)
print("Done")