import ElementTree2 as ET
from ROOT import TLorentzVector, TCanvas, TH1F,TLegend,gStyle, TPaveLabel

tree1 = ET.parse('/Users/chep/Documents/MG5_aMC_v2_6_5/mywork/pp_zp_a0h_bb_292600_scan/Events/run_01/unweighted_events.lhe')
root1=tree1.getroot()
phi_A0=[]
eta_A0=[]
pt_A0=[]
m_A0=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(0)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(4)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_01")
c = TCanvas()

#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())




       b=[s for s in lines if s.split()[0]=='25']

       p=[]
       p1=[]
       if b:
           px=float (b[0].split()[6])
           py=float (b[0].split()[7])
           pz=float (b[0].split()[8])
           e=float (b[0].split()[9])
           m=float(b[0].split()[10])
           p=TLorentzVector(px,py,pz,e)
           phi_A0.append(p.Phi())
           eta_A0.append(p.Eta())
           pt_A0.append(p.Pt())


h_pt1=TH1F("pT of h","",100,-100,1000)
for i in pt_A0:
        h_pt1.Fill(i)

h_phi1=TH1F("Phi of h","",10,-5,5)
for i in phi_A0:
    h_phi1.Fill(i)

h_eta1=TH1F("Eta of h","",10,-8,8)
for i in eta_A0:
        h_eta1.Fill(i)



tree1 = ET.parse('/Users/chep/Documents/MG5_aMC_v2_6_5/mywork/pp_zp_a0h_bb_292600_scan/Events/run_02/unweighted_events.lhe')
root1=tree1.getroot()
phi_A0_1=[]
eta_A0_1=[]
pt_A0_1=[]
m_A0_1=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(1111)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(4)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_02")

#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())


       b1=[s for s in lines if s.split()[0]=='25']


       p=[]
       p1=[]
       if b1:
           px=float (b1[0].split()[6])
           py=float (b1[0].split()[7])
           pz=float (b1[0].split()[8])
           e=float (b1[0].split()[9])
           m=float(b1[0].split()[10])
           p=TLorentzVector(px,py,pz,e)
           phi_A0_1.append(p.Phi())
           eta_A0_1.append(p.Eta())
           pt_A0_1.append(p.Pt())


h_pt2=TH1F("pT of h","",100,-100,1000)
for i in pt_A0_1:
        h_pt2.Fill(i)

h_phi2=TH1F("Phi of h","",10,-5,5)
for i in phi_A0_1:
    h_phi2.Fill(i)

h_eta2=TH1F("Eta of h","",10,-8,8)
for i in eta_A0_1:
        h_eta2.Fill(i)



tree1 = ET.parse('/Users/chep/Documents/MG5_aMC_v2_6_5/mywork/pp_zp_a0h_bb_292600_scan/Events/run_03/unweighted_events.lhe')
root1=tree1.getroot()
phi_A0_2=[]
eta_A0_2=[]
pt_A0_2=[]
m_A0_2=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(1111)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(4)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_03")

#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())


       b2=[s for s in lines if s.split()[0]=='25']

       p=[]
       p1=[]
       if b2:
           px=float (b2[0].split()[6])
           py=float (b2[0].split()[7])
           pz=float (b2[0].split()[8])
           e=float (b2[0].split()[9])
           m=float(b2[0].split()[10])
           p=TLorentzVector(px,py,pz,e)
           phi_A0_2.append(p.Phi())
           eta_A0_2.append(p.Eta())
           pt_A0_2.append(p.Pt())


h_pt3=TH1F("pT of h","",100,-100,1000)
for i in pt_A0_2:
        h_pt3.Fill(i)

h_phi3=TH1F("Phi of h","",10,-5,5)
for i in phi_A0_2:
    h_phi3.Fill(i)

h_eta3=TH1F("Eta of h","",10,-8,8)
for i in eta_A0_2:
        h_eta3.Fill(i)



tree1 = ET.parse('/Users/chep/Documents/MG5_aMC_v2_6_5/mywork/pp_zp_a0h_bb_292600_scan/Events/run_04/unweighted_events.lhe')
root1=tree1.getroot()
phi_A0_3=[]
eta_A0_3=[]
pt_A0_3=[]
m_A0_3=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(1111)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(4)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_04")

