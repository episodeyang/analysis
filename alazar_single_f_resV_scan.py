__author__ = 'Ge Yang'

from analysis_util import indexString
import matplotlib.pyplot as plt
from slab import dataanalysis
import numpy as np
import util

import re
def is_ramp_key(keyString):
    try:
        return re.search(ur'(ramp_\d\d\d)', keyString, re.UNICODE).group() == keyString
    except AttributeError, e:
        return False

def get_alazar_single_f_resV_scan(cache, stack_index, iterator=None, done=None):
    indStr = indexString(stack_index)
    stack_prefix = "stack_" + indStr + '.'

    stackType = cache.get(stack_prefix+'type')
    startTime = cache.get(stack_prefix+'startTime')
    notes = cache.get(stack_prefix+'notes')

    frequency = cache.get(stack_prefix+'frequency')
    # now the cache.index function takes care of the trailing '.' well
    # no need to put the [:-1] there.
    # but I like the explicity of it.
    rampList = filter(is_ramp_key, cache.index(stack_prefix[:-1]))
    print "filtered key list", rampList
    # rampList = ['ramp_000', 'ramp_001', 'ramp_002', 'ramp_003', 'ramp_004', 'ramp_005']
    # Try not to output all the data. Just want to plot each first.
    for rampKey in rampList:
        # mag_stacks[ind].append( cache.get(stack_prefix + rampKey + '.mags') )
        # mags = cache.get(stack_prefix + rampKey + '.mags')
        # phases = cache.get(stack_prefix + rampKey + '.phases')
        I = cache.get(stack_prefix + rampKey + '.I')
        Q = cache.get(stack_prefix + rampKey + '.Q')
        resVs = cache.get(stack_prefix + rampKey + '.resVs')
        rampHighs = cache.get(stack_prefix + rampKey + '.rampHighs')
        rampLows = cache.get(stack_prefix + rampKey + '.rampLows')
        if iterator != None:
            iterator(stackType, startTime, notes, frequency, rampList, I, Q, rampHighs, rampLows, resVs)
    
    if done != None:
        done(stackType, startTime, notes, frequency, rampList, I, Q, rampHighs, rampLows, resVs)

    return stackType, startTime, notes, frequency, I, Q 

def alazar_single_f_resV_scan_plotter(stackType, startTime, notes, frequency, rampList, I, Q, rampHighs, rampLows, resVs):

    rampHigh = rampHighs[0]
    rampLow = rampLows[0]
    plt.subplot(121)
    plt.imshow(I, aspect='auto', interpolation='none', origin = 'lower', cmap = 'gist_stern',
           extent = [rampHigh, 2*rampLow-rampHigh, resVs[0], resVs[-1]])
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('resonator volt')
    plt.title('I @ {:.4f}GHz'.format(float(frequency)/1e9))
    plt.colorbar()

    plt.subplot(122)
    plt.imshow(Q, aspect='auto', interpolation='none', origin = 'lower', cmap = 'gist_stern',
           extent = [rampHigh, 2*rampLow-rampHigh, resVs[0], resVs[-1]])
    plt.title('Q @ {:.4f}GHz'.format(float(frequency)/1e9))
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('resonator volt')
    plt.colorbar()

    fig_name = r'./raw figures/{},({},{}), IQ voltage.png'.format(notes[-1][6:9], rampHigh, rampLow)
    dataanalysis.save_styled_fig(fig_name, 'wide')
    plt.show()

    plt.subplot(121)
    mags = np.sqrt(I**2 + Q**2)
    plt.imshow(mags, aspect='auto', interpolation='none', origin = 'lower',
           extent = [rampHigh, 2*rampLow-rampHigh, resVs[0], resVs[-1]], cmap = 'YlOrRd')
    plt.title('Magnitude @ {:.4f}GHz'.format(float(frequency)/1e9))
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
    plt.xlabel('Trap voltage (V)')
    plt.ylabel('resonator V')
    plt.colorbar()


    phases = []
    for Irow, Qrow in zip(I, Q):
        phases.append(map(util.phase, zip(Irow, Qrow)))
    phases = np.array(phases)
    print np.shape(phases)
    plt.subplot(122)
    phases = np.array(phases)
    print np.shape(phases)
    plt.subplot(122)
    phases = np.array(phases)
    print np.shape(phases)
    plt.subplot(122)
    phases = np.array(phases)
    print np.shape(phases)
    plt.subplot(122)
    plt.imshow(phases, aspect='auto', interpolation='none', origin = 'lower',
           extent = [rampHigh, 2*rampLow-rampHigh, resVs[0], resVs[-1]], cmap = 'YlOrRd')
    plt.title('phase @ {:.4f}GHz'.format(float(frequency)/1e9))
    axes = plt.gca()
    axes.ticklabel_format(style = 'sci', useOffset=False)
