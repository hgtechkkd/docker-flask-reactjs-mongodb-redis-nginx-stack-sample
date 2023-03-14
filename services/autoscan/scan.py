import calendar
from pymongo import MongoClient
# import boto3
from dotenv import load_dotenv
from pathlib import Path
# import os
import logging
import time


from os import listdir,getenv
from os.path import isfile, join
import glob

load_dotenv()

key = getenv("key")
secret = getenv("secret")
region = getenv("region")
dburl = getenv("MONGOURI")
dbname =  getenv("DBNAME")

# walkpath = Path("E:\\docker\\volume_backups\\nimbleocrfiles\\")
walkpath = Path("/data/files/")
polltime = 5
SKIP_DIRS = ["temp", "logs"]

print("connecting to mongodb...")
try:
    mongo = MongoClient(dburl)
except Exception as e:
    print(e)

db = mongo[dbname]
coll = db["files"]


def listDiff(OriginalList: list, NewList: list):
    diff = [x for x in NewList if x not in OriginalList] # not checking deleted files
    return(diff)

def watcher(dir, polltime):
    while True:
        if 'watching' not in locals():
            # prevList = glob.glob(dir, recursive=True)
            prevList = [i.stem for i in dir.rglob("*") if set(i.parts).isdisjoint(SKIP_DIRS)]
            watching = 1
            # print("first list = ", prevList)
        
        time.sleep(polltime)
        # newList = glob.glob(dir, recursive=True)
        newList = [i.stem for i in dir.rglob("*") if set(i.parts).isdisjoint(SKIP_DIRS)]
        # print("next list = ", newList)
        diff = listDiff(prevList, newList)
        prevList = newList

        if(len(diff)==0): continue
        processNewFiles(diff)


def processNewFiles(flist):
    print("New files found ...!")
    document = {"timestamp":calendar.timegm(time.gmtime()), "files":flist}
    print(document)
    coll.insert_one(document)

print(f"Watching files in {walkpath} for every {polltime} seconds")
watcher(walkpath, polltime)