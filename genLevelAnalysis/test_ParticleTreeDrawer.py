
import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('analysis')
# define the defaults here, changed from command line
options.maxEvents = 100
#options.inputFiles = 'file:/work/mratti/GEN_HNL/CMSSW_10_2_3/src/HNLsGen/genFiles/March19_BPH-test.root'
#options.inputFiles = 'file:/pnfs/psi.ch/cms/trivcat/store/user/mratti/BHNLsGen/testIncl_n3000_njt1/mass1.5_ctau51.922757246/step1_nj1.root'
#options.inputFiles = 'file:/work/mratti/GEN_HNL_newPythia/CMSSW_10_2_3/src/HNLsGen/slurm/testManyChan_n100_njt1/BPH-step1_numEvent1000.root'
#options.inputFiles = 'file:/work/mratti/GEN_HNL_newPythia/CMSSW_10_2_3/src/HNLsGen/slurm/testBc_n10_njt1/BPH-step1_numEvent1000.root'
#options.inputFiles = 'file:/work/mratti/GEN_HNL_newPythia/CMSSW_10_2_3/src/HNLsGen/slurm/testDmesons_n20_njt1/BPH-step1_numEvent20.root'
options.inputFiles = 'file:/pnfs/psi.ch/cms/trivcat/store/user/mratti/BHNLsGen/testControl/mass999_ctau999/step1_nj1.root'
options.parseArguments()
print options

process = cms.Process("testParticle")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.printTree1 = cms.EDAnalyzer("ParticleListDrawer",
    src = cms.InputTag("genParticles"),
    maxEventsToPrint  = cms.untracked.int32(3)
)

process.printTree2 = cms.EDAnalyzer("ParticleTreeDrawer",
    src = cms.InputTag("genParticles"),
    printP4 = cms.untracked.bool(False),
    printPtEtaPhi = cms.untracked.bool(False),
    printVertex = cms.untracked.bool(False),
    printStatus = cms.untracked.bool(True),
    printIndex  = cms.untracked.bool(True)
)

process.printEventNumber = cms.OutputModule("AsciiOutputModule")

process.p = cms.Path(process.printTree1*process.printTree2)
#process.p = cms.Path(process.printTree1)
process.outpath = cms.EndPath(process.printEventNumber)
process.MessageLogger.destinations = cms.untracked.vstring('cout','cerr')


