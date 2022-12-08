#!/usr/bin/env python3

"""
 It will run in the background monitoring some of your system statistics: CPU usage, disk space,
 available memory and name resolution.
 Moreover, this Python script should send an email if there are problems, such as:

        Report an error if CPU usage is over 80%
        Report an error if available disk space is lower than 20%
        Report an error if available memory is less than 500MB
        Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

"""

import psutil
import shutil
import emails


# disk_usage = shutil.disk_usage("/")
# new_disk_usage = disk_usage.free/disk_usage.total * 100
# print(disk_usage, new_disk_usage)
#
# #using core information
# psutil.cpu_percent(0.1)# gives the average of cpu usage within the interval passed, i.e 0.1


def cpu_usage_warning():
    usage = psutil.cpu_percent(0.1)
    return True if usage >= 80.0 else False


def storage_state_warning():
    disk_usage = shutil.disk_usage("/")
    available_disk = disk_usage.free / disk_usage.total * 100
    return True if available_disk <= 20 else False


def memory_state_warning():
    mem = psutil.virtual_memory()
    THRESHOLD = 500 * 1024 * 1024  # 100MB
    return True if mem.available <= THRESHOLD else False


# TODO: Left for hostname resolution implementation


if __name__ == "__main__":
    subject = str()
    if cpu_usage_warning():
        subject = "Error - CPU usage is over 80%"
    elif storage_state_warning():
        subject = "Error - Available disk space is less than 20%"
    elif memory_state_warning():
        subject = "Error - Available memory is less than 500MB"
    else:
        subject = "Something is doing wrong!!"

    message = emails.generate_email("automation@example.com", "student-03-ae13425c3d3c@example.com", subject,
                                    "Please check your system and resolve the issue as soon as possible.", "")

    emails.send_email(message)
