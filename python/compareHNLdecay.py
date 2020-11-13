from decays import *
from common import *

import matplotlib.pyplot as plt



masses = [0.5+i*0.1 for i in range(0,60) ] # GeV

ctaus_peskin_lep = [ctau_from_gamma(gamma_lep(mass=m,vv=1)) for m in masses] 
ctaus_peskin_had = [ctau_from_gamma(gamma_had(mass=m,vv=1)) for m in masses]   
ctaus_peskin_neu = [ctau_from_gamma(gamma_neu(mass=m,vv=1)) for m in masses]   
ctaus_peskin_tot = [ctau_from_gamma(gamma_total(mass=m,vv=1)) for m in masses]    

ctaus_peskin = [ctaus_peskin_lep, ctaus_peskin_had, ctaus_peskin_neu, ctaus_peskin_tot]

decays = [HNLDecays(m,1.) for m in masses]

# factor 2 is because Peskin considers Majorana
ctaus_bondarenko_lep = [ctau_from_gamma(2*decays[im].decay_rate['tot_lep']) for im,m in enumerate(masses)]
ctaus_bondarenko_had = [ctau_from_gamma(2*decays[im].decay_rate['tot_had']) for im,m in enumerate(masses)]
ctaus_bondarenko_neu = [ctau_from_gamma(2*decays[im].decay_rate['tot_neu']) for im,m in enumerate(masses)]
ctaus_bondarenko_tot = [ctau_from_gamma(2*decays[im].decay_rate['tot']    ) for im,m in enumerate(masses)]

ctaus_bondarenko = [ctaus_bondarenko_lep, ctaus_bondarenko_had, ctaus_bondarenko_neu, ctaus_bondarenko_tot]

labels = ['Leptonic', 'Hadronic', 'Neutrinos', 'Total']

fig, axes = plt.subplots(1, 4, figsize=(5.5*4, 5))
for i,ax in enumerate(axes):
  ax.plot(masses, ctaus_peskin[i], 'b', label='{} (Peskin)'.format(labels[i]))
  ax.plot(masses, ctaus_bondarenko[i], 'r', label='{} (Bondarenko)'.format(labels[i]))
  ax.set_ylabel('c$\\tau$ (mm)')
  ax.set_xlabel('HNL mass (GeV)')
  ax.legend(loc='upper right', frameon=True) 
  ax.grid(which='both', axis='both')
  ax.set_yscale('log')
 
fig.savefig('HNLlifetime_check_log.pdf')
fig.savefig('HNLlifetime_check_log.png')

fig, axes = plt.subplots(1, 4, figsize=(5.5*4, 5))
for i,ax in enumerate(axes):
  ax.plot(masses, ctaus_peskin[i], 'b', label='{} (Peskin)'.format(labels[i]))
  ax.plot(masses, ctaus_bondarenko[i], 'r', label='{} (Bondarenko)'.format(labels[i]))
  ax.set_ylabel('c$\\tau$ (mm)')
  ax.set_xlabel('HNL mass (GeV)')
  ax.legend(loc='upper right', frameon=True) 
  ax.grid(which='both', axis='both')
  #ax.set_yscale('log')
 
fig.savefig('HNLlifetime_check_lin.pdf')
fig.savefig('HNLlifetime_check_lin.png')


# ratio
ctaus_ratios = []
for pes,bon in zip(ctaus_peskin,ctaus_bondarenko):
  ctaus_ratio = []
  for im,mass in enumerate(masses):
    ctaus_ratio.append(pes[im]/bon[im])
  ctaus_ratios.append(ctaus_ratio)

fig, axes = plt.subplots(1, 4, figsize=(5.5*4, 5))
for i,ax in enumerate(axes):
  ax.plot(masses, ctaus_ratios[i], 'r', label='{}'.format(labels[i]))
  ax.set_ylabel('Ratio of c$\\tau$ (mm)')
  ax.set_xlabel('HNL mass (GeV)')
  ax.set_ylim(0.4,1.4)
  ax.legend(loc='upper right', frameon=True) 
  ax.grid(which='both', axis='both')
  #ax.set_yscale('log')
fig.suptitle('Ratio Peskin/Bondarenko', fontsize=14) 
fig.savefig('HNLlifetime_ratio_lin.pdf')
fig.savefig('HNLlifetime_ratio_lin.png')

# figure 12 right of Bondarenko, ratio between quarks, leptons, neutrinos
gammas_bondarenko_lep = [2*decays[im].decay_rate['tot_lep'] for im,m in enumerate(masses)]
gammas_bondarenko_had = [2*decays[im].decay_rate['tot_had'] for im,m in enumerate(masses)]
gammas_bondarenko_neu = [2*decays[im].decay_rate['tot_neu'] for im,m in enumerate(masses)]
gammas_bondarenko_tot = [2*decays[im].decay_rate['tot']     for im,m in enumerate(masses)]

gammas_bondarenko_lepFrac = [x_lep / x_tot for x_lep,x_tot in zip(gammas_bondarenko_lep,gammas_bondarenko_tot)]
gammas_bondarenko_hadFrac = [x_had / x_tot for x_had,x_tot in zip(gammas_bondarenko_had,gammas_bondarenko_tot)]
gammas_bondarenko_neuFrac = [x_neu / x_tot for x_neu,x_tot in zip(gammas_bondarenko_neu,gammas_bondarenko_tot)]

fig, ax = plt.subplots(1, 1, figsize=(5.5*1, 5))
ax.plot(masses, gammas_bondarenko_lepFrac, 'r', label='leptons')
ax.plot(masses, gammas_bondarenko_hadFrac, 'b',  label='quarks')
ax.plot(masses, gammas_bondarenko_neuFrac, 'g',  label='neutrinos')
ax.set_ylabel('BR')
ax.set_xlabel('HNL mass (GeV)')
ax.set_ylim(0.1,1.0)
ax.set_xlim(1,5)
ax.set_yticks([0.1,0.2,0.4,0.6,0.8,1.0], minor=True)
ax.legend(loc='center right', frameon=True) 
ax.grid(which='both', axis='both')
ax.set_yscale('log')
ax.set_xscale('log')

fig.savefig('HNL_BR_bon_log.pdf')
fig.savefig('HNL_BR_bon_log.png')

# lifetime figure
taus_bondarenko_tot = [ctau / const_c * 0.001 for ctau in ctaus_bondarenko_tot ]

fig, ax = plt.subplots(1, 1, figsize=(5.5*1, 5))
ax.plot(masses, taus_bondarenko_tot, 'r', label='$V_e=V_{\\tau}=0$')
ax.set_ylabel('$\\tau$ (s) ')
ax.set_xlabel('HNL mass (GeV)')
ax.set_ylim(1e-16,1e-04)
ax.set_xlim(0.05,5)
#ax.set_yticks([0.1,0.2,0.4,0.6,0.8,1.0], minor=True)
ax.legend(loc='center right', frameon=False) 
ax.grid(which='both', axis='both')
ax.set_yscale('log')
ax.set_xscale('log')

fig.savefig('HNL_tau_bon_log.pdf')
fig.savefig('HNL_tau_bon_log.png')


