import cfscrape

import requests
from threading import Thread
from bs4 import BeautifulSoup
from terminaltables import AsciiTable
from colored import fg, bg, attr
from os import system
from art import text2art
import sys

# system("title " + "DramaCool Granner | Anbuselvan Rocky")
# system('cls')

reset = attr('reset')
# art = text2art("DramaCool Scraper")
# print(fg("red") + art + reset)
# print(f"{fg('#0ecf12')}Developed by Anbuselvan Rocky{reset}")
search_result_table = [["Index", "Drama Name"]]

# search_drama()

# download_drama()


def startDownloading(finalLink):
    # print("These are finalLinks: " + finalLink)

    # searching_color = fg("green")
    # print(searching_color + "[*] Searching for " + finalLink + "....." + reset)

    drama_download_urls = []

    downloadList = []

    # url = f"https://www3.dramacool.movie/search?type=movies&keyword={query}"
    url = f"{finalLink}"

    result = requests.get(url).text

    # if "don't exist" in result:
    #     print(f"{fg('red')}[*] No results found for {query}!{reset}")
    #     exit()

    soup = BeautifulSoup(result, "html.parser")

    print(soup)
    sys.exit()

    downloadLinks = soup.find_all('div', {'class': 'dowload'})

    for link in downloadLinks:
        downloadList.append(link.text)

    print(downloadList)
    sys.exit()

    # for i in range(len(drama_Names)):
    #     search_result_table.append([str(i + 1), drama_Names[i]])

    # table = AsciiTable(search_result_table)
    # table_color = fg("#66e887")
    # print(table_color + table.table + reset)
    # print(searching_color + "[*] Total Results " +
    #       str(len(drama_Names)) + reset)

    # drama_choice = int(
    #     input("Enter the index number of the drama you want to scrape: ")) - 1
    # print()
    # get_episodes_url(drama_details_urls[drama_choice].replace("'", ""))


def startDownloading2(finalLink):
    # replace url with anti-bot protected website
    target_url = finalLink
    scraper = cfscrape.create_scraper()
    html_text = scraper.get(target_url).text
    parsed_html = BeautifulSoup(html_text, 'html.parser')
    print(parsed_html)


with open('download_links_final.txt', 'r') as downloadFile:
    for link in downloadFile:
        startDownloading2(link)
