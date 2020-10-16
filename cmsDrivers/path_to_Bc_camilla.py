# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/BPH-RunIISummer19UL18pLHEGEN-00004-fragment.py --filein lhe:aaa.lhe.gz --fileout file:BPH-RunIISummer19UL18pLHEGEN-00004_step1.root --mc --eventcontent LHE --datatier LHE --conditions 106X_upgrade2018_realistic_v4 --step NONE --era Run2_2018 --python_filename BPH-RunIISummer19UL18pLHEGEN-00004_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('LHE',Run2_2018)

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("LHESource",
    fileNames = cms.untracked.vstring(
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_0.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_1.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_2.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_3.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_4.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_5.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_6.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_7.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_8.lhe.xz',
#         'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M/bcvegpy_200k_9.lhe.xz',

        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_0.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_1.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_2.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_3.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_4.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_5.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_6.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_7.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_8.lhe.xz',
        'gsiftp://storage01.lcg.cscs.ch//pnfs/lcg.cscs.ch/cms/trivcat/store/user/cgalloni/Bc_LHE_2M_noPtcut/bcvegpy_200k_9.lhe.xz',
    )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/BPH-RunIISummer19UL18pLHEGEN-00004-fragment.py nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('LHE'),
        filterName = cms.untracked.string('')
    ),
#     fileName = cms.untracked.string('file:BPH-RunIISummer19UL18pLHEGEN-00004_step1_with_gen_cuts.root'),
    fileName = cms.untracked.string('file:BPH-RunIISummer19UL18pLHEGEN-00004_step1_without_gen_cuts.root'),
    outputCommands = process.LHEEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v4', '')

# Path and EndPath definitions
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.LHEoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

