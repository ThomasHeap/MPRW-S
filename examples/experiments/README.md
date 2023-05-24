# Movielens
To replicate the movielens experiments in figures 1 and 2:

First read and follow the instructions in the movielens folder to obtain the dataset.

### Global RWS
```sh
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_global training.N=5 training.M=150 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_global training.N=5 training.M=50 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_global training.N=5 training.M=300 training.pred_ll.do_pred_ll=True training.Ks=[3,10,30,100,300,1000,3000,10000]
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_global training.N=10 training.M=150 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_global training.N=10 training.M=50 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_global training.N=10 training.M=300 training.pred_ll.do_pred_ll=True
```
### MP RWS
```sh
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_tmc_new training.N=5 training.M=150 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_tmc_new training.N=5 training.M=50 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_tmc_new training.N=5 training.M=300 training.pred_ll.do_pred_ll=True training.Ks=[1,3,10,30,100]
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_tmc_new training.N=10 training.M=150 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_tmc_new training.N=10 training.M=50 training.pred_ll.do_pred_ll=True
python runner.py dataset=movielens model=movielens_discrete training.inference_method=rws_tmc_new training.N=10 training.M=300 training.pred_ll.do_pred_ll=True
```
### Plotting
```sh
python movielens/plot_rws.py
python movielens/plot_rws_fig2.py
```
# Bus Breakdown NYC
To replicate the NYC bus breakdown dataset experiments in figure 3:

First read and follow the instructions in the bus_breakdown folder to obtain the dataset.

### Running experiments
```sh
python runner.py dataset=bus_breakdown model=bus_breakdown training.inference_method=rws_tmc_new training.pred_ll.do_pred_ll=True training.num_iters=75000
python runner.py dataset=bus_breakdown model=bus_breakdown training.inference_method=rws_global training.pred_ll.do_pred_ll=True training.num_iters=75000 training.Ks=[3,10,30,100,300,1000,3000,10000,30000]
```
### Plotting
```sh
python bus_breakdown/plot_rws.py
```

# Timeseries

To replicate the timeseries model experiments in figure 4:

### Running experiments
```sh
mkdir timeseries/results
python timeseries/timeseries.py
python timeseries/timeseries_more_obs.py
```
### Plotting
```sh
python timeseries/plot_elbos.py
```
