#!/usr/bin/python

import csv
import json

content = open("damaging.json", "r").read()
data = json.loads(content)

thresholds = data["scores"]["enwiki"]["damaging"]["info"]["statistics"]["thresholds"]

fieldnames = thresholds["true"][0].keys()

for target_class, points in thresholds.items():
    out = open("damaging.csv".format(target_class=target_class), "w")
    writer = csv.DictWriter(out, fieldnames)
    writer.writeheader()
    for line in points:
        writer.writerow(line)

out.close()
