import FWCore.ParameterSet.Config as cms

from Analysis.VLQAna.VLQParams_cfi import * 

evtcleaner = cms.EDFilter("EventCleaner",
    runnoLabel                 = cms.InputTag("eventInfo", "evtInfoRunNumber"),
    lumisecLabel               = cms.InputTag("eventInfo", "evtInfoLumiBlock"),
    evtnoLabel                 = cms.InputTag("eventInfo", "evtInfoEventNumber"),
    trigNameLabel              = cms.InputTag("TriggerUserData", "triggerNameTree"), 
    trigBitLabel               = cms.InputTag("TriggerUserData", "triggerBitTree"), 
    metFiltersNameLabel        = cms.InputTag("METUserData", "triggerNameTree"), 
    metFiltersBitLabel         = cms.InputTag("METUserData", "triggerBitTree"), 
    lheProdName                = cms.string("externalLHEProducer"), 
    genEvtInfoProdName         = cms.string('generator'),
    vtxRhoLabel                = cms.InputTag("vertexInfo", "rho"),
    vtxZLabel                  = cms.InputTag("vertexInfo", "z"),
    vtxNdfLabel                = cms.InputTag("vertexInfo", "ndof"),
    npvLabel                   = cms.InputTag("eventUserData", "npv"),
    puNtrueIntLabel            = cms.InputTag("eventUserData", "puNtrueInt"),
    hltPaths                   = cms.vstring (
        ), 
    metFilters                 = cms.vstring (
        "Flag_goodVertices",
        "Flag_CSCTightHaloFilter",
        "Flag_HBHENoiseFilter", 
        "Flag_eeBadScFilter",
        ), 
    isData                     = cms.bool(False), 
    DoPUReweightingOfficial    = cms.bool(False),
    DoPUReweightingNPV         = cms.bool(False),
    File_PVWt                  = cms.string('hnpv_data_Run2015D_mc_RunIISpring15DR74-Asympt25ns_pvwt.root'),
    File_PUDistData            = cms.string('RunII2015_25ns_PUXsec69000nb.root'),
    File_PUDistDataLow         = cms.string('RunII2015_25ns_PUXsec65550nb.root'),
    File_PUDistDataHigh        = cms.string('RunII2015_25ns_PUXsec72450nb.root'),
    File_PUDistMC              = cms.string('PUDistMC_2015_25ns_Startup_PoissonOOTPU.root'),
    Hist_PVWt                  = cms.string('hpvwt_data_mc'),
    Hist_PUDistData            = cms.string('pileup'),
    Hist_PUDistMC              = cms.string('pileup'),
    cleanEvents                = cms.bool(False), 
    TtZParams                  = cms.PSet(genPartParams,TtZParams), 
    TtHParams                  = cms.PSet(genPartParams,TtHParams), 
    TbWParams                  = cms.PSet(genPartParams,TbWParams), 
    BbZParams                  = cms.PSet(genPartParams,BbZParams), 
    BbHParams                  = cms.PSet(genPartParams,BbHParams), 
    BtWParams                  = cms.PSet(genPartParams,BtWParams), 
    )
