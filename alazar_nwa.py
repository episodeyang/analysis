__author__ = 'Ge Yang'


from analysis_util import indexString
import matplotlib.pyplot as plt
from slab import dataanalysis
import numpy as np
import util

def get_alazar_nwa(cache, stack_index, callback=None):
    indStr = indexString(stack_index)
    stack_prefix = "stack_" + indStr + '.'
    stackType = cache.get(stack_prefix+'type')
    startTime = cache.get(stack_prefix+'startTime')
    notes = cache.get(stack_prefix+'notes')
    fpts = cache.get(stack_prefix+'fpts')
    rampHigh = cache.get(stack_prefix+'rampHigh')
    rampLow = cache.get(stack_prefix+'rampLow')
    try:
        Q = cache.get(stack_prefix+'Q')
    except: print "can't read Q data"
    try:
        I = cache.get(stack_prefix+'I')
    except: print "can't read I data"

    if callback != None:
        mags, phases = callback(stackType, startTime, notes, Q, I, fpts, rampHigh, rampLow)

    cache.set(stack_prefix+'mags', mags)
    cache.set(stack_prefix+'phases', phases)

    return stackType, startTime, notes, Q, I, fpts, rampHigh, rampLow, mags, phases

def alazar_nwa_plotter(stackType, startTime, notes, Q, I, fpts, rampHigh, rampLow):

    plt.subplot(121)
    plt.imshow(I, aspect='auto', interpolation='none', origin = 'lower', cmap = 'gist_stern',
           extent = [rampHigh, 2*rampLow-rampHigh , min(fpts), max(fpts)])
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency (Hz)')
    plt.title('alazar nwa I channel')
    plt.colorbar()

    plt.subplot(122)
    plt.imshow(Q, aspect='auto', interpolation='none', origin = 'lower', cmap = 'gist_stern',
           extent = [rampHigh, 2*rampLow-rampHigh, min(fpts), max(fpts)])
    plt.title('alazar nwa Q channel')
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency(Hz)')
    plt.colorbar()

    fig_name = r'./raw figures/{},({},{}), IQ voltage.png'.format(notes[-1][6:9], rampHigh, rampLow)
    dataanalysis.save_styled_fig(fig_name, 'wide')
    plt.show()

    plt.subplot(121)
    mags = np.sqrt(I**2 + Q**2)
    plt.imshow(mags, aspect='auto', interpolation='none', origin = 'lower',
           extent = [rampHigh, 2*rampLow-rampHigh, min(fpts), max(fpts)], cmap = 'YlOrRd')
    plt.title('Magnitude')
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency(Hz)')
    plt.colorbar()


    phases = []
    for Irow, Qrow in zip(I, Q):
        phases.append(map(util.phase, zip(Irow, Qrow)))
    phases = np.array(phases)
    print np.shape(phases)
    plt.subplot(122)
    plt.imshow(phases, aspect='auto', interpolation='none', origin = 'lower',
           extent = [rampHigh, 2*rampLow-rampHigh, min(fpts), max(fpts)], cmap = 'YlOrRd')
    plt.title('phase')
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency(Hz)')
    plt.colorbar()

    fig_name = r'./raw figures/{},({},{}), Mag Phase voltage.png'.format(notes[-1][6:9], rampHigh, rampLow)
    dataanalysis.save_styled_fig(fig_name, 'wide')
    plt.show()

    return mags, phases
