# cuts
supercut = 'mll>12  \
            && Lepton_pt[0]>25 && Lepton_pt[1]>20 \
            && bVeto \
            && PuppiMET_pt > 30 \
            '

cuts['hww2l2v_13TeV_SS_em'] = '(Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13) \
                          && nLepton==2  \
                         '
                         



