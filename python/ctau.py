
from common import getCtau

import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import matplotlib.colors as colors
import numpy as np


masses = np.array( [float('{:.2f}'.format(0.5+i*0.1)) for i in range(0,56) ] )# GeV
#masses = np.logspace( np.log10(0.5), np.log10(6.0),  56, base=10)
#vvs = np.logspace( np.log10(1e-06), np.log10(3e-04), 50, base=10)
vvs = np.logspace( np.log10(1e-06), np.log10(1), 100, base=10)

ctaus = []
for vv in vvs:
  ctaus_m = []
  for m in masses:
    ctaus_m.append(getCtau(m,vv)/1000)
  ctaus.append(ctaus_m)

ctaus = np.array(ctaus)
masses, vvs = np.meshgrid(masses, vvs)

fig, ax0 = plt.subplots()
pcm = ax0.pcolor(masses, vvs, ctaus,
                   norm=colors.LogNorm(vmin=ctaus.min(), vmax=ctaus.max()),
                   cmap='PiYG_r')
cbar = fig.colorbar(pcm, ax=ax0, extend='max')
cbar.set_label('c$\\tau$ (m)')
CS = ax0.contour(masses, vvs, ctaus, levels=np.array([0.001, 0.01, 0.1, 0.2, 0.4, 0.6, 0.8, 1., 2.]))
ax0.clabel(CS, inline=1, fontsize=10)
ax0.set_xlabel('mass (GeV)')
ax0.set_ylabel('$V^2$')
ax0.set_ylim(1e-06,1.)
#ax0.set_ylim(1e-06,3e-04)
ax0.set_xlim(0.5,6)
#ax0.set_xlim(0.5,6)
ax0.set_yscale('log')
ax0.set_xscale('log')
ax0.grid(which='both', axis='both')

fig.savefig('ctau.pdf')



