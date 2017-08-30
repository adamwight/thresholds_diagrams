.PHONY: clean datasets

datasets: draftquality-OK.csv damaging.csv

clean:
	rm -f *.csv *.json

draftquality.json:
	curl "https://ores-misc.wmflabs.org/v2/scores/enwiki/draftquality/?model_info=statistics.thresholds" > $@

draftquality-OK.csv: draftquality.json
	python dq-csv.py

damaging.json:
	curl "https://ores-misc.wmflabs.org/v2/scores/enwiki/damaging/?model_info=statistics.thresholds.true" > $@

damaging.csv: damaging.json
	python eq-csv.py
