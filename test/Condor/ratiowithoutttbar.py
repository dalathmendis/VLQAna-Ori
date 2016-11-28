#! /usr/bin/env python                                                          
from array import array
from ROOT import TH1D,TFile,TCanvas, THStack,TF1, TH1,TList

from ROOT import TH1D,TH2D,TFile,TMath,TCanvas,THStack,TLegend,TPave,TLine,TLatex, TF1, TGraph, TMultiGraph,kBlack,kBlue
from ROOT import gROOT,gStyle,gPad,gStyle


#path ='/uscms_data/d3/dmendis/80x/CMSSW_8_0_15/src/Analysis/VLQAna/test/Condor/Histo5Mu/'
path = '/uscms_data/d3/dmendis/80x/CMSSW_8_0_15/src/Analysis/VLQAna/test/Condor/Macro/mutest3/CR_Zmumu/'
path2 = '/uscms_data/d3/dmendis/80x/CMSSW_8_0_15/src/Analysis/VLQAna/test/Condor/Macro/mutest3/CR_Zmumu/'

c1= TCanvas()
#f1 = TFile(path+'ht_pre.root')
f1 = TFile(path2+'nob_ht.root')

#define empty histograms
h1=TH1D()
h2=TH1D()
h3=TH1D()
h4=TH1D()
h5=TH1D()

gStyle.SetOptStat(0)# 0 =kFALSE , set all option stat boxes to zero

n= 1 # signal mutiplication
rebin=1 # set rebin
signalsample="tZbW"

def cosmetics( hs,mkrsize,mkrstyle,mkrcolor,linewidth,fillcolor, linecolor, fillstyle,rebins,title):
    hs.SetMarkerSize(mkrsize)
    hs.SetMarkerStyle(mkrstyle)
    hs.SetMarkerColor(mkrcolor)
    hs.SetLineWidth(linewidth)
    hs.SetFillColor(fillcolor)
    hs.SetLineColor(linecolor)
    hs.SetFillStyle(fillstyle)
    hs.Rebin(rebins)
    hs.SetTitle(title)

#get appropriate histograms from the root file
h1= f1.Get('eeT0Z0H0b2__DATA')
h2 = f1.Get('eeT0Z0H0b2__DY')
h3= f1.Get('eeT0Z0H0b2__Top')

c1.Divide(3,2)
c1.cd(1)

cosmetics(h1, 1,20,1,2,1,2,1001,rebin,"overly of Data,DY and TTBar")
cosmetics(h2, 1,22,28,2,28,4,1001,rebin, " ")
cosmetics(h3, 1,21,3,2,3,46,1001,rebin, " ")

h1.Draw()
h2.Draw("SAME")
h3.Draw("SAME")

leg1 =TLegend(0.6,0.7,0.9,0.9)#); //(x1,y1,x2,y2)                                                                                                                          
leg1.AddEntry(h1,"Data","f")
leg1.AddEntry(h2,"DY","f")
leg1.AddEntry(h3,"ttbar","f")
leg1.Draw()

cms = TLatex()
cms.SetNDC(1)
cms.SetTextFont(61)
cms.SetTextSize(0.04)
cms.DrawLatex(0.6, 0.65,"Rebin ="+str(rebin))

c1.cd(2)
h4=h1.Clone('h4')
h4.Add(h3,-1)
cosmetics(h4, 1,20,1,2,1,2,1001,1,"overly of Data-TTBar,DY and TTBar")
h4.Draw("b")
h2.Draw("b SAME")
h3.Draw("b SAME")

leg2=TLegend(0.6,0.7,0.9,0.9)#); //(x1,y1,x2,y2)                                                                                                    
leg2.AddEntry(h4,"Data-TTBar","f")
leg2.AddEntry(h2,"DY","f")
leg2.AddEntry(h3,"ttbar","f")
leg2.Draw()
cms = TLatex()
cms.SetNDC(1)
cms.SetTextFont(61)
cms.SetTextSize(0.04)
cms.DrawLatex(0.6, 0.65,"Rebin ="+str(rebin))

c1.cd(3)
h5=h1.Clone('h5')
h5.Add(h3,-1)
h6= f1.Get('eeT0Z0H0b2__TT_'+str(signalsample)+'_M800')

cosmetics(h6, 2,2,4,2,4,46,1001,rebin," ")
h5.Add(h6,n)
cosmetics(h5, 1,20,1,2,1,2,1001,1,"overly of (Data-TTBar+"+str(n)+"*Signal) and DY ")
h5.Draw()
h2.Draw("SAME")

leg3=TLegend(0.6,0.7,0.9,0.9)#); //(x1,y1,x2,y2)                                                                                                                           
leg3.AddEntry(h5,"Data +"+str(n)+"signal-TTBar","f")
leg3.AddEntry(h2,"DY","f")
leg3.Draw()

cms = TLatex()
cms.SetNDC(1)
cms.SetTextFont(61)
cms.SetTextSize(0.04)
cms.DrawLatex(0.6, 0.65,"Rebin ="+str(rebin))

c1.cd(4)
h6=TH1D()
h6=h1.Clone('h6')
h6.Divide(h2)
h6.SetTitle("Ratio plot (Data/DY)")
h6.SetMarkerStyle(20)  
h6.Draw()

line1 = TLine(0, 1, 4000, 1)                                                                                                                                                
line1.SetLineColor(kBlack)                                                                                                                                                  
line1.Draw()                                                                                                                                                           
line2 = TLine(0, 0, 4000, 0)                                                                                                                                                
line2.SetLineColor(kBlack)                                                                                                                                                 
line2.Draw()  

