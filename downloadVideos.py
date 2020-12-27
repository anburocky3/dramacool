import webbrowser
import time
import urllib.parse as urlparse
from urllib.parse import parse_qs


def saveLinks(links):
    f = open("download_links_final.txt", "a")
    f.write(links + '\n')
    f.close()


def buildLinkStructure(link):
    urlToParse = "https://k-vid.co/download?id="
    parsed = urlparse.urlparse(link)

    idValue = parse_qs(parsed.query)['id'][0]
    finalLink = urlToParse + idValue
    print(finalLink)
    saveLinks(finalLink)
    webbrowser.open_new_tab(finalLink)
    time.sleep(10)


with open('download_links.txt', 'r') as downloadFile:
    open('file.txt', 'w').close()
    for link in downloadFile:
        buildLinkStructure(link)
        # if 'str' in line:
        #     break
