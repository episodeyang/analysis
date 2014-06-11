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

    try:
        resV = cache.get(stack_prefix + 'resV')
    except:
        print 'resV does not exist in stack. Retrieving from notes'
        print notes
        resV = notes[-1][6:9]

    if callback != None:
        mags, phases = callback(stack_index, stackType, startTime, notes, Q, I, fpts, rampHigh, rampLow, resV)
    try:
        mags = cache.get(stack_prefix+'mags')
    except:
        cache.set(stack_prefix+'mags', mags)
    try:
        phases = cache.get(stack_prefix+'phases')
    except:
        cache.set(stack_prefix+'phases', phases)

    return stackType, startTime, notes, Q, I, fpts, rampHigh, rampLow, mags, phases, resV

def alazar_nwa_plotter(stack_index, stackType, startTime, notes, Q, I, fpts, rampHigh, rampLow, resV):

    resV = float(resV)

    plt.subplot(121)
    plt.imshow(I, aspect='auto', interpolation='none', origin = 'lower', cmap = 'gist_stern',
           extent = [rampHigh, 2*rampLow-rampHigh , min(fpts), max(fpts)])
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency (Hz)')
    plt.title('alazar I @{:.3f}V'.format(resV))
    plt.colorbar()

    plt.subplot(122)
    plt.imshow(Q, aspect='auto', interpolation='none', origin = 'lower', cmap = 'gist_stern',
           extent = [rampHigh, 2*rampLow-rampHigh, min(fpts), max(fpts)])
    plt.title('alazar Q @{:.3f}V'.format(resV))
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency(Hz)')
    plt.colorbar()

    fig_name = r'./raw figures/{}_{},({},{}), IQ voltage.png'.format(stack_index, resV, rampHigh, rampLow)
    dataanalysis.save_styled_fig(fig_name, 'r2')
    plt.show()

    plt.subplot(121)
    mags = np.sqrt(I**2 + Q**2)
    plt.imshow(mags, aspect='auto', interpolation='none', origin = 'lower',
           extent = [rampHigh, 2*rampLow-rampHigh, min(fpts), max(fpts)], cmap = 'YlOrRd')
    plt.title('Magnitude @{:.3f}V'.format(resV))
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
    plt.title('Phase @{:.3f}V'.format(resV))
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('Frequency(Hz)')
    plt.colorbar()

    fig_name = r'./raw figures/{}_{},({},{}), Mag Phase voltage.png'.format(stack_index, resV, rampHigh, rampLow)
    dataanalysis.save_styled_fig(fig_name, 'r2')
    plt.show()

    return mags, phases
