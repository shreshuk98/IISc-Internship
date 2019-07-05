#!/usr/bin/env python
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, TLegend, gStyle
import ROOT as ROOT
import os
import sys, optparse
from array import array
import math
#import numpy as numpy_

#ROOT.gROOT.LoadMacro("Loader.h+")
#outfilename= "ntupleHistos.root"

def SetCanvas():

    # CMS inputs
    # -------------
    H_ref = 1000;
    W_ref = 1000;
    W = W_ref
    H  = H_ref

    T = 0.08*H_ref
    B = 0.21*H_ref
    L = 0.12*W_ref
    R = 0.08*W_ref
    # --------------

    c1 = TCanvas("c2","c2",0,0,2000,1500)
    c1.SetFillColor(0)
    c1.SetBorderMode(0)
    c1.SetFrameFillStyle(0)
    c1.SetFrameBorderMode(0)
    c1.SetLeftMargin( L/W )
    c1.SetRightMargin( R/W )
    c1.SetTopMargin( T/H )
    c1.SetBottomMargin( B/H )
    c1.SetTickx(0)
    c1.SetTicky(0)
    c1.SetTickx(1)
    c1.SetTicky(1)
    c1.SetGridy(0)
    c1.SetGridx(0)
    c1.SetLogy(1)
    return c1


def CreateLegend(x1, y1, x2, y2, header):

    leg = ROOT.TLegend(x1, x2, y1, y2)
    leg.SetFillColor(0)
    leg.SetFillStyle(3002)
    leg.SetBorderSize(0)
    leg.SetHeader(header)
    return leg


def AddText(txt):
    texcms = ROOT.TLatex(-20.0, 50.0, txt)
    texcms.SetNDC()
    texcms.SetTextAlign(12)
    texcms.SetX(0.1)
    texcms.SetY(0.94)
    texcms.SetTextSize(0.02)
    texcms.SetTextSizePixels(22)
    return texcms

def AddTextCat(cat):
    texCat = ROOT.TLatex(-20.0, 50.0, cat)
    texCat.SetNDC()
    texCat.SetTextAlign(12)
    texCat.SetX(0.85)
    texCat.SetY(0.94)
    texCat.SetTextFont(40)
    texCat.SetTextSize(0.025)
    texCat.SetTextSizePixels(22)
    return texCat


leg_entry=['m_{Zp}=450 GeV','m_{Zp}=500 GeV','m_{Zp}=600 GeV','m_{Zp}=800 GeV','m_{Zp}=1000 GeV','m_{Zp}=1200 GeV']#,'ma=dhfgvsg']

ntuple = TChain("ana/anatree")
#ntuple.Add(sys.argv[1])

runs=['01','02','03','05','06','07']#,'04','05','06']

histspt=[]
histseta=[]
histsphi=[]
histsmass=[]

