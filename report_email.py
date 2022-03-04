#!/usr/bin/env python3
import os
import datetime
import reports
import emails

def main():
    path = 'supplier-data/descriptions/'
    report_body = ""
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file = open(os.path.join(path, file))
            text = file.readlines()
            name = "Name: {}".format(text[0])
            weight = "Weight: {}".format(text[1])
            report_body += "{}<br/>{}<br/><br/>".format(name, weight)
    
    report_path = '/tmp/processed.pdf'
    
    today = datetime.datetime.today()
    MM = today.strftime("%B")
    DD = today.day
    YYYY = today.year
    report_title = "Processed Update on {} {}, {}".format(MM, DD, YYYY)

    reports.generate_report(report_path, report_title, report_body)
    
    sender = "automation@example.com"
    receiver = 'studen@example.com'
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = '/tmp/processed.pdf'
    
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    
    emails.send_email(message)

if __name__ == "__main__":
    main()
