import requests
from threading import Thread
from bs4 import BeautifulSoup
from terminaltables import AsciiTable
from colored import fg, bg, attr
from os import system
import os
from art import text2art
import sys
from signal import signal, SIGINT

import webbrowser
import time
import urllib.parse as urlparse
from urllib.parse import parse_qs

system("title " + "DramaCool Grabber | Anbuselvan Rocky")
system('cls')

rows, columns = os.popen('stty size', 'r').read().split()
version = "1.0"

availableColumn = int(columns)

reset = attr('reset')
art = text2art("DramaCool  Scraper")
print(fg("red") + art + reset)
print(f"{fg('#0ecf12')}*" * availableColumn + reset)
print(f"{fg('#0ecf12')}\t\t Developed by:{reset} {fg('#fff')}Anbuselvan Rocky,{reset} {fg('#48B8FF')}v{version}{reset}".center(
    availableColumn))
print(f"{fg('#0ecf12')}*" * availableColumn + reset)

search_result_table = [["Index", "Drama Name"]]


def get_episodes_url(drama_url):
    all_episodes = []
    result = requests.get(drama_url).text
    soup = BeautifulSoup(result, "html.parser")

    titles = soup.find_all('h3', {'class': 'title'})

    drama_Title = soup.find('h1').text
    details = soup.find_all('p')

    details_check = ""

    for i in range(1, len(details) - 1):
        if "Description" in details[i].text:
            details_check += details[i].text.replace("\n", " ") + "\n"
        else:
            details_check += details[i].text.replace("\n", " ") + "\n\n"

    print(f"{fg('#fca503')}Title: {drama_Title}{reset}\n")

    print(f"{fg('#e6be30')}{details_check}{reset}")

    for i in range(len(titles)):
        if ".html" in titles[i]['onclick']:
            all_episodes.append(titles[i]['onclick'].replace(
                "window.location = '", "https://www3.dramacool.movie"))

    for episode in all_episodes:
        Thread(target=get_video_url(episode.replace("'", ""))).start()


def saveLinks(links):
    f = open("download_links.txt", "a")
    f.write(links + '\n')
    f.close()


def saveDirectLinks(link):
    urlToParse = "https://k-vid.co/download?id="
    parsed = urlparse.urlparse(link)

    idValue = parse_qs(parsed.query)['id'][0]
    finalLink = urlToParse + idValue
    print(finalLink)

    # Save to file
    f = open("download_links_final.txt", "a")
    f.write(link + '\n')
    f.close()

    webbrowser.open_new_tab(finalLink)
    time.sleep(10)


def get_video_url(episode_url):
    result = requests.get(episode_url).text
    soup = BeautifulSoup(result, "html.parser")

    titles = soup.find('h1').text
    print(fg('#66e887') + titles.replace(" | Dramacool", "") + reset)

    embded_url = f"https:{soup.find('iframe')['src']}"

    print(embded_url)
    # saveLinks(embded_url)
    saveDirectLinks(embded_url)

    # print("*" * 20)
    # print()


def search_drama():
    # query = input("Drama to search: ")
    query = "lo"

    searching_color = fg("green")
    print(searching_color + "[*] Searching for " + query + "....." + reset)

    drama_details_urls = []

    drama_Names = []

    # url = f"https://www3.dramacool.movie/search?type=movies&keyword={query}"
    url = f"https://dramacool.so/search?type=movies&keyword={query}"

    result = requests.get(url).text

    if "don't exist" in result:
        print(f"{fg('red')}[*] No results found for {query}!{reset}")
        exit()

    soup = BeautifulSoup(result, "html.parser")

    # print(soup)
    # sys.exit()

    drama_titles = soup.find_all('h3', {'class': 'title'})

    for drama_title in drama_titles:
        drama_Names.append(drama_title.text)
        drama_details_urls.append(drama_title['onclick'].replace(
            # "window.location = '", "https://www3.dramacool.movie"))
            "window.location = '", "https://dramacool.so"))

    for i in range(len(drama_Names)):
        search_result_table.append([str(i + 1), drama_Names[i]])

    table = AsciiTable(search_result_table)
    table_color = fg("#66e887")
    print(table_color + table.table + reset)
    print()
    print(searching_color + "[*] Total Results " +
          str(len(drama_Names)) + reset)

    drama_choice = int(
        input("Enter the index number of the drama you want to scrape: ")) - 1
    print()
    get_episodes_url(drama_details_urls[drama_choice].replace("'", ""))


def handler(signal_received, frame):
    print("{fg('red')} \n Want to quit?. Exiting gracefully" + reset)
    exit(0)


if __name__ == "__main__":
    signal(SIGINT, handler)
    search_drama()
