#!/usr/bin/env python3

import os
import datetime
import reports
import emails

#def main():
path = 'descriptions' #"supplier-data/descriptions/"
report_body = ""
for file in os.listdir(path):
    if file.endswith(".txt"):
        file = open(os.path.join(path, file))
        text = file.readlines()
        name = "Name: {}".format(text[0])
        weight = "Weight: {}".format(text[1])
        report_body = "{}<br/>{}<br/><br/>".format(name, weight)
