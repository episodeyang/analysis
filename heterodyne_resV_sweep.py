def heterodyne_resV_sweep(cache, index, callback=None, draw=True, extent=[None, None], symmetric=False):
    cache.current_stack = stackPrefix(index)
    notes = cache.get('notes')
    ampI = cache.get('amp I')
    ampQ = cache.get('amp Q')
    offsetFrequency = cache.get('offset_frequency')
    resVs = cache.get('resVs')
    IF = cache.get('IF')
    startTime = cache.get('startTime')
    try:
        temperature = cache.get('temperature')
        print "temperature: {}".format(temperature)
    except:
        pass
    try: peakFs = cache.get('peakFs')
    except: pass
    
    RFs = cache.get('RFs')
    
    try:
        rampHigh = cache.get('rampHigh')
        rampLow = cache.get('rampLow')

        if callback == None and draw==True:
            heterodyne_resV_sweep_plotter(index, ampI, ampQ, offsetFrequency, rampHigh, rampLow, resVs, startTime, symmetric=symmetric)
        elif callback !=None : 
            callback(index, ampI, ampQ, offsetFrequency, rampHigh, rampLow, resVs, startTime, symmetric=symmetric)
        return ampI, ampQ, offsetFrequency, RFs, rampHigh, rampLow, resVs, startTime, peakFs

    except:
        rampHighs = cache.get('rampHighs')
        rampLows = cache.get('rampLows')
        if callback == None and draw==True:
            heterodyne_resV_sweep_plotter(index, ampI[extent[0]: extent[1]], ampQ[extent[0]: extent[1]], 
                                          offsetFrequency, rampHighs, rampLows, resVs, startTime, symmetric=symmetric)
        elif callback !=None : 
            callback(index, ampI, ampQ, offsetFrequency, rampHighs, rampLows, resVs, startTime, symmetric=symmetric)
        return ampI, ampQ, offsetFrequency, RFs, rampHighs, rampLows, resVs, startTime, peakFs
    
def heterodyne_resV_sweep_plotter(index, ampI, ampQ, offsetFrequency, rampHigh, rampLow, resVs, 
                                  startTime, cmap='jet', symmetric=False, titles=['amplitude I','amplitude II']):
    try:
        rampHigh = rampHigh[-1]
        rampLow = rampLow[-1]
    except: 
        pass
    if symmetric:
        extent=[rampHigh, 2*rampLow - rampHigh, resVs[-1], resVs[0]]
    else:
        extent=[rampHigh, rampLow, resVs[-1], resVs[0]]
    subplot(122, title=titles[1], xlabel='trap voltage (V)', ylabel='resonator votage (V)')
    imshow(ampQ, aspect='auto', extent=extent, 
           origin='upper', interpolation="none", cmap=cmap)
    colorbar();
    subplot(121, title=titles[0], xlabel='trap voltage (V)', ylabel='resonator voltage (V)')
    imshow(ampI, aspect='auto', extent=extent, 
           origin='upper', interpolation="none", cmap=cmap)
    colorbar();