datasets: draftquality.json damaging.json

draftquality.json:
	curl "https://ores-misc.wmflabs.org/v2/scores/enwiki/draftquality/?model_info=statistics.thresholds" > $@

draftquality-OK.csv: draftquality.json
	python dq-csv.py

damaging.json:
	curl "https://ores-misc.wmflabs.org/v2/scores/enwiki/damaging/?model_info=statistics.thresholds.true" > $@

damaging.csv:
	python eq-csv.py
