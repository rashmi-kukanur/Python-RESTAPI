#!/bin/python3
import requests
import json

endpoint_str='https://api.nasa.gov/planetary/earth/assets'
key='api_key=aG8m58V0NSORbqSiK8oLjB4ueR59ZYCH6mRY9bxZ'

def get_location():
    print("Enter the latitude and longitude of the location")
    llist=input().strip().split()
    print("Enter the begin date in year-mm-dd format")
    begin_date=input()
    return([float(llist[0]),float(llist[1]),begin_date])

def build_url(lat,lon,bg_date):
    url=endpoint_str+"?"+"lon=%f"%(lon)+"&"+"lat=%f"%(lat)+"&"+"begin=%s"%(bg_date)+"&"+key
    return(url)


def get_latest_date(url):
    r = requests.get(url)

    assert r.status_code==200

    d = r.json()
    count = d['count']

    print("Last image of this location taken on %s"%(d['results'][count - 1]['date']))


if(__name__=='__main__'):
    location_list=get_location()
    new_url=build_url(location_list[0],location_list[1],location_list[2])
    get_latest_date(new_url)


