#!/usr/bin/python3

import requests
import json
import os


#   Drones - UAV - UAS  GitHub request : https://api.github.com/search/repositories?q=drone+OR+UAV+OR+UAS&per_page=100&page=1
URL_DRONE = 'https://api.github.com/search/repositories?q=drone+OR+UAV+OR+UAS'
with open("auth.json") as json_file:
    auth_data = json.load(json_file)
USER = auth_data["user"]
TOKEN = auth_data["token"]


def getMaxPages(url, size):
    r = requests.get(url + '&per_page=' + str(size) + '&page=1', auth=(USER, TOKEN))
    pages = int(r.json()["total_count"] / size)
    if (r.json()["total_count"] % size != 0):
        pages += 1
    return pages


def getListofJsons(url):
    lst = []
    size = 100
    maxpages = getMaxPages(url, size)

    for i in range(1, maxpages):
        r = requests.get(url + '&per_page=' + str(size) + '&page=' + str(i), auth=(USER, TOKEN))
        lst.append(r.json())
    return lst


def getYear(strYear):
    return strYear[:4]


def generateTrendByYear():

    years = [str(year) for year in range(2010, 2021)]
    tecn = {"url": URL_DRONE, "data": {}}
    listJsons = getListofJsons(tecn["url"])

    for json in listJsons:
        try:
            for item in json["items"]:
                if getYear(item["created_at"]) in tecn["data"]:
                    tecn["data"][getYear(item["created_at"])] += 1
                else:
                    tecn["data"][getYear(item["created_at"])] = 1
        except:
            print(str(json))

    with open('githubTrendYear.csv', 'w') as file:
        file.write('2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020\n')
        for year in years:
            file.write(str(tecn["data"][year])+',')
        file.seek(file.tell() - 1, os.SEEK_SET)
        file.truncate()
        file.write('\n')


if __name__ == '__main__':
    generateTrendByYear()
