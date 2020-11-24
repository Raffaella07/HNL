from decays import HNLDecays

import numpy as np
import math
from scipy.stats import expon  

# constants 
const_pi = math.pi
const_hbar = 6.582119569e-22 * 1e-03 # GeV s  # from http://pdg.lbl.gov/2020/reviews/rpp2020-rev-phys-constants.pdf
const_c = 299792458. # m / s                  # from http://pdg.lbl.gov/2020/reviews/rpp2020-rev-phys-constants.pdf


def ctau_from_gamma(gamma):
    tau_natural = 1. / gamma                  # 1/GeV
    tau = tau_natural * const_hbar            # s
    ctau = tau * const_c * 1000               # mm
    return ctau

def gamma_total(mass,vv):
    '''
    Total width for N (Dirac)
    '''
    gamma_total =  HNLDecays(mass=mass,mixing_angle_square=vv).decay_rate['tot']   # GeV
    return gamma_total

def gamma_partial(mass,vv):
    '''
    Partial width for N->mupi (Dirac)
    '''
    gamma_partial = HNLDecays(mass=mass,mixing_angle_square=vv).decay_rate['mupi'] # GeV
    return gamma_partial

def BR_HNLmupion(mass): # vv is irrelevant, as it cancels out in the ratio
    return gamma_partial(mass=mass,vv=1.)/gamma_total(mass=mass,vv=1.)

def getCtau(mass=-99,vv=-99,ismaj=True):
    '''
    Helper function to go from vv,m -> ctau
    '''
    mult = 2. if ismaj else 1.
    return ctau_from_gamma(mult*gamma_total(mass=mass,vv=vv))

def getVV(mass=-99.,ctau=-99.,ismaj=True):
    '''
    Helper function to go from ctau,m -> vv
    '''
    mult = 2. if ismaj else 1.
    ref_m = 1. # GeV
    ref_vv = 1. 
    ref_ctau = ctau_from_gamma(mult*gamma_total(mass=ref_m,vv=ref_vv))

    k = ref_ctau * np.power(ref_m,5) * ref_vv

    return k/(np.power(mass, 5) * ctau)
   



class Point(object):
  '''
  Class that contains information on mass,ctau,vv of a given signal point
  '''
  def __init__(self,mass,ctau=None,vv=None,isrw=False,orig_vv=None,ismaj=True):
    self.mass = mass
    self.isrw = isrw
    self.ismaj = ismaj

    if not vv: 
      self.ctau=ctau 
      self.vv=getVV(mass=self.mass, ctau=self.ctau, ismaj=self.ismaj)
    if not ctau:
      self.vv = vv
      self.ctau=getCtau(mass=self.mass, vv=self.vv, ismaj=self.ismaj)

    if self.isrw:
      self.orig_vv = orig_vv
      self.orig_ctau = getCtau(mass=self.mass,vv=orig_vv, ismaj=self.ismaj)
    else:
      self.orig_vv = self.vv 
      self.orig_ctau = self.ctau

  #def getExpMedian():
    rv = expon(scale=self.ctau) 
    self.median = rv.median()
    #return rv.mean(),rv.median()

  def stamp(self):
    attrs=[]
    for k,v in self.__dict__.items():
      attrs.append(' {}={} '.format(k,v))
    attrs=' '.join(attrs)
    print(attrs)

  def stamp_simpli(self):
    attrs=[]
    #attrs.append('{}'.format(self.mass))
    attrs.append('{}'.format(self.vv))
    attrs.append('{}'.format(self.ctau))
    attrs.append('{}'.format(self.median))
    attrs=' '.join(attrs)
    return attrs

if __name__ == "__main__":
  import matplotlib.pyplot as plt

  # test old vs new relation 
  mass = 1.0

  vvs = [5e-03, 1e-03, 5e-04, 1e-04, 5e-05, 1e-05, 5e-06, 1e-06, 5e-07]

