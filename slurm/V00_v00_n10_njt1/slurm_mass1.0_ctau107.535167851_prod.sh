#!/bin/bash
#export SCRAM_ARCH=slc7_amd64_gcc700
#cd /CMSSW_10_2_15/src/
#eval `scramv1 runtime -sh`
export CMSSW_SEARCH_PATH=$CMSSW_SEARCH_PATH:$PWD
#SBATCH -J prod_m1.0_ctau107.535167851
#SBATCH -o logs/prod_mass1.0_ctau107.535167851_%a.log
#SBATCH -e logs/prod_mass1.0_ctau107.535167851_%a.log
#SBATCH -p wn
#SBATCH -t 08:00:00
#SBATCH --mem 3500
#SBATCH --array=1-1
#SBATCH --ntasks=1
#SBATCH --account=t3

#DIRNAME="V00_v00_n10_njt1"/mass1.0_ctau107.535167851/
#STARTDIR=$CMSSW_BASE/src/HNLsGen/
#TOPWORKDIR="/scratch/ratramon/"
#JOBDIR="gen_${SLURM_JOB_ID}_${1}"
#WORKDIR=$TOPWORKDIR/$JOBDIR
#INSEPREFIX="root://t3dcachedb.psi.ch:1094/"
#OUTSEPREFIX="root://t3dcachedb.psi.ch:1094/"
#SERESULTDIR="/pnfs/psi.ch/cms/trivcat/store/user/ratramon/BHNLsGen/"$DIRNAME
#source $VO_CMS_SW_DIR/cmsset_default.sh
#shopt -s expand_aliases
#echo ""
#echo "Going to set up cms environment"
#cd $STARTDIR
#cmsenv
#echo ""
#
#echo "Going to create work dir"
#mkdir -p $WORKDIR
#echo "workdir: "
#echo $WORKDIR
#echo ""
#
#echo "Going to create the output dir"
#echo "May give an error if the directory already exists, which can be ignored"
#xrdfs $T3CACHE mkdir -p $SERESULTDIR
#echo ""
#
#echo "Going to copy cmsdriver to work dir"
#cp $STARTDIR/slurm/V00_v00_n10_njt1/step1.py $WORKDIR/. 
#echo ""
#
#cd $WORKDIR
#pwd
echo "Going to run step1"
DATE_START_step1=`date +%s`
cmsRun BPH_mod_BtoDMuN_NtoE_cfg.py maxEvents=10 nThr=1 mass=1.0 ctau=107.535167851 outputFile=BPH-step1.root seedOffset=$1 
DATE_END_step1=`date +%s`
if [ $? -eq 0 ]; then echo "Successfully run step 1"; else exit $?; fi
echo "Finished running step1"
ls
#echo "Content of current directory"
#ls -al
#echo ""

#echo "Going to copy output to result directory"
#xrdcp -f $WORKDIR/BPH-step1_numEvent10.root $OUTSEPREFIX/$SERESULTDIR/step1_nj$1".root"
#if [ $? -eq 0 ]; then echo "Successfully copied step1 file"; else exit $?; fi


### step2 ###
#echo "Going to copy cmsdriver to work dir"
#cp $STARTDIR/slurm/V00_v00_n10_njt1/step2.py $WORKDIR/. 
#echo "Copying pileup profile file to work dir"
#cp /afs/cern.ch/work/r/ratramon/HNL/CMSSW_10_2_15/src/HNLsGen/data/pileup_2018.root .
#echo "Going to run step2"
DATE_START_step2=`date +%s`
cmsRun step2.py randomizePremix=1 nPremixFiles=20 nThr=1 inputFile=BPH-step1_numEvent10.root outputFile=BPH-step2.root seedOffset=$1
DATE_END_step2=`date +%s`
if [ $? -eq 0 ]; then echo "Successfully run step"; else exit $?; fi
echo "Finished running step2"
#echo "Content of current directory"
#ls -al
#echo ""
#RUNTIME_step2=$((DATE_END_step2-DATE_START_step2))
#echo "Intermediate wallclock running time step2: $RUNTIME_step2 s"


### step3 ###
#echo "Going to copy cmsdriver to work dir"
#cp $STARTDIR/slurm/V00_v00_n10_njt1/step3.py $WORKDIR/. 
#echo "Copying pileup profile file to work dir"
#cp $STARTDIR/data/pileup_2018.root $WORKDIR/.
#echo "Going to run step3"
DATE_START_step3=`date +%s`
cmsRun step3.py nThr=1 inputFile=BPH-step2.root outputFile=BPH-step3.root seedOffset=$1
DATE_END_step3=`date +%s`
if [ $? -eq 0 ]; then echo "Successfully run step"; else exit $?; fi
echo "Finished running step3"
rm BPH-step2.root
#echo "Content of current directory"
#ls -al
#echo ""
#RUNTIME_step3=$((DATE_END_step3-DATE_START_step3))
#echo "Intermediate wallclock running time step3: $RUNTIME_step3 s"


### step4 ###
#echo "Going to copy cmsdriver to work dir"
#cp $STARTDIR/slurm/V00_v00_n10_njt1/step4.py $WORKDIR/. 
#echo "Copying pileup profile file to work dir"
#cp $STARTDIR/data/pileup_2018.root $WORKDIR/.
echo "Going to run step4"
DATE_START_step4=`date +%s`
cmsRun step4.py nThr=1 inputFile=BPH-step3.root outputFile=BPH-step4.root seedOffset=$1
DATE_END_step4=`date +%s`
if [ $? -eq 0 ]; then echo "Successfully run step"; else exit $?; fi
echo "Finished running step4"
rm BPH-step3.root
#echo "Content of current directory"
#ls -al
#echo ""
#RUNTIME_step4=$((DATE_END_step4-DATE_START_step4))
#echo "Intermediate wallclock running time step4: $RUNTIME_step4 s"


