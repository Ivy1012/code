#!/usr/bin/env python

# Documentation of 'plotfile' see -
# http://matplotlib.org/api/pyplot_api.html#module-matplotlib.pyplot

# This script is used to plot the data generated by - 'test_airsea'

from pylab import plotfile, show, gca, savefig

fname="fort.200"
plotfile(fname, (0, 1, 2,), delimiter=' ',subplots=False)
gca().set_xlabel(r'Wind speed')
gca().set_title(r'Momentum bulk transfer coefficient')
savefig('cdd.png')
show()

plotfile(fname, (0, 3, 4,), delimiter=' ',subplots=False)
gca().set_xlabel(r'Wind speed')
gca().set_title(r'Latent heat bulk transfer coefficient')
savefig('ced.png')
show()

plotfile(fname, (0, 5, 6,), delimiter=' ',subplots=False)
gca().set_xlabel(r'Wind speed')
gca().set_title(r'Sensible heat bulk transfer coefficient')
savefig('chd.png')
show()

plotfile(fname, (0, 1, 3, 5,), delimiter=' ',subplots=False)
gca().set_xlabel(r'Wind speed')
gca().set_title(r'Kondo- compare with Fig.5')
savefig('kondo.png')
show()

plotfile(fname, (0, 2, 4, 6,), delimiter=' ',subplots=False)
gca().set_xlabel(r'Wind speed')
gca().set_title(r'Fairall')
savefig('fairall.png')
show()