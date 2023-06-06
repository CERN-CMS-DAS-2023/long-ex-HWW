# PlotsConfigurationsCMSDAS2023CERN

Twiki: https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolCERN2023HWWLongExercise

## Installation
Singularity image:

    apptainer shell   -B /afs/ -B /cvmfs --bind /tmp  --bind /eos/ --env KRB5CCNAME=$KRB5CCNAME --bind /etc/sysconfig/ngbauth-submit   -B /etc/grid-security/certificates \
    /cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/dvalsecc/latinoanalysis-cms-das-cern-2023:lxplus-cc7-latest

    # You will be now inside the image
    # Activate the CMSSW environment with LatinosAnalysis pre-installed under /opt/CMSSW_10_6_27
    source /usr/bin/activate-latinos

    # setup an environmental variable for the location of the jobs file
    export LATINOS_BASEDIR=/afs/cern.ch//

    # You are now ready to work on Latinos configurations

Manual install :

    cmsrel CMSSW_10_6_4
    cd CMSSW_10_6_4/src/
    cmsenv
    git clone --branch 13TeV git@github.com:latinos/setup.git LatinosSetup
    source LatinosSetup/SetupShapeOnly.sh
    git clone git@github.com:amassiro/PlotsConfigurationsCMSDAS2020CERN.git PlotsConfigurations
    cd LatinoAnalysis/Tools/python/
    cp userConfig_TEMPLATE.py userConfig.py (change the baseDir path to somewhere you have write permissions)     
    cd -
    scram b -j4

    
 
## Content 
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
    
 
