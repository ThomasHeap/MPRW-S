MovieLens
=========

<!-- put a description of movielens here -->

Data
====
1. Download data from https://data.cityofnewyork.us/Transportation/Bus-Breakdown-and-Delays/ez4e-fazm

2. Move the csv file to ./data
```sh
python make_data.py
```

Running scripts
===============


RWS:
```sh
python runner.py dataset=bus_breakdown model=bus_breakdown training.inference_method=rws training.pred_ll.do_pred_ll=False
```
