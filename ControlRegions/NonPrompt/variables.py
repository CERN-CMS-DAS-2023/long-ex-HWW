# variables

#variables = {}
    


variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                        'fold' : 3
                       }

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',    
                        'range' : (20,0,200),
                        'xaxis' : 'pfmet [GeV]',
                        'fold'  : 3
                        }

variables['mll']  = {   'name': 'mll',            #   variable name    
                        'range' : (20, 40,120),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['detall']  = {   'name': 'abs(Lepton_eta[0] - Lepton_eta[1])',            #   variable name    
                        'range' : (20,0.,10.),    #   variable range
                        'xaxis' : 'detall',  #   x axis name
                        'fold' : 3
                        }


variables['mth']  = {   'name': 'mth',            #   variable name    
                        'range' : (40,0,200),    #   variable range
                        'xaxis' : 'm_{T}^{H} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['dphill']  = {   'name': 'abs(dphill)',     
                        'range' : (20,0,3.14),   
                        'xaxis' : '#Delta#phi_{ll}',
                        'fold' : 3
                        }


variables['ptll']  = {   'name': 'ptll',     
                        'range' : (40, 0,200),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }
variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (20,0,100),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3                         
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',     
                        'range' : (20,0,100),   
                         'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3                         
                        }
variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3                         
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3                         
                        }



variables['ht']  = {  'name': 'ht',
                        'range' : (40,0,200),
                        'xaxis' : 'ht [GeV]',
                         'fold' : 3
                        }
