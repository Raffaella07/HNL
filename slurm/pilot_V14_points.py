from python.common  import Point,Config,getCtauEff

# List of points to be generated
#   - N.B.: mass must be a float

m_vv_s = [
(0.5,1.0e-01),

(1.0,3.0e-03),

(1.5,3.0e-04),

(2.0,8.0e-05),

(3.0,1.0e-05),
(3.0,4.0e-04),

(4.5,2.0e-04),
(4.5,6.0e-03),

#(5.5,1.0e-03),
#(5.5,3.0e-02),
]

muonEff = {}
muonEff[0.5]=6.00e-03 #0.01
muonEff[1.0]=3.33e-03 #0.005
muonEff[1.5]=2.00e-03 #0.003
muonEff[2.0]=5.67e-04 #0.001
muonEff[3.0]=4.67e-03 #0.004
muonEff[4.5]=4.80e-04 #0.0003
#muonEff[5.5]=#0.0003


displEff = {}
displEff[0.5]=1.0 #0.5
displEff[1.0]=1.0 #0.5
displEff[1.5]=1.0 #0.5
displEff[2.0]=1.0 #0.5
displEff[3.0]=1.0 #0.5
displEff[4.5]=1.0 #1.0
#displEff[5.5]=1.0 #1.0

m_vv_eff_time_s = [
(0.5,1.0e-01,6.0e-03,104),
(1.0,3.0e-03,3.3e-03,160),
(1.5,3.0e-04,2.0e-03,216),
(2.0,8.0e-05,5.7e-04,435),
(3.0,1.0e-05,4.7e-03,149),
(3.0,4.0e-04,5.6e-03,107),
(4.5,2.0e-04,4.8e-04,700),
(4.5,6.0e-03,4.8e-04,700),
]

points = []
for m,vv in m_vv_s:
  p   = Point(mass=m,ctau=None,vv=vv,ismaj=True)
  cfg = Config(nevtseff=15,muoneff=muonEff[m],displeff=displEff[m],timeevt=1000,timejob=14,contingency=3.)
  p.setConfig(cfg)
  points.append(p)

  # 

  #print('mass={:.1f} vv={:.1e} before={:.1e}, after={:.1e}'.format(p.mass,p.vv,displEff[m][vv],getCtauEff(p.ctau*4.,1000.))) # 4 is the assumed beta*gamma factor...
  #cfg.stamp()
  







