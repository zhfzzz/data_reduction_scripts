import os
from ezmethods import *
import pandas as pd
import matplotlib.pyplot as plt
import os
SIZE=35
# Latex interpretation for plots
plt.rcParams.update({'font.size': SIZE})
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'DejaVu Serif'
plt.rcParams["mathtext.fontset"] = "cm"#
plt.rcParams["figure.dpi"] = 400
plt.rcParams['figure.figsize'] = 23,8
#
plt.rc('font', size=SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SIZE)    # legend fontsize
plt.rc('figure', titlesize=SIZE)  #
# left=0.08, right=0.98,top=0.9, bottom=0.2, wspace=0.02, hspace=0.1
    

plot_eff_strain(0,all=True,marker_size=15)
#plot_yield_stress(0,all=True,marker_size=15)

exit(0)