#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())


       b3=[s for s in lines if s.split()[0]=='25']

       p=[]
       p1=[]
       if b3:
           px=float (b3[0].split()[6])
           py=float (b3[0].split()[7])
           pz=float (b3[0].split()[8])
           e=float (b3[0].split()[9])
           m=float(b3[0].split()[10])
           p=TLorentzVector(px,py,pz,e)
           phi_A0_3.append(p.Phi())
           eta_A0_3.append(p.Eta())
           pt_A0_3.append(p.Pt())


h_pt4=TH1F("pT of h","",100,-100,1000)
for i in pt_A0_3:
    h_pt4.Fill(i)

h_phi4=TH1F("Phi of h","",10,-5,5)
for i in phi_A0_3:
    h_phi4.Fill(i)

h_eta4=TH1F("Eta of h","",10,-8,8)
for i in eta_A0_3:
    h_eta4.Fill(i)



tree1 = ET.parse('/Users/chep/Documents/MG5_aMC_v2_6_5/mywork/pp_zp_a0h_bb_292600_scan/Events/run_05/unweighted_events.lhe')
root1=tree1.getroot()
phi_A0_4=[]
eta_A0_4=[]
pt_A0_4=[]
m_A0_4=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(1111)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(4)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_05")

#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())


       b4=[s for s in lines if s.split()[0]=='25']

       p=[]
       p1=[]
       if b4:
           px=float (b4[0].split()[6])
           py=float (b4[0].split()[7])
           pz=float (b4[0].split()[8])
           e=float (b4[0].split()[9])
           m=float(b4[0].split()[10])
           p=TLorentzVector(px,py,pz,e)
           phi_A0_4.append(p.Phi())
           eta_A0_4.append(p.Eta())
           pt_A0_4.append(p.Pt())


h_pt5=TH1F("pT of h","",100,-100,1000)
for i in pt_A0_4:
        h_pt5.Fill(i)

h_phi5=TH1F("Phi of h","",10,-5,5)
for i in phi_A0_4:
    h_phi5.Fill(i)

h_eta5=TH1F("Eta of A0","",10,-8,8)
for i in eta_A0_4:
        h_eta5.Fill(i)



tree1 = ET.parse('/Users/chep/Documents/MG5_aMC_v2_6_5/mywork/pp_zp_a0h_bb_292600_scan/Events/run_06/unweighted_events.lhe')
root1=tree1.getroot()
phi_A0_5=[]
eta_A0_5=[]
pt_A0_5=[]
m_A0_5=[]
gStyle.SetFrameLineWidth(3)
gStyle.SetOptTitle(0)
gStyle.SetOptStat(1111)
#gStyle.SetLegendBorderSize(2)
gStyle.SetFillColor(4)
gStyle.SetLineWidth(1)
#gStyle.SetPadColor(1)
#legend=TLegend(.63,.69,.87,.89,"","brNDC")
#legend=TLegend(0.57, 0.5, 0.94,0.65,"","run_06")

#lhefdata=LHEFData(float(root.attrib['version']))
for child in root1:
    if(child.tag=='event'):
       lines=child.text.strip().split('\n')
       event_header=lines[0].strip()
       num_part=int(event_header.split()[0].strip())


       b5=[s for s in lines if s.split()[0]=='25']

       p=[]
       p1=[]
       if b5:
           px=float (b5[0].split()[6])
           py=float (b5[0].split()[7])
           pz=float (b5[0].split()[8])
           e=float (b5[0].split()[9])
           m=float(b5[0].split()[10])
           p=TLorentzVector(px,py,pz,e)
           phi_A0_5.append(p.Phi())
           eta_A0_5.append(p.Eta())
           pt_A0_5.append(p.Pt())



h_pt6=TH1F("pT of h","",100,-100,1000)
for i in pt_A0_5:
        h_pt6.Fill(i)

h_phi6=TH1F("Phi of h","",10,-5,5)
for i in phi_A0_5:
    h_phi6.Fill(i)

h_eta6=TH1F("Eta of h","",10,-8,8)
for i in eta_A0_5:
        h_eta6.Fill(i)



c.SetLogy()
gStyle.SetOptStat(1111)


h_pt1.SetXTitle("p_{T} of h[GeV]")
h_pt1.SetYTitle("Events")
h_pt1.SetLineColor(2)

h_pt2.SetXTitle("P_{T} of bb #tilde")
h_pt2.SetYTitle("Events")
h_pt2.SetLineColor(3)

h_pt3.SetXTitle("P_{T} of bb #tilde")
h_pt3.SetYTitle("Events")
h_pt3.SetLineColor(4)

