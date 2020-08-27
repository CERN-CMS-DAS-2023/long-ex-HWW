# PlotsConfigurationsCMSDAS2020CERN

Install:

    cmsrel CMSSW_10_6_4
    cd CMSSW_10_6_4/src/
    cmsenv
    git clone --branch 13TeV git@github.com:latinos/setup.git LatinosSetup
    source LatinosSetup/SetupShapeOnly.sh
    scram b -j4

    
 

 
 

Where (temporary):

    /afs/cern.ch/work/a/amassiro/Latinos/Framework/CMSDAS2020CERN/CMSSW_10_6_4/src
    
First simple phase space:

    Z>mumu
    Z>ee
    
    ControlRegions/DY/
    

Effect of scale factors:

    Z>mumu
    Z>ee
    
    ControlRegions/DYscalefactors/


Non-prompt control region (a.k.a. same sign]

    non-prompt
    
    ControlRegions/NonPrompt/


Top control region 

    non-prompt
    
    ControlRegions/Top/


Nuisances:
theory nuisance 

    Nuisances/TheoryScale

Experimental nusances
E.g. lepton scale

    Nuisances/LeptonScale

    
Signal regions 

    SignalRegion/ggH
    SignalRegion/VBF
    SignalRegion/All
    
 