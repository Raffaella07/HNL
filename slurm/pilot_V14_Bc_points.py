from python.common  import Point,Config,getCtauEff

# List of points to be generated
#   - N.B.: mass must be a float

m_vv_s = [
(2.0,8.0e-05),

(3.0,1.0e-05),
(3.0,4.0e-04),

(4.5,2.0e-04),
(4.5,6.0e-03),

(5.5,1.0e-03),
(5.5,3.0e-02),
]

muonEff = {}
muonEff[2.0]=0.001
muonEff[3.0]=0.004
muonEff[4.5]=0.0005
muonEff[5.5]=0.0003

displEff = {}
displEff[2.0]=0.5
displEff[3.0]=0.5
displEff[4.5]=1.0
displEff[5.5]=1.0


points = []
for m,vv in m_vv_s:
  p   = Point(mass=m,ctau=None,vv=vv,ismaj=True)
  cfg = Config(nevtseff=15,muoneff=muonEff[m],displeff=displEff[m],timeevt=1000,timejob=14,contingency=3.)
  p.setConfig(cfg)
  points.append(p)

  # 

  #print('mass={:.1f} vv={:.1e} before={:.1e}, after={:.1e}'.format(p.mass,p.vv,displEff[m][vv],getCtauEff(p.ctau*4.,1000.))) # 4 is the assumed beta*gamma factor...
  #cfg.stamp()
  







