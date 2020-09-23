Lepton Scale uncertainties
=====================
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

    
Resubmit

    ls -alrth /afs/cern.ch/user/a/amassiro/jobs/jobs/mkShapes__LeptonScaleNuisance__ALL/*/mkShapes__*.jid | awk '{print "condor_submit " $9}'  | sed 's/jid/jds/'

    
    
# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_LeptonScaleNuisance_ALL.root rootFile/plots_LeptonScaleNuisance_ALL_*.root

# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_LeptonScaleNuisance.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1

# Make datacards:

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_LeptonScaleNuisance.root


# Check nuisances

    cd ../../../LatinoAnalysis/ShapeAnalysis/test/draw

    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/LeptonScale/datacards/df/ptll/shapes/histos_df.root  \
     --outputDirPlots ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/LeptonScale/df_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/LeptonScale/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/LeptonScale/samples.py \
     --cutName df

     

Variables:

    root -l /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv6_Full2018v6/MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6__MupTup_suffix/nanoLatino_ST_t-channel_top__part19.root
    
    Events->Scan("mll_MupTup")
    
    