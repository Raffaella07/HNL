import os

out_dir = 'BHNL_Bc_LHEGEN_v0'

lhe_files = [
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/2MLHE_MuChannel_for2016/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/2MLHE_MuChannel_for2016/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/2MLHE_MuChannel_for2017/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/2MLHE_MuChannel_for2017/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/2MLHE_MuChannel_for2018/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/2MLHE_MuChannel_for2018/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_5/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/0_14/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_5/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/15_29/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_5/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/30_44/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/45_50/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/45_50/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/45_50/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/45_50/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2016/45_50/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_5/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/0_14/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_5/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/15_29/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_10/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_11/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_12/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_13/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_14/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_5/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_6/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_7/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_8/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/30_44/Bcgen_9/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/45_50/Bcgen_0/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/45_50/Bcgen_1/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/45_50/Bcgen_2/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/45_50/Bcgen_3/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/45_50/Bcgen_4/bcvegpy.lhe',
    'root://cms-xrd-global.cern.ch//eos/cms/store/group/phys_bphys/fiorendi/13TeV/BcLHE/50MLHE_for2017/45_50/Bcgen_5/bcvegpy.lhe',
]

events_per_job = -1
njobs = len(lhe_files)


##########################################################################################
##########################################################################################

# make output dir
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
    os.makedirs(out_dir + '/logs')
    os.makedirs(out_dir + '/errs')
# make se output dir
if not os.path.exists('/pnfs/psi.ch/cms/trivcat/store/user/mratti/BHNLsGen/{se_dir}/'.format(se_dir=out_dir)):
    os.makedirs('/pnfs/psi.ch/cms/trivcat/store/user/mratti/BHNLsGen/{se_dir}/'.format(se_dir=out_dir))
            
for ijob in range(njobs):

    # relaunch only some
    #if ijob not in [104,105,106,13,24,57,75,86,87]:
    #  continue

    #input file
    fin = open("../cmsDrivers/BHNL_Bc_LHEtoRoot_TEMPLATE.py", "rt")
    #output file to write the result to
    fout = open("%s/BHNL_Bc_LHEtoRoot_cfg_nj%d.py" %(out_dir, ijob), "wt")
    #for each line in the input file
    for line in fin:
        #read replace the string and write to output file
        if   'HOOK_MAX_EVENTS' in line: fout.write(line.replace('HOOK_MAX_EVENTS' , '%s' %events_per_job))
        elif 'HOOK_FIRST_LUMI' in line: fout.write(line.replace('HOOK_FIRST_LUMI' , '%d' %(ijob+1) ))
        elif 'HOOK_FILE_IN'    in line: fout.write(line.replace('HOOK_FILE_IN'    , lhe_files[ijob] ))
        elif 'HOOK_FILE_OUT'   in line: fout.write(line.replace('HOOK_FILE_OUT'   , '/scratch/mratti/{scratch_dir}/BHNL_Bc_LHEtoRoot_step0_nj{ijob}.root'.format(scratch_dir=out_dir+'_nj%d' %(ijob),ijob=ijob)))
#         elif 'HOOK_SKIP_EVENTS'in line: fout.write(line.replace('HOOK_SKIP_EVENTS', '%d' %(events_per_job*ijob)))
        else: fout.write(line)
    #close input and output files
    fout.close()
    fin.close()

    flauncher = open("%s/submitter_nj%d.sh" %(out_dir, ijob), "wt")
    flauncher.write(
'''#!/bin/bash
cd {dir}
source $VO_CMS_SW_DIR/cmsset_default.sh
shopt -s expand_aliases
cmsenv
mkdir -p /scratch/mratti/{scratch_dir}
ls /scratch/mratti/{scratch_dir}
cmsRun {cfg}
xrdcp /scratch/mratti/{scratch_dir}/BHNL_Bc_LHEtoRoot_step0_nj{ijob}.root root://t3dcachedb.psi.ch:1094///pnfs/psi.ch/cms/trivcat/store/user/mratti/BHNLsGen/{se_dir}/BHNL_Bc_LHEtoRoot_step0_nj{ijob}.root
rm -r /scratch/mratti/{scratch_dir}/
'''.format(dir='/'.join([os.getcwd(), out_dir]), scratch_dir=out_dir+'_nj%d' %(ijob), cfg='BHNL_Bc_LHEtoRoot_cfg_nj%d.py' %(ijob), ijob=ijob, se_dir=out_dir)
    )
    flauncher.close()
    
    command_sh_batch = 'sbatch -p wn --account=t3 -o %s/logs/step0_nj%d.log -e %s/logs/step0_nj%d.log --job-name=%s --time=01:00:00 %s/submitter_nj%d.sh' %(out_dir, ijob, out_dir, ijob, out_dir, out_dir, ijob)

    print(command_sh_batch)
    os.system(command_sh_batch)
    
    
    

