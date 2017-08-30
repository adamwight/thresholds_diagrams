#!/usr/bin/python

import csv
import json

content = open("draftquality.json", "r").read()
data = json.loads(content)

thresholds = data["scores"]["enwiki"]["draftquality"]["info"]["statistics"]["thresholds"]

fieldnames = thresholds["OK"][0].keys()

for target_class, points in thresholds.items():
    out = open("draftquality-{target_class}.csv".format(target_class=target_class), "w")
    writer = csv.DictWriter(out, fieldnames)
    writer.writeheader()
    for line in points:
        writer.writerow(line)

out.close()
