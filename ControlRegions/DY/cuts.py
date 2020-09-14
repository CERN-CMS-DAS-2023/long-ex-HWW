# cuts

supercut = ' mll > 12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
           '

## Signal regions
cuts['hww2l2v_13TeV'] = {
   'expr': 'bVeto',
    # Define the sub-categorization of sr
   'categories' : {
      'em' : ' zeroJet  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13) && mth<60 && mll>40 && mll<80',
      #
      'ee' : ' zeroJet  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)',
      #
      'mm' : ' zeroJet  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)', 
      #
   }
}


