'''
Created on Aug 5, 2017

@author: runsheng
'''
import sys

from scipy.stats import lognorm

from src.qsar import *

if __name__ == '__main__':
    SMILEs = 'CNC(=O)O\N=C(/C)SC' # The input SMILEs must be a list

#     this_q = qsar("Lepomis Macrochirus")
#     print this_q.predict(SMILEs)
    this_q = run_all.run(SMILEs)
#     
    print this_q
    
#     from QSAR_SSD_Toolbox.src.ssd import ssd_generator

#     this_ssd = ssd_generator()
#     df_mean, df_high, df_low = this_ssd.generate(this_q, dist=lognorm, run_error=True,run_bootstrap=False, bootstrap_time=500, display_range=[2,8])
# 
#     print df_mean
#     print df_high
#     print df_low
    