from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = 'TpTp_M1200_25ns'
config.General.workArea = 'OS2LAna_12oct2015/'
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'os2lana_cfg.py' 
config.JobType.pyCfgParams = ['isData=False', 'doPUReweightingNPV=True']

config.section_("Data")
config.Data.inputDataset = '/TprimeTprime_M-1200_TuneCUETP8M1_13TeV-madgraph-pythia8/phys_b2g-B2GAnaFW_v74x_v6p1_25ns-d5e3976e154b1b4043d031aaa9c2809b/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.ignoreLocality = False
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/devdatta/OS2LAna_12oct2015/'
# This string is used to construct the output dataset name

config.section_("Site")
config.Site.storageSite = 'T2_CH_CERN'

config.section_('User')
