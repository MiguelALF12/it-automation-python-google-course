#!/usr/bin/env python3
import requests
import os
import re

# This example shows how a file can be uploaded using
# The Python Requests module

"""
url = ""
path = ""
with open(path, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
"""


def uploadingImages():
    path = "supplier-data/images"
    url = "http://35.222.112.221/upload/"
    with os.scandir(path) as imagesDirectory:
        for entry in imagesDirectory:
            if re.search("[0-9][0-9][0-9][.]jpeg", entry.name):
                fullFilePath = entry
                with open(fullFilePath, 'rb') as opened:
                    response = requests.post(url, files={'file': opened})
                    if not response.ok:
                        raise Exception("POST failed with status code {}".format(response.status_code))
                opened.close()
    imagesDirectory.close()


uploadingImages()
