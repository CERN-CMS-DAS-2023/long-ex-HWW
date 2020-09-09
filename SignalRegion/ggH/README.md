HWW ggH 2018 analysis
=====================

How to run the analysis.

Remember to define the file: Tools/python/userConfig.py (if not already done)
    
    #!/usr/bin/env python
    baseDir  = '/afs/cern.ch/user/a/amassiro/jobs/'
    jobDir   = baseDir+'jobs/'
    workDir  = baseDir+'workspace/'
    jobDirSplit=True


Resubmit:


    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__ggH2018_v6/mkShapes__ggH2018_v6__*.jid | awk '{print "condor_submit " $9}'  | sed 's/jid/jds/'
    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__ggH2018_v6__ALL/*/mkShapes__ggH2018_v6__*.jid | awk '{print "condor_submit " $9}'  | sed 's/jid/jds/'


Location ntuples:

    /eos/user/c/cmsdas/long-exercises/hww/Autumn18_102X_nA1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/
    from: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6/
    
    
    
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_ggH2018_v6_ALL.root rootFile/plots_ggH2018_v6_ALL_*.root
    
    
<!-- # Run a postprocessing script for the correct treatment of DY embedded uncertainties -->
<!--  -->
<!--     python scripts/mkDYvetoUnc.py configuration.py -->

# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_ggH2018_v6.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1

# Make datacards:

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_ggH2018_v6.root

# Combine datacards (also removes samples with expected yield below a given threshold) and make workspaces:

    ./scripts/doCombination.sh

# Do the fits:

    ./scripts/doFits.sh


    
    
    
Special usecase:

    easyDescription.py --inputFileSamples samples.py --outputFileSamples extended_samples.py

    
    