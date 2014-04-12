__author__ = 'Ge Yang'

def indexString(ind, width=5):
    return str(10**width+ind)[-width:]

def checkType(typeString, stackType):
    if typeString == stackType[:len(typeString)]:
        return True
    else:
        return False
