#!/usr/bin/env python3

import os
import requests


def getDescriptionEntries():
    path = "supplier-data/descriptions/"
    descriptionObjTempl = {
        'name': str(),
        'weight': int(),  # in lb
        'description': str(),
        'image_name': str()
    }
    feedbackObjects = []
    fruitImgCounter = 1
    sortedDirEntries = os.listdir(path)
    sortedDirEntries.sort()
    for file in sortedDirEntries:
        fullFilePath = os.path.join(path, file)
        with open(fullFilePath) as feedback:
            # for line in feedback:
            feedbackObjTempl = {'name': feedback.readline(),
                                'weight': int(feedback.readline()[:-4]),
                                'description': feedback.readline(),
                                'image_name': f"00{fruitImgCounter}.jpeg"
                                }
            feedbackObjects.append(feedbackObjTempl)
        fruitImgCounter += 1
        feedback.close()
    return feedbackObjects


# TODO: Need to sort os.listdir(path) in order to have the right image for each description

def main():
    descriptions = getDescriptionEntries()
    for description in descriptions:
        print(description)
        response = requests.post("http://35.202.239.72/fruits", data=description)
        if not response.ok:
            raise Exception("POST failed with status code {}".format(response.status_code))


main()
