from python.common  import Point,Config

# List of points to be generated
#   - N.B.: mass must be a float

m_vv_s = [
(0.5,1.0e-06),
(0.5,4.5e-06),
(0.5,1.8e-05),
(0.5,7.0e-05),
#(0.5,3.0e-04),

(1.0,1.0e-06),
(1.0,4.5e-06),
(1.0,1.8e-05),
(1.0,7.0e-05),
#(1.0,3.0e-04),

(1.5,1.0e-06),
(1.5,4.5e-06),
(1.5,1.8e-05),
(1.5,7.0e-05),
#(1.5,3.0e-04),

(2.0,1.0e-06),
(2.0,4.5e-06),
(2.0,1.8e-05),
(2.0,7.0e-05),
#(2.0,3.0e-04),

#(3.0,1.0e-06),
(3.0,4.5e-06),
(3.0,1.8e-05),
(3.0,7.0e-05),
(3.0,3.0e-04),

#(4.5,1.0e-06),
(4.5,4.5e-06),
(4.5,1.8e-05),
(4.5,7.0e-05),
(4.5,3.0e-04),

#(6.0,1.0e-06),
#(6.0,4.5e-06),
#(6.0,1.8e-05),
#(6.0,7.0e-05),
#(6.0,3.0e-04),
]

muonEff = {}
muonEff[0.5] = 1e-03 
muonEff[1.0] = 1e-03
muonEff[1.5] = 1e-03 # 0.008
muonEff[2.0] = 5e-04 # 0.004  
muonEff[3.0] = 7e-03 # 0.024
muonEff[4.5] = 1e-04 # guess
muonEff[6.0] = 1e-04 # guess 

displEff = {}
displEff[0.5]={}
displEff[1.0]={}
displEff[1.5]={}
displEff[2.0]={}
displEff[3.0]={}
displEff[4.5]={}
displEff[6.0]={}

displEff[1.0][1.0e-06] = 0.00075182481402 / 20.
displEff[1.0][4.5e-06] = 0.00225267581546 / 10.
displEff[1.0][1.8e-05] = 0.0148611200403  / 5.
displEff[1.0][7.0e-05] = 0.0504638517648
displEff[1.0][3.0e-04] = 0.190128020373

displEff[2.0][1.0e-06] = 0.0251267971351 / 10.
displEff[2.0][4.5e-06] = 0.0718707550494 / 5.
displEff[2.0][1.8e-05] = 0.34741875426
displEff[2.0][7.0e-05] = 0.691271749982
displEff[2.0][3.0e-04] = 0.935873464042

displEff[3.0][1.0e-06] = 0.215505500588
displEff[3.0][4.5e-06] = 0.495083845539
displEff[3.0][1.8e-05] = 0.939304719095
displEff[3.0][7.0e-05] = 0.966696317468
displEff[3.0][3.0e-04] = 0.966696317468

displEff[4.5] = displEff[3.0]
displEff[6.0] = displEff[3.0]

displEff[1.5] = displEff[1.0]
for k,v in displEff[1.0].items():
  displEff[0.5][k]=v/30. 

points = []
for m,vv in m_vv_s:
  p   = Point(mass=m,ctau=None,vv=vv,ismaj=True)
  eff = displEff[m][vv] * muonEff[m]
  cfg = Config(nevtseff=10,filtereff=eff,timeevt=1000,timejob=60,contingency=3.)
  #cfg = Config(nevtseff=100,filtereff=eff,timeevt=100,timejob=01,contingency=1.5)
  p.setConfig(cfg)
  points.append(p)

  #p.stamp_simpli()
  #cfg.stamp()
  




