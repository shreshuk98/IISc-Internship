import ElementTree2 as ET
from ROOT import TFile, TTree, TH1F, TH1D, TH1, TCanvas, TChain,TGraphAsymmErrors, TMath, TH2D, TLorentzVector, AddressOf, gROOT, TNamed, TLegend, gStyle
import ROOT as ROOT

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

leg_entry=['m_{Zp}=450 GeV','m_{Zp}=500 GeV','m_{Zp}=600 GeV']#,'m_{Zp}=800 GeV','m_{Zp}=1000 GeV','m_{Zp}=1200 GeV']
runs=['01','02','03']#,'04']
histspt=[]
histseta=[]
histsphi=[]
histsmass=[]

for i in runs:
    tree1 = ET.parse('run_'+i+'.lhe')
    root1=tree1.getroot()
    phi_A0=[]
    eta_A0=[]
    pt_A0=[]
    m_A0=[]
    # gStyle.SetFrameLineWidth(3)
    # gStyle.SetOptTitle(0)
    # gStyle.SetOptStat(0)
    # #gStyle.SetLegendBorderSize(2)
    # gStyle.SetFillColor(4)
    # gStyle.SetLineWidth(1)
    # #gStyle.SetPadColor(1)
    # #legend=TLegend(.63,.69,.87,.89,"","brNDC")
    # #legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_01")
    # c = TCanvas()

    #lhefdata=LHEFData(float(root.attrib['version']))
    for child in root1:
        if(child.tag=='event'):
           lines=child.text.strip().split('\n')
           event_header=lines[0].strip()
           num_part=int(event_header.split()[0].strip())

           h=[s for s in lines if s.split()[0]=='25']
           b=[s for s in lines if s.split()[0]=='5' and ((s.split()[2]=='5' and lines[5].split()[0]=='28') or (s.split()[2]=='4' and lines[4].split()[0]=='28'))]
           chi=[s for s in lines if s.split()[0]=='-5' and ((s.split()[2]=='5' and lines[5].split()[0]=='28') or (s.split()[2]=='4' and lines[4].split()[0]=='28'))]

           p=[]
           p1=[]
           p2=[]
           if b:
               px=float (b[0].split()[6])
               py=float (b[0].split()[7])
               pz=float (b[0].split()[8])
               e=float (b[0].split()[9])
               m=float(b[0].split()[10])
               p=TLorentzVector(px,py,pz,e)

           if chi:
               px1=float (chi[0].split()[6])
               py1=float (chi[0].split()[7])
               pz1=float (chi[0].split()[8])
               e1=float (chi[0].split()[9])
               p1=TLorentzVector(px1,py1,pz1,e1)

           if h:
               px2=float (h[0].split()[6])
               py2=float (h[0].split()[7])
               pz2=float (h[0].split()[8])
               e2=float (h[0].split()[9])
               p2=TLorentzVector(px2,py2,pz2,e2)

           if b and chi and h:
               pi=[]
               pi=p+p1+p2
               m_A0.append(pi.M())
               phi_A0.append(pi.Phi())
               eta_A0.append(pi.Eta())
               pt_A0.append(pi.Pt())


    h_mass1=TH1F("Inv.Mass of Zp","",200,200,800)
    for i in m_A0:
        h_mass1.Fill(i)

    histsmass.append(h_mass1)

    # h_pt1=TH1F("pT of Zp","",100,-100,1000)
    # for i in pt_A0:
    #         h_pt1.Fill(i)
    #
    # h_phi1=TH1F("Phi of Zp","",10,-5,5)
    # for i in phi_A0:
    #     h_phi1.Fill(i)
    #

c = SetCanvas()
gStyle.SetOptStat(0)
legend = CreateLegend(0.80, 0.94, 0.75, 0.92, "m_{A0}=300 GeV, m_{h}=125 GeV")

for hist in range(len(histsmass)):
    #legend = CreateLegend(0.70, 0.94, 0.75, 0.92, "M_{A0}=300 GeV")
    if hist==0:
        histsmass[hist].SetXTitle("m_{#gamma#gammabb~} [GeV]")
        histsmass[hist].SetYTitle("Events")
        histsmass[hist].SetLineColor(hist+1)
        histsmass[hist].SetLineWidth(4)
        histsmass[hist].Scale(1/histsmass[hist].Integral())
        #histsmass[hist].SetLineStyle(hist+1)
        legend.AddEntry(histsmass[hist],leg_entry[hist],"L")
        histsmass[hist].Draw('hist')

    else:
        histsmass[hist].SetXTitle("m_{#gamma#gammabb~} [GeV]")
        histsmass[hist].SetYTitle("Events")
        histsmass[hist].SetLineColor(hist+1)
        histsmass[hist].SetLineWidth(4)
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
t = ROOT.TPaveLabel(0.1, 0.96, 0.95, 0.99, "m_{Zp} comparison", "brNDC")
t.Draw('same')
c.Update()

c.SaveAs("Phi of Zp Combined.png")
c.SaveAs("Phi of Zp Combined.root")
