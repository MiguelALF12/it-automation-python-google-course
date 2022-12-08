#!/usr/bin/env python3

from datetime import date
import os
import reports
import emails


def process_data():
    path = "supplier-data/descriptions/"
    formatted_descriptions = ""
    orderedDirEntries = os.listdir(path)
    orderedDirEntries.sort()

    for file in orderedDirEntries:
        fullFilePath = os.path.join(path, file)
        with open(fullFilePath) as description:
            formatted_descriptions += "\nname: {}<br/>weight: {} <br/><br/>".format(description.readline(),
                                                                                    description.readline())
        description.close()

    return formatted_descriptions


if __name__ == "__main__":
    descriptions = process_data()
    reports.generate_report("/tmp/processed.pdf",
                            "Processed Update on {}".format(date.today().isoformat()),
                            descriptions)
    message = emails.generate_email("automation@example.com", "student-03-ae13425c3d3c@example.com",
                                    "Upload Completed - Online Fruit Store",
                                    "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
                                    , "/tmp/processed.pdf")
    emails.send_email(message)