c1.cd(5)
h7=TH1D()
h7=h4.Clone('h7')
h7.Divide(h2)
h7.SetTitle("Ratio plot (Data-ttbar)/DY")
h7.SetMarkerStyle(20)
h7.Draw()

line3 = TLine(0, 1, 4000, 1)
line3.SetLineColor(kBlack)
line3.Draw()
line4 = TLine(0, 0, 4000, 0)
line4.SetLineColor(kBlack)
line4.Draw()

f3 = TF1("myfit"," [0]+ [1]*x", 201,1300)                                                                                                                                   
h7.Fit("myfit","r")                                                                                                                                                         
 

c1.cd(6)
h8=TH1D()
h8=h5.Clone('h8')
h8.Divide(h2)
h8.SetTitle("Ratio plot (Data-ttbar+"+str(n)+"*signal)/DY")
h8.SetMarkerStyle(20)
h8.Draw()

line5 = TLine(0, 1, 4000, 1)
line5.SetLineColor(kBlack)
line5.Draw()
line6 = TLine(0, 0, 4000, 0)
line6.SetLineColor(kBlack)
line6.Draw()

#f3 = TF1("myfit"," [0]+ [1]*x", 201,1300)
h8.Fit("myfit","r")



'''
c1.cd(2)
h3=h6.Clone('h3')
h3.Divide(h2)
h3.GetYaxis().SetTitle('Ratio Data/DY')
h3.GetYaxis().SetTitleFont(43)
h3.GetYaxis().SetTitleOffset(0.5)
h3.GetYaxis().SetTitleSize(20)
h3.SetMarkerStyle(20)

#for i in range(1,100):
  #  nbin = h3.GetBinContent(i)
  #  nbinX= h3.GetNbinsX()
  #  bincen = h3.GetBinCenter(i)
   # binlab=h3.GetBinLabel(i)
#f3 = TF1("myfit"," [0]+ ([1]*x) +([2]*x^2)+([3]*x^3)", 200,2500)
#f3 = TF1("myfit"," [0]", 1500,3000) 
f3 = TF1("myfit"," [0]+ [1]*x", 201,1300) 

h3.Fit("myfit","r")
h3.Draw()


line = TLine(0, 1, 4000, 1)
line.SetLineColor(kBlack)
line.Draw()

line1 = TLine(0, 0, 4000, 0)
line1.SetLineColor(kBlue)
line1.Draw()

nbins1= h6.GetNbinsX()
nbins2 = h2.GetNbinsX()
nbins3 = h5.GetNbinsX()
print "nbins",nbins1
print "nbins2", nbins2
print "nbins2", nbins3
print " ********** data before removing adding ttbar*********************"
for i in range (1,nbins1+1):
    print h6.GetBinContent(i)

print " **********  ttbar*********************"
for i in range (1,nbins3+1):
    print h5.GetBinContent(i)
h6.Add(h5,-1) 

print " ********** data after removing  ttbar*********************"
for i in range (1,nbins1+1):
    print h6.GetBinContent(i)

h6.Add(h5,2)
print " ********** data after removing  ttbar*********************"
for i in range (1,nbins1+1):
    print h6.GetBinContent(i)



c1.cd(4)
h7= TH1D()
h8= TH1D()
h7=h1.Clone('h7')
h8=f1.Get('eeT0Z0H0b2__TT_tZtZ_M800') 
h7.Add(h5,-1)
list = TList()
list.Add(h7)
factor = 100
list.Add(factor*h8)
h = h1.Clone("h")
h.Reset()
h.Merge(list)
#h.Draw()  


#h7=h6.Add('h7')
h.Divide(h2)
h.GetYaxis().SetTitle('Ratio Data-ttbar+signal/DY')
h.GetYaxis().SetTitleFont(43)
h.GetYaxis().SetTitleOffset(0.5)
h.GetYaxis().SetTitleSize(20)
h.SetMarkerStyle(20)

#for i in range(1,100):                                                                                                                                           
  #  nbin = h3.GetBinContent(i)                                                                                                                                   
  #  nbinX= h3.GetNbinsX()                                                                                                                                        
  #  bincen = h3.GetBinCenter(i)                                                                                                                                  
   # binlab=h3.GetBinLabel(i)                                                                                                                                     
#f3 = TF1("myfit"," [0]+ ([1]*x) +([2]*x^2)+([3]*x^3)", 200,2500)                                                                                                 
#f3 = TF1("myfit"," [0]", 1500,3000)                                                                                                                              
f4 = TF1("myfit1"," [0]+ [1]*x", 201,1300)

h.Fit("myfit1","r")
h.Draw()



line2 = TLine(0, 1, 4000, 1)
line2.SetLineColor(kBlack)
line2.Draw()

line3 = TLine(0, 0, 4000, 0)
line3.SetLineColor(kBlue)
line3.Draw()

c1.cd(3)
h10 =TH1D()
h11=TH1D()
h10=factor*h8
#h10.Draw()
h11=h1.Clone('h11')
h11.Add(h5,-1)
#h1.Draw("SAME")
hs1 = THStack()
hs1.Add(h10)
hs1.Add(h11)
hs1.Draw()
'''
raw_input("hod_on")
'''
    if bincen>2000:
        #print nbin,",",bincen #nbin, i
        #f3 = TF1("myfit"," [0]+ ([1]*x) +([2]*x^2)+([3]*x^3)", 200,2500)
        f4 = TF1("myfit1"," [0]", 2000,3000)
#f3 = TF1("myfit"," [0]+ ([1]*x) +([2]*x^2)", 200,2500)
#f3 = TF1("myfit"," [0]+ ([1]*x)", 201,1200) 

        h3.Fit("myfit1","r") 
        h3.Draw('')

raw_input("hod_on")
'''
