from math import radians

import numpy as np # installed with matplotlib
import matplotlib.pyplot as plt

def main():
    xss = np.arange(0, radians(1800), radians(12))
    plt.plot(xss, np.cos(xss), 'b')
    plt.show()


main()

