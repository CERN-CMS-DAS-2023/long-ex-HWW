Theory uncertainties
=====================
    
# Produce the shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday

# Hadd the root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10

or

    hadd rootFile/plots_TheoryNuisance_ALL.root rootFile/plots_TheoryNuisance_ALL_*.root

# Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile rootFile/plots_TheoryNuisance.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1

# Make datacards:

    mkDatacards.py --pycfg configuration.py --inputFile rootFile/plots_TheoryNuisance.root


# Check nuisances

    cd ../../../LatinoAnalysis/ShapeAnalysis/test/draw

    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/TheoryScale/datacards/df/ptll/shapes/histos_df.root  \
     --outputDirPlots ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/TheoryScale/df_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/TheoryScale/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurationsCMSDAS2020CERN/Nuisances/TheoryScale/samples.py \
     --cutName df

     