h_pt4.SetXTitle("P_{T} of bb #tilde")
h_pt4.SetYTitle("Events")
h_pt4.SetLineColor(6)

h_pt5.SetXTitle("p_{T} of bb #tilde")
h_pt5.SetYTitle("Events")
h_pt5.SetLineColor(7)

h_pt6.SetXTitle("P_{T} of bb #tilde")
h_pt6.SetYTitle("Events")
h_pt6.SetLineColor(8)

h_pt1.DrawNormalized()
h_pt2.DrawNormalized("Hist&SAME")
h_pt3.DrawNormalized("Hist&SAME")
h_pt4.DrawNormalized("Hist&SAME")
h_pt5.DrawNormalized("Hist&SAME")
h_pt6.DrawNormalized("Hist&SAME")

legend1=TLegend(.63,.69,.87,.89,"","brNDC")
legend1.SetHeader("Legend")
gStyle.SetLegendBorderSize(2);
legend1.AddEntry(h_pt1,"run_01","l")
legend1.AddEntry(h_pt2,"run_02","l")
legend1.AddEntry(h_pt3,"run_03","l")
legend1.AddEntry(h_pt4,"run_04","l")
legend1.AddEntry(h_pt5,"run_05","l")
legend1.AddEntry(h_pt6,"run_06","l")
legend1.Draw("Same")

title1=TPaveLabel(5,39,9.8,46,"p_{T} of h","brndc")
title1.SetFillColor(10)
title1.Draw("Same")

c.SaveAs("Pt of h Combined.png")
c.SaveAs("Pt of h Combined.root")


h_phi1.SetXTitle("#phi_{h}")
h_phi1.SetYTitle("Events")
h_phi1.SetLineColor(2)

h_phi2.SetLineColor(3)

h_phi3.SetLineColor(4)

h_phi4.SetLineColor(6)

h_phi5.SetLineColor(7)

h_phi6.SetLineColor(8)

h_phi1.DrawNormalized()
h_phi2.DrawNormalized("Hist&SAME")
h_phi3.DrawNormalized("Hist&SAME")
h_phi4.DrawNormalized("Hist&SAME")
h_phi5.DrawNormalized("Hist&SAME")
h_phi6.DrawNormalized("Hist&SAME")

legend1=TLegend(.63,.69,.87,.89,"","brNDC")
legend1.SetHeader("Legend")
gStyle.SetLegendBorderSize(2);
legend1.AddEntry(h_phi1,"run_01","l")
legend1.AddEntry(h_phi2,"run_02","l")
legend1.AddEntry(h_phi3,"run_03","l")
legend1.AddEntry(h_phi4,"run_04","l")
legend1.AddEntry(h_phi5,"run_05","l")
legend1.AddEntry(h_phi6,"run_06","l")
legend1.Draw("Same")

title2=TPaveLabel(5,39,9.8,46,"#phi_{h}","brndc")
title2.SetFillColor(10)
title2.Draw("Same")

c.SaveAs("Phi of h Combined.png")
c.SaveAs("Phi of h Combined.root")


h_eta1.SetXTitle("#eta_{h}")
h_eta1.SetYTitle("Events")
h_eta1.SetLineColor(2)

h_eta2.SetLineColor(3)

h_eta3.SetLineColor(4)

h_eta4.SetLineColor(6)

h_eta5.SetLineColor(7)

h_eta6.SetLineColor(8)

h_eta1.DrawNormalized()
h_eta2.DrawNormalized("Hist&SAME")
h_eta3.DrawNormalized("Hist&SAME")
h_eta4.DrawNormalized("Hist&SAME")
h_eta5.DrawNormalized("Hist&SAME")
h_eta6.DrawNormalized("Hist&SAME")

legend1=TLegend(.63,.69,.87,.89,"","brNDC")
legend1.SetHeader("Legend")
gStyle.SetLegendBorderSize(2);
legend1.AddEntry(h_eta1,"run_01","l")
legend1.AddEntry(h_eta2,"run_02","l")
legend1.AddEntry(h_eta3,"run_03","l")
legend1.AddEntry(h_eta4,"run_04","l")
legend1.AddEntry(h_eta5,"run_05","l")
legend1.AddEntry(h_eta6,"run_06","l")
legend1.Draw("Same")

title3=TPaveLabel(5,39,9.8,46,"#eta_{h}","brndc")
title3.SetFillColor(10)
title3.Draw("Same")

c.SaveAs("Eta of h Combined.png")
c.SaveAs("Eta of h Combined.root")
