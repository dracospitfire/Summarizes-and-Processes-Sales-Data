#!/usr/bin/env python3

import psutil
import socket
import emails

"""System Parameters"""
max_cpu_usage_perc = 80
max_disk_avail_perc = 20
max_mem_avail_mb = 500
chk_local_host_ip = "127.0.0.1"

def chkCPU():
    """Looking for CPU usage above 80%"""
    cpu_usage_perc = psutil.cpu_percent(interval=3)
    return cpu_usage_perc > max_cpu_usage_perc

def chkDisk():
    """Looking for available disk space"""
    max_disk_usage_perc = 100 - max_disk_avail_perc
    dsk_usage_perc = psutil.disk_usage("/").percent
    return dsk_usage_perc > max_disk_usage_perc

def chkMem():
    """Looking for available memory"""
    one_mb = 2 ** 20
    max_mem_avail = one_mb * max_mem_avail_mb
    mem_avail = psutil.virtual_memory().available
    return mem_avail < max_mem_avail

def chkNet():
    """Looking for "localhost" cannot be resolved to "127.0.0.1""""
    local_host_ip = socket.gethostbyname('localhost')
    return local_host_ip != chk_local_host_ip

def sendAlert(alert):
    """Send Email for Output Error"""
    sender = "automation@example.com"
    receiver = 'student@example.com'
    subject = alert
    body = "Please check your system and resolve the issue as soon as possible."
    attachment = None
    
    try:
        message = emails.generate_email(sender, receiver, subject, body, attachment)
        emails.send_email(message)
    except:
        print("unable to send alert email notification!")


def main():
    print("checking system resources")
    alert = None
    if chkCPU():
        alert = f"Error - CPU usage is over {max_cpu_usage_perc}%"
    elif chkDisk():
        alert = f"Error - Available disk space is less than {max_disk_avail_perc}%"
    elif chkMem():
        alert = f"Error - Available memory is less than {max_mem_avail_mb}MB"
    elif chkNet():
        alert = f"Error - localhost cannot be resolved to {chk_local_host_ip}"

    if alert:
        sendAlert(alert)
    else:
        print("system ok")

if __name__ == '__main__':
    main()
