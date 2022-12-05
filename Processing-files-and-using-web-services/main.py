import os
import requests


def getFeedbacksEntries():
    # path = "/data/feedback/" #This the path for the qwiklab
    path = "feedbacks"
    feedbackObjTempl = {'title': str(),
                        'name': str(),
                        'date': str(),
                        'feedback': str()}
    feedbackObjects = []
    for file in os.listdir(path):
        fullFilePath = os.path.join(path, file)
        with open(fullFilePath) as feedback:
            # for line in feedback:
            feedbackObjTempl = {'title': feedback.readline(),
                                'name': feedback.readline(),
                                'date': feedback.readline(),
                                'feedback': feedback.readline()}
            feedbackObjects.append(feedbackObjTempl)

        feedback.close()
    return feedbackObjects


def main():
    feedbacks = getFeedbacksEntries()
    for feedback in feedbacks:
        print(feedback)
        # This URL may do not work in the future, this is the one from the qwiklab, so unless I restarted,
        # it will need to be an app from my own
        """
        response = requests.post("http://34.122.120.189/feedback/", data=feedback)
        if not response.ok:
            raise Exception("POST failed with status code {}".format(response.status_code))
        """


main()
