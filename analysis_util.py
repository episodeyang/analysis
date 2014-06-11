__author__ = 'Ge Yang'

import numpy as np
import matplotlib.pyplot as plt


def indexString(ind, width=5):
    return str(10 ** width + ind)[-width:]


def stackPrefix(ind, prefix='stack'):
    return prefix + '_' + indexString(ind)


def checkType(typeString, stackType):
    if typeString == stackType[:len(typeString)]:
        return True
    else:
        return False


def img_log(img):
    return map(lambda img_row: np.log10(img_row), img)


def subtract_background(img, center=False):
    if center:
        return map(lambda img_row: img_row - img_row[len(img_row) / 2], img)
    else:
        return map(lambda img_row: img_row - img_row[-1], img)

def normalize_background(img, avg=20, center=False):
    if center:
        return map(lambda img_row: img_row / np.mean(img_row[len(img_row) / 2 - avg / 2:len(img_row) / 2 + avg / 2]), img)
    else: 
        return map(lambda img_row: img_row / np.mean(img_row[-avg:]), img)



if __name__ == "__main__":
    # test img_log function
    img = np.outer(np.arange(0, 100), np.ones(50))
    plt.imshow(img_log(img))
    plt.colorbar()
    plt.show()
