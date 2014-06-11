def heterodyne_spectrum(cache, index, callback=None, draw=True, symmetric=False):
    cache.current_stack = stackPrefix(index)
    notes = cache.get('notes')
    ampI = cache.get('amp I')
    ampQ = cache.get('amp Q')
    fStart = cache.get('fStart')
    fEnd = cache.get('fEnd')
    fN = cache.get('fN')
    fpts = cache.get('fpts')
    rampHigh = cache.get('rampHigh')
    rampLow = cache.get('rampLow')
    resV = cache.get('resV')
    startTime = cache.get('startTime')
    try:
        temperature = cache.get('temperature')
        print "temperature: {}".format(temperature)
    except:
        pass
    if callback == None and show:
        heterodyne_spectrum_plotter(index, ampI, ampQ, fStart, fEnd, fN, fpts, rampHigh, rampLow, resV, startTime, symmetric=False)
    else: 
        callback(index, ampI, ampQ, fStart, fEnd, fN, fpts, rampHigh, rampLow, resV, startTime, symmetric=False)
    return ampI, ampQ, fStart, fEnd, fN, fpts, rampHigh, rampLow, resV, startTime

    
def heterodyne_spectrum_plotter(index, ampI, ampQ, fStart, fEnd, fN, fpts, rampHigh, rampLow, resV, startTime, symmetric=False):
    subplot(121, title='amplitude I', xlabel='trap voltage', ylabel='frequency (GHz)')
    if symmetric:
        extent=[rampHigh, 2*rampLow - rampHigh, fStart, fEnd]
    else:
        extent=[rampHigh, rampLow, fStart, fEnd]
    imshow(ampI, aspect='auto', extent=extent, 
           origin='lower', interpolation="none")
    colorbar();
    subplot(122, title='amplitude Q', xlabel='trap voltage', ylabel='frequency (GHz)')
    imshow(ampQ, aspect='auto', extent=extent, 
           origin='lower', interpolation="none")
    colorbar();
