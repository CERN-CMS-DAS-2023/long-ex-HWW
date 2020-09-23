Top control region
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


Resubmit:


    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__Top2018_v6__ALL/mkShapes__*.jid | awk '{print "condor_submit " $9}'  | sed 's/jid/jds/'
    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__Top2018_v6__ALL/*/mkShapes__*.jid | awk '{print "condor_submit " $9}'  | sed 's/jid/jds/'

    
# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_Top2018_v6_ALL.root rootFile/plots_Top2018_v6_ALL_*.root
    

# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_Top2018_v6.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1
    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_Top2018_v6.root --showIntegralLegend=1

    
    
Special usecase:

    easyDescription.py --inputFileSamples samples.py --outputFileSamples extended_samples.py

    
    