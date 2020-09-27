# cuts

supercut = ' mll > 12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>13 \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
           '

cuts['hww2l2v_top_13TeV'] = {
   'expr': 'topcr && mtw2>30 && mll>50',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'em' : ' multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
      #
   }
}

cuts['hww2l2v_2jet_13TeV'] = {
   'expr': '1',
    # Define the sub-categorization of sr
   'categories' : {
      #
      'em' : ' multiJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)',
      #
   }
}

