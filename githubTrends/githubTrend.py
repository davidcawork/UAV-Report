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


def generateTrendByYear():

    years = [str(year) for year in range(2008, 2021)]
    tecn = {"url": URL_DRONE, "data": {}}

    for year in years:
        try:
            tecn["data"][year] = requests.get(tecn["url"] + '+created:'+str(int(year))+'-01-01..'+str(int(year)+1)+'-01-01&per_page=100&page=1', auth=(USER, TOKEN)).json()["total_count"]
        except:
            print("Error :D huehuehuehue time to debug ")

    with open('data/githubTrendYear.csv', 'w') as file:
        file.write('Year,Repositories created\n')
        for year in years:
            file.write(year + ','+str(tecn["data"][year])+'\n')


if __name__ == '__main__':
    generateTrendByYear()
