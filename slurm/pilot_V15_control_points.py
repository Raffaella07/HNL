from python.common  import Point,Config,getCtauEff

# List of points to be generated
#   - N.B.: mass must be a float


p = Point(mass=999,ctau=999,vv=999)
cfg = Config(nevtseff=5000,muoneff=1.0e-03,displeff=1.0,timeevt=230,timejob=23,contingency=3.)
#cfg = Config(nevtseff=5,muoneff=1.,displeff=1.0,timeevt=100,timejob=01,contingency=3.)
p.setConfig(cfg)

points = []
points.append(p)








