# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from LatinoAnalysis.Tools.commonTools import getSampleFiles

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc_emb = [skey for skey in samples if skey != 'DATA' and skey != 'Dyveto' and not skey.startswith('Fake')]
    mc = [skey for skey in mc_emb if skey != 'Dyemb']
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

################################ EXPERIMENTAL UNCERTAINTIES  #################################

##### Jet energy scale
  
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']
folderup = ""
folderdo = ""

for js in jes_systs:
  if 'Absolute' in js:
     folderup = 'JESAbsoluteup_suffix'
     folderdo = 'JESAbsolutedo_suffix'
  elif 'BBEC1' in js:
     folderup = 'JESBBEC1up_suffix'
     folderdo = 'JESBBEC1do_suffix'
  elif 'EC2' in js:
     folderup = 'JESEC2up_suffix'
     folderdo = 'JESEC2do_suffix'
  elif 'HF' in js:
     folderup = 'JESHFup_suffix'
     folderdo = 'JESHFdo_suffix'
  elif 'Relative' in js:
     folderup = 'JESRelativeup_suffix'
     folderdo = 'JESRelativedo_suffix'
  elif 'FlavorQCD' in js:
     folderup = 'JESFlavorQCDup_suffix'
     folderdo = 'JESFlavorQCDdo_suffix' 
  
  nuisances[js] = {
                'name': 'CMS_scale_'+js,
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': js+'up',
                'mapDown': js+'do',
                'samples': dict((skey, ['1', '1']) for skey in mc),
                'folderUp'   : makeMCDirectory(folderup), 
                'folderDown' : makeMCDirectory(folderdo),
                #'AsLnN': '1'
  }