for i in runs:

    ntuple = TChain("ana/anatree")
    RootFile='out_tree_run_'+i+'.root'
    ntuple.Add(RootFile)

    NEntries = ntuple.GetEntries()

    h_pt         =TH1F('h_pt','',100,0,1000)
    h_eta           =TH1F('h_eta',  '',  100,-8,8)
    h_phi          =TH1F('h_phi',  '',  10,-5,5)
    h_mass          =TH1F('h_mass','',100,100,500)


    for ievent in range(NEntries):
        #print ("Procees events", ievent,' of ',NEntries)
        #if ievent%1==0: print ("Processed %d of %d events..." %(ievent,NEntries))
        ntuple.GetEntry(ievent)
        genpid                     = ntuple.__getattr__('GenParticles_genpid')
        genpt                      = ntuple.__getattr__('GenParticles_genpt')
        geneta                   = ntuple.__getattr__('GenParticles_geneta')
        genphi                     = ntuple.__getattr__('GenParticles_genphi')
        genmass                    = ntuple.__getattr__('GenParticles_genmass')
        gencharge                    = ntuple.__getattr__('GenParticles_gencharge')
        genstatus                    = ntuple.__getattr__('GenParticles_genmass')
        mom0pt                    = ntuple.__getattr__('GenParticles_mom0pt')
        mom1pt                    = ntuple.__getattr__('GenParticles_mom1pt')
        mom0eta                    = ntuple.__getattr__('GenParticles_mom0eta')
        mom1eta                    = ntuple.__getattr__('GenParticles_mom1eta')
        mom0phi                    = ntuple.__getattr__('GenParticles_mom0phi')
        mom1phi                   = ntuple.__getattr__('GenParticles_mom1phi')
        mom0pid                    = ntuple.__getattr__('GenParticles_mom0pid')
        mom1pid                    = ntuple.__getattr__('GenParticles_mom1pid')
        mom0status                    = ntuple.__getattr__('GenParticles_mom0status')
        mom1status                    = ntuple.__getattr__('GenParticles_mom1status')
        mom0energy                    = ntuple.__getattr__('GenParticles_mom0energy')
        mom1energy                    = ntuple.__getattr__('GenParticles_mom1energy')

        # print ("total no of particle", len(genpid))
        # print("total mom0status",len(mom0status))
        p4h=ROOT.TLorentzVector();
        for i in range(len(mom0status)):
            pdgID=genpid[i+2]
            momstatus=mom0status[i]
            if (pdgID==5 or pdgID==-5) and mom0pid[i]==28 and momstatus==22:
                p4=ROOT.TLorentzVector()
                p4.SetPtEtaPhiM(genpt[i+2],geneta[i+2],genphi[i+2],genmass[i+2])
                p4h=p4h+p4
                # print("pdgID",pdgID)
                # print("mom0status",momstatus)
                # print("mom0pid",mom0pid[i])
                # print ("mom0status",mom0status[i])
                #print ("genstatus",genstatus[i+2])
                #print("mom0pt",mom0pt[i])
                #print ("genPt",genpt[i+2])

        h_pt.Fill(p4h.Pt())
        h_mass.Fill(p4h.M())
        h_eta.Fill(p4h.Eta())
        h_phi.Fill(p4h.Phi())
        #print("mass of A0:",p4h.M())
            # if pdgID==22:
            #     #print ()
            #     print ("pdgID",pdgID)
            #     print ("genPt",genpt[i])
            #     print ("status",status)

    histspt.append(h_pt)
    histseta.append(h_eta)
    histsphi.append(h_phi)
    histsmass.append(h_mass)

c=SetCanvas()
#c.SetLogy()

# gStyle.SetFrameLineWidth(5)
# gStyle.SetFillColor(4)
gStyle.SetOptStat(0)

legend = CreateLegend(0.70, 0.94, 0.75, 0.92, "m_{A0}=300 GeV, m_{h}=125 GeV")

for hist in range(len(histspt)):

    if hist==0:
        histspt[hist].SetXTitle("p_{T} of A0 [GeV]")
        histspt[hist].SetYTitle("Events")
        histspt[hist].SetMaximum(10)
        histspt[hist].SetLineColor(hist+1)
        histspt[hist].Rebin(2)
        histspt[hist].SetLineWidth(4)
        histspt[hist].Scale(1/histspt[hist].Integral())
        #histspt[hist].SetLineStyle(hist+1)
        legend.AddEntry(histspt[hist],leg_entry[hist],"L")
        histspt[hist].Draw('hist')

    else:
        histspt[hist].SetXTitle("pT_{A0} [GeV")
        histspt[hist].SetYTitle("Events")
        histspt[hist].SetMaximum(10)
        histspt[hist].SetLineColor(hist+1)
        histspt[hist].Rebin(2)
        histspt[hist].SetLineWidth(4)
        histspt[hist].Scale(1/histspt[hist].Integral())
        #histspt[hist].SetLineStyle(hist+1)
        legend.AddEntry(histspt[hist],leg_entry[hist],"L")
        #legend.AddEntry(histspt[hist],"run_0"+str(hist+1),"L")
        histspt[hist].Draw('hist&same')

legend.Draw()

txt = 'Zp->h(#gamma#gamma) A0(bb#tilde)'
texcms = AddText(txt)
texCat= AddTextCat("Zp2HDM")
texcms.Draw("same")
texCat.Draw("same")
t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "p_{T} comparison of A0", "brNDC")
t.Draw('same')
c.Update()

c.SaveAs("Combined_A0_pt_a0300.png")
c.SaveAs("Combined_A0_pt_a0300.root")

###################################################################

legend = CreateLegend(0.70, 0.94, 0.75, 0.92, "m_{A0}=300 GeV, m_{h}=125 GeV")

