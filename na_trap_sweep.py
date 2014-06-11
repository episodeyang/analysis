__author__ = 'Ge Yang'

from analysis_util import indexString
import matplotlib.pyplot as plt
from slab import dataanalysis
import numpy as np
import util

def get_na_trap_sweep(cache, stack_index, callback=None):
    indStr = indexString(stack_index)
    stack_prefix = "stack_" + indStr + '.'

    stackType = cache.get(stack_prefix+'type')
    startTime = cache.get(stack_prefix+'startTime')
    notes = cache.get(stack_prefix+'notes')
    fpts = cache.get(stack_prefix+'fpts')
    mags = cache.get(stack_prefix+'mags')
    phases = cache.get(stack_prefix+'phases')
    trapStart = cache.get(stack_prefix+'trapStart')
    trapEnd = cache.get(stack_prefix+'trapEnd')

    if callback != None:
        callback(stack_index, stackType, startTime, notes, fpts, mags, phases, trapStart, trapEnd)

    return stackType, startTime, notes, fpts, mags, phases

def na_trap_sweep_plotter(stack_index, stackType, startTime, notes, fpts, mags, phases, trapStart, trapEnd):
    plt.subplot(121)
    midInd = len(mags)/2;
    plt.imshow(np.transpose(mags[:midInd+1]), aspect='auto', interpolation='none', cmap = 'gist_rainbow',
           origin = 'lower', extent = [trapStart, trapEnd, min(fpts), max(fpts)])
    plt.subplot(122)
    plt.imshow(np.transpose(mags[midInd+1:]), aspect='auto', interpolation='none', cmap = 'gist_rainbow',
           origin = 'lower', extent = [trapEnd, trapStart, min(fpts), max(fpts)])
    # locator_params(nbins=10)
    plt.title('trap V vs transmission')
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.ylabel('Frequency (Hz)')
    plt.xlabel('Resonator voltage (V)')
