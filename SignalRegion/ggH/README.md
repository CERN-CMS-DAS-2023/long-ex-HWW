HWW ggH 2017 analysis
=====================

How to run the analysis.

Remember to define the file: Tools/python/userConfig.py (if not already done)
    
    #!/usr/bin/env python
    baseDir  = '/afs/cern.ch/user/a/amassiro/jobs/'
    jobDir   = baseDir+'jobs/'
    workDir  = baseDir+'workspace/'
    jobDirSplit=True


# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

# Run a postprocessing script for the correct treatment of DY embedded uncertainties

    python scripts/mkDYvetoUnc.py configuration.py

# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_ggH2017_v6.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1

# Make datacards:

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_ggH2017_v6.root

# Combine datacards (also removes samples with expected yield below a given threshold) and make workspaces:

    ./scripts/doCombination.sh

# Do the fits:

    ./scripts/doFits.sh

