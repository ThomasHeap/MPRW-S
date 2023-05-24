import numpy as np
import matplotlib.pyplot as plt
import json
from tueplots import axes, bundles

Ks = ['3', '10','30','100', '300','1000']


plt.rcParams.update({"figure.dpi": 300})
with plt.rc_context(bundles.icml2022()):

    count = 0
    fig_elbos, ax_elbos = plt.subplots(1,1, figsize=(5.5/2, 2.0))

    with open('results/timeseries_elbo_tmc_new.json') as f:
        elbo_tmc_new = json.load(f)

    with open('results/timeseries_elbo_tmc.json') as f:
        elbo_tmc = json.load(f)

    with open('results/timeseries_elbo_global.json') as f:
        elbo_global = json.load(f)


    elbos_tmc_new = [elbo_tmc_new[k]['mean'] for k in Ks]
    stds_tmc_new = [elbo_tmc_new[k]['std_err'] for k in Ks]

    elbos_tmc = [elbo_tmc[k]['mean'] for k in Ks]
    stds_tmc = [elbo_tmc[k]['std_err'] for k in Ks]

    elbos_global = [elbo_global[k]['mean'] for k in Ks]
    stds_global = [elbo_global[k]['std_err'] for k in Ks]


    ax_elbos.errorbar(Ks,elbos_tmc_new, yerr=stds_tmc_new, linewidth=0.55, markersize = 0.75, fmt='-o', c='red', label='Massively Parallel')
    ax_elbos.errorbar(Ks,elbos_tmc, yerr=stds_tmc, linewidth=0.55, markersize = 0.75, fmt='-o', c='orange', label='TMC')
    ax_elbos.errorbar(Ks,elbos_global, yerr=stds_global, linewidth=0.55, markersize = 0.75, fmt='-o', c='blue', label='Global Importance Weighting')

    ax_elbos.set_ylabel('Evidence Lower Bound')
    ax_elbos.set_xlabel('K')


    ax_elbos.annotate(r'\bf{a}', xy=(0, 1), xycoords='axes fraction', fontsize=10,
                xytext=(-30, 5), textcoords='offset points',
                ha='right', va='bottom')
    plt.savefig('charts/timeseries.png')
    plt.savefig('charts/timeseries.pdf')


    with open('results/timeseries_more_obs_elbo_tmc_new.json') as f:
        elbo_tmc_new = json.load(f)

    with open('results/timeseries_more_obs_elbo_tmc.json') as f:
        elbo_tmc = json.load(f)

    with open('results/timeseries_more_obs_elbo_global.json') as f:
        elbo_global = json.load(f)

    Ks = ['3', '10','30','100', '300','1000']
    fig_elbos, ax_elbos = plt.subplots(1,1, figsize=(5.5/2, 2.0))

    elbos_tmc_new = [elbo_tmc_new[k]['mean'] for k in Ks]
    stds_tmc_new = [elbo_tmc_new[k]['std_err'] for k in Ks]

    elbos_tmc = [elbo_tmc[k]['mean'] for k in Ks]
    stds_tmc = [elbo_tmc[k]['std_err'] for k in Ks]

    elbos_global = [elbo_global[k]['mean'] for k in Ks]
    stds_global = [elbo_global[k]['std_err'] for k in Ks]

    ax_elbos.errorbar(Ks,elbos_tmc_new, yerr=stds_tmc_new, linewidth=0.55, markersize = 0.75, fmt='-o', c='red', label='Massively Parallel')
    ax_elbos.errorbar(Ks,elbos_tmc, yerr=stds_tmc, linewidth=0.55, markersize = 0.75, fmt='-o', c='orange', label='TMC')
    ax_elbos.errorbar(Ks,elbos_global, yerr=stds_global, linewidth=0.55, markersize = 0.75, fmt='-o', c='blue', label='Global Importance Weighting')

    font = {'color':  'white',
            }

    ax_elbos.set_ylabel('i', fontdict=font)
    ax_elbos.set_xlabel('K')

    ax_elbos.annotate(r'\bf{b}', xy=(0, 1), xycoords='axes fraction', fontsize=10,
                xytext=(-30, 5), textcoords='offset points',
                ha='right', va='bottom')
    plt.legend()
    plt.savefig('charts/timeseries_more_obs.png')
    plt.savefig('charts/timeseries_more_obs.pdf')
