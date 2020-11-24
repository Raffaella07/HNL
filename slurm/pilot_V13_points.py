from python.common  import Point,Config

# List of points to be generated
#   - N.B.: mass must be a float

points_cfgs = [
# just to test the lowest filter efficiencies and see how long it takes to generate
[Point(mass=1.0,ctau=None,vv=1.0e-06,ismaj=True), Config(nevts_eff=1000,filter_eff=0.05,time_evt=80,time_job=04,contingency=1.5)],
[Point(mass=1.5,ctau=None,vv=1.0e-06,ismaj=True), Config(nevts_eff=1000,filter_eff=0.05,time_evt=80,time_job=04,contingency=1.5)],   
#Point(mass=2.0,ctau=None,vv=1.0e-06,ismaj=True),
#Point(mass=3.0,ctau=None,vv=1.0e-06,ismaj=True),
#Point(mass=4.5,ctau=None,vv=1.0e-06,ismaj=True),
#Point(mass=6.5,ctau=None,vv=1.0e-06,ismaj=True),
]

points = []
for p,cfg in points_cfgs: 
  p.setConfig(cfg)
  points.append(p)

  p.stamp()
  cfg.stamp()


#for p in points:
#  p.stamp()




