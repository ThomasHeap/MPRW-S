import torch as t
import torch.distributions as dist
import torch.nn as nn
import alan
import math
from alan.experiment_utils import seed_torch
from functorch.dim import dims, Dim
from alan.utils import *
from alan.dist import Categorical
import json
import numpy as np
import time
seed_torch(1)

device = t.device("cuda" if t.cuda.is_available() else "cpu")

N = 30

var = float(1/math.sqrt(N))
tau = 5
def P(tr):
    tr.sample('ts_1', alan.Normal(0.0, np.sqrt(2/tau)))
    for i in range(2,N+1):
        latent = (1-(1/tau))*tr['ts_{}'.format(i-1)]
        tr.sample('ts_{}'.format(i), alan.Normal(latent, np.sqrt(2/tau)))
        if i % 3 == 0:
            tr.sample('obs_{}'.format(i//3), alan.Normal(tr['ts_{}'.format(i)], 1))

def Q(tr):
    tr.sample('ts_1', alan.Normal(0.0, np.sqrt(2/tau)))
    # print(tr['ts_1'])
    for i in range(2,N+1):
        latent = (1-(1/tau))*tr['ts_{}'.format(i-1)]
        tr.sample('ts_{}'.format(i), alan.Normal(latent, np.sqrt(2/tau)))




## Running exps
Ks=[3,10,30,100,300,1000]

elbos = {k:[] for k in Ks}
elbos_tmc = {k:[] for k in Ks}
elbos_global = {k:[] for k in Ks}


times = {k:[] for k in Ks}
times_tmc = {k:[] for k in Ks}
times_global = {k:[] for k in Ks}

varnames = ('obs_{}'.format(j) for j in range(1,N//3 + 1))
num_runs = 100
for i in range(num_runs):
    varnames = ('obs_{}'.format(j) for j in range(1,N//3 + 1))
    data = alan.sample(P, varnames=tuple(varnames))
    for k in Ks:
        model = alan.Model(P, Q, data)
        start = time.time()
        elbos[k].append(model.elbo_tmc_new(k).item())
        end = time.time()
        times[k].append(end-start)
        start = time.time()
        elbos_tmc[k].append(model.elbo_tmc(k).item())
        end = time.time()
        times_tmc[k].append(end-start)
        start = time.time()
        elbos_global[k].append(model.elbo_global(k).item())
        end = time.time()
        times_global[k].append(end-start)

for k in Ks:
    elbos[k] = {'mean':np.mean(elbos[k]), 'std_err':np.std(elbos[k])/np.sqrt(num_runs), 'time_mean':np.mean(times[k]), 'time_std_err':np.std(times[k])/np.sqrt(num_runs)}
    elbos_tmc[k] = {'mean':np.mean(elbos_tmc[k]), 'std_err':np.std(elbos_tmc[k])/np.sqrt(num_runs), 'time_mean':np.mean(times_tmc[k]), 'time_std_err':np.std(times_tmc[k])/np.sqrt(num_runs)}
    elbos_global[k] = {'mean':np.mean(elbos_global[k]), 'std_err':np.std(elbos_global[k])/np.sqrt(num_runs), 'time_mean':np.mean(times_global[k]), 'time_std_err':np.std(times_global[k])/np.sqrt(num_runs)}

file = 'results/timeseries_more_obs_elbo_tmc_new.json'
with open(file, 'w') as f:
    json.dump(elbos, f)

file = 'results/timeseries_more_obs_elbo_tmc.json'
with open(file, 'w') as f:
    json.dump(elbos_tmc, f)

file = 'results/timeseries_more_obs_elbo_global.json'
with open(file, 'w') as f:
    json.dump(elbos_global, f)