for hist in range(len(histseta)):

    if hist==0:
        histseta[hist].SetXTitle("#eta_{A0}")
        histseta[hist].SetYTitle("Events")
        histseta[hist].SetLineColor(hist+1)
        histseta[hist].SetLineWidth(4)
        histseta[hist].Scale(1/histseta[hist].Integral())
        #histseta[hist].SetLineStyle(hist+1)
        legend.AddEntry(histseta[hist],leg_entry[hist],"L")
        #legend.AddEntry(histseta[hist],"run_0"+str(hist+1),"L")
        histseta[hist].Draw('hist')

    else:
        histseta[hist].SetXTitle("#eta_{A0}")
        histseta[hist].SetYTitle("Events")
        histseta[hist].SetLineColor(hist+1)
        histseta[hist].SetLineWidth(4)
        histseta[hist].Scale(1/histseta[hist].Integral())
        #histseta[hist].SetLineStyle(hist+1)
        legend.AddEntry(histseta[hist],leg_entry[hist],"L")
        #legend.AddEntry(histseta[hist],"run_0"+str(hist+1),"L")
        histseta[hist].Draw('hist&same')

legend.Draw()

txt = 'Zp->h(#gamma#gamma) A0(bb#tilde)'
texcms = AddText(txt)
texCat= AddTextCat("Zp2HDM")
texcms.Draw("same")
texCat.Draw("same")
t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "#eta_{A0} comparison", "brNDC")
t.Draw('same')
c.Update()

c.SaveAs("Combined_A0_eta_a0300.png")
c.SaveAs("Combined_A0_eta_a0300.root")

###################################################################

legend = CreateLegend(0.80, 0.94, 0.75, 0.92, "m_{A0}=300 GeV, m_{h}=125 GeV")

for hist in range(len(histsphi)):

    if hist==0:
        histsphi[hist].SetXTitle("#phi_{A0}")
        histsphi[hist].SetYTitle("Events")
        histsphi[hist].SetLineColor(hist+1)
        histsphi[hist].SetLineWidth(4)
        histsphi[hist].Scale(1/histsphi[hist].Integral())
        #histsphi[hist].SetLineStyle(hist+1)
        legend.AddEntry(histsphi[hist],leg_entry[hist],"L")
        histsphi[hist].Draw('hist')

    else:
        histsphi[hist].SetXTitle("#phi_{A0}")
        histsphi[hist].SetYTitle("Events")
        histsphi[hist].SetLineColor(hist+1)
        histsphi[hist].SetLineWidth(4)
        histsphi[hist].Scale(1/histsphi[hist].Integral())
        #histsphi[hist].SetLineStyle(hist+1)
        legend.AddEntry(histsphi[hist],leg_entry[hist],"L")
        histsphi[hist].Draw('hist&same')

legend.Draw()

txt = 'Zp->h(#gamma#gamma) A0(bb#tilde)'
texcms = AddText(txt)
texCat= AddTextCat("Zp2HDM")
texcms.Draw("same")
texCat.Draw("same")
t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "#phi_{A0} comparison", "brNDC")
t.Draw('same')
c.Update()

c.SaveAs("Combined_A0_phi_a0300.png")
c.SaveAs("Combined_A0_phi_a0300.root")

###################################################################

legend = CreateLegend(0.70, 0.94, 0.75, 0.92, "m_{A0}=300 GeV, m_{h}=125 GeV")

for hist in range(len(histsmass)):

    if hist==0:
        histsmass[hist].SetXTitle("m_{bb#tilde} [GeV]")
        histsmass[hist].SetYTitle("Events")
        histsmass[hist].SetLineColor(hist+1)
        histsmass[hist].SetLineWidth(4)
        histsmass[hist].Rebin(4)
        histsmass[hist].Scale(1/histsmass[hist].Integral())
        #histsmass[hist].SetLineStyle(hist+1)
        legend.AddEntry(histsmass[hist],leg_entry[hist],"L")
        histsmass[hist].Draw('hist')

    else:
        histsmass[hist].SetXTitle("M_{bb#tilde} [GeV]")
        histsmass[hist].SetYTitle("Events")
        histsmass[hist].SetLineColor(hist+1)
        histsmass[hist].SetLineWidth(4)
        histsmass[hist].Rebin(4)
        histsmass[hist].Scale(1/histsmass[hist].Integral())
        #histsmass[hist].SetLineStyle(hist+1)
        legend.AddEntry(histsmass[hist],leg_entry[hist],"L")
        histsmass[hist].Draw('hist&same')

legend.Draw()

txt = 'Zp->h(#gamma#gamma) A0(bb#tilde )'
texcms = AddText(txt)
texCat= AddTextCat("Zp2HDM")
texcms.Draw("same")
texCat.Draw("same")
t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "m_{A0} comparison", "brNDC")
t.Draw('same')
c.Update()

c.SaveAs("Combined_A0_mass_a0300.png")
c.SaveAs("Combined_A0_mass_a0300.root")
