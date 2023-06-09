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
seed_torch(2)

device = t.device("cuda" if t.cuda.is_available() else "cpu")

N = 30

var = float(1/math.sqrt(N))
def P(tr):
    tr.sample('ts_1', alan.Normal(0.0, var))
    for i in range(2,N+1):
        tr.sample('ts_{}'.format(i), alan.Normal(tr['ts_{}'.format(i-1)], var))

    tr.sample('obs', alan.Normal(tr['ts_{}'.format(N)], 1))

def Q(tr):
    tr.sample('ts_1', alan.Normal(0.0, var))
    for i in range(2,N+1):
        tr.sample('ts_{}'.format(i), alan.Normal(tr['ts_{}'.format(i-1)], var))

data = {'obs':t.tensor(4)}
model = alan.Model(P, Q, data)
model.to(device)



## Running exps
Ks=[3,10,30,100,300,1000]
elbos = {k:[] for k in Ks}
elbos_tmc = {k:[] for k in Ks}
elbos_particle = {k:[] for k in Ks}
elbos_global = {k:[] for k in Ks}


times = {k:[] for k in Ks}
times_tmc = {k:[] for k in Ks}
times_particle = {k:[] for k in Ks}
times_global = {k:[] for k in Ks}

print(data)
for k in Ks:
    num_runs = 250
    for i in range(num_runs):
        start = time.time()
        model = alan.Model(P, Q, data)
        elbos[k].append(model.elbo_tmc_new(k).item())
        end = time.time()
        times[k].append(end-start)
        start = time.time()
        model = alan.Model(P, Q, data)
        elbos_tmc[k].append(model.elbo_tmc(k).item())
        end = time.time()
        times_tmc[k].append(end-start)
        start = time.time()
        elbos_global[k].append(model.elbo_global(k).item())
        end = time.time()
        times_global[k].append(end-start)

    elbos[k] = {'mean':np.mean(elbos[k]), 'std_err':np.std(elbos[k])/np.sqrt(num_runs), 'time_mean':np.mean(times[k]), 'time_std_err':np.std(times[k])/np.sqrt(num_runs)}
    elbos_tmc[k] = {'mean':np.mean(elbos_tmc[k]), 'std_err':np.std(elbos_tmc[k])/np.sqrt(num_runs), 'time_mean':np.mean(times_tmc[k]), 'time_std_err':np.std(times_tmc[k])/np.sqrt(num_runs)}
    elbos_global[k] = {'mean':np.mean(elbos_global[k]), 'std_err':np.std(elbos_global[k])/np.sqrt(num_runs), 'time_mean':np.mean(times_global[k]), 'time_std_err':np.std(times_global[k])/np.sqrt(num_runs)}

file = 'results/timeseries_elbo_tmc_new.json'
with open(file, 'w') as f:
    json.dump(elbos, f)

file = 'results/timeseries_elbo_tmc.json'
with open(file, 'w') as f:
    json.dump(elbos_tmc, f)

file = 'results/timeseries_elbo_global.json'
with open(file, 'w') as f:
    json.dump(elbos_global, f)
