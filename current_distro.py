import sys,os
from ROOT import *
from array import array
#import numpy as np

if __name__ == "__main__":
      
      file_nam = 'current_distros.root'
      
      if(sys.argv[1]):
            file_nam = sys.argv[1]
      
      file_name = TFile.Open(file_nam)
      outfile = TFile("Current_means.root","RECREATE")
      histos = {}
      
      for i in range(1,5):
            name = 'Disk'+ str(i) + 'Means'
            histos[name] = TH1D(name,name,20,0,10);

      for i in range(1,5):
            if( i == 1):
                  for j in range(2,4):
                        for k in range(1,19):

                              name = 'Disk' + str(i) + '_Ring' + str(j) + '_C' + str(k*2 - 1) + '_Currents'
                              print name
                              name1 = 'Disk'+ str(i) + 'Means'
                              h = file_name.Get(name)
                              histos[name1].Fill(h.GetMean())
            elif( i > 1):
                  for k in range(1,37):
                        name = 'Disk' + str(i) + '_C' + str(k) + '_Currents'
                        #print name
                        name1 = 'Disk'+ str(i) + 'Means'
                        h = file_name.Get(name)
                        histos[name1].Fill(h.GetMean())
      
      for item in histos:
            histos[item].Write()

      c1 = TCanvas()
      histos['Disk1Means'].SetLineColor(1)
      histos['Disk1Means'].SetLineWidth(4)
      histos['Disk1Means'].Draw()
      histos['Disk2Means'].SetLineColor(2)
      histos['Disk2Means'].SetLineWidth(3)
      histos['Disk2Means'].Draw('SAMES')
      histos['Disk3Means'].SetLineColor(3)
      histos['Disk3Means'].SetLineWidth(2)
      histos['Disk3Means'].Draw('SAMES')
      histos['Disk4Means'].SetLineColor(4)
      histos['Disk4Means'].SetLineWidth(1)
      histos['Disk4Means'].Draw('SAMES')

      c1.Write()

      histo = TH1D('SummaryMeanCurrents','',4,0,4)
      histo.SetBinContent(1, histos['Disk1Means'].GetMean() )
      histo.SetBinError(1, histos['Disk1Means'].GetMeanError())
      histo.SetBinContent(2,histos['Disk2Means'].GetMean())
      histo.SetBinError(2,histos['Disk2Means'].GetMeanError())
      histo.SetBinContent(3,histos['Disk3Means'].GetMean())
      histo.SetBinError(3,histos['Disk3Means'].GetMeanError())
      histo.SetBinContent(4,histos['Disk4Means'].GetMean())
      histo.SetBinError(4,histos['Disk4Means'].GetMeanError())

      histo1 = TH1D('SummaryRMSCurrents','',4,0,4)
      histo1.SetBinContent(1, histos['Disk1Means'].GetRMS() )
      histo1.SetBinError(1, histos['Disk1Means'].GetRMSError())
      histo1.SetBinContent(2,histos['Disk2Means'].GetRMS())
      histo1.SetBinError(2,histos['Disk2Means'].GetRMSError())
      histo1.SetBinContent(3,histos['Disk3Means'].GetRMS())
      histo1.SetBinError(3,histos['Disk3Means'].GetRMSError())
      histo1.SetBinContent(4,histos['Disk4Means'].GetRMS())
      histo1.SetBinError(4,histos['Disk4Means'].GetRMSError())
      
      c1 = TCanvas()
      gStyle.SetOptStat(0)
      histo.SetMarkerStyle(21)
      histo.SetMarkerColor(2)
      histo.SetMarkerSize(2)
      c1.SetTickx(1)
      c1.SetTicky(1)
      xaxis = histo.GetXaxis()
      xaxis.SetBinLabel(1,'Disk +1')
      xaxis.SetBinLabel(2,'Disk +2')
      xaxis.SetBinLabel(3,'Disk +3')
      xaxis.SetBinLabel(4,'Disk +4')
      yaxis = histo.GetYaxis()
      yaxis.SetTitle('Mean Current #mu A')
      histo.Draw()
      c1.SaveAs('plots/MeanCurrent.png')
      
      histo1.SetMarkerStyle(21)
      histo1.SetMarkerColor(2)
      histo1.SetMarkerSize(2)
      c1.SetTickx(1)
      c1.SetTicky(1)
      xaxis = histo1.GetXaxis()
      xaxis.SetBinLabel(1,'Disk +1')
      xaxis.SetBinLabel(2,'Disk +2')
      xaxis.SetBinLabel(3,'Disk +3')
      xaxis.SetBinLabel(4,'Disk +4')
      yaxis = histo1.GetYaxis()
      yaxis.SetTitle('RMS Current #mu A')
      histo1.Draw()
      c1.SaveAs('plots/RMSCurrent.png')

      outfile.Close()      
      file_name.Close() 
