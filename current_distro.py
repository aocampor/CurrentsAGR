import sys,os
from ROOT import *
from array import array
sys.path.append('useful_func.py')
from useful_func import *

if __name__ == "__main__":
      
      file_nam = 'ROOT/current_distros_NoPeak.root'
      file_nam1 = 'ROOT/barrel_current_distros_NoPeak.root'
      
      #if(sys.argv[1] and sys.argv[2]):
      #      file_nam = sys.argv[1]
      #      file_nam1 = sys.argv[2]
      
      file_name = TFile.Open(file_nam)
      file_name1 = TFile.Open(file_nam1)
      outfile = TFile("ROOT/Current_means.root","RECREATE")
      histos = {}
      
      for i in range(1,5):
            name = 'Disk'+ str(i) + 'Means'
            histos[name] = TH1D(name,name,20,0,10);
      for i in range(-2,1):
            name = 'Wheel'+ get_wheel(i) + 'Means'
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
      
      for i in range(-2,1):            
            for j in range(1,13):
                  for k in range(1,7):
                        for l in range(1,6):
                              if(get_chamber(l,k,j) != '-1'):
                                    name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(l,k,j) 
                                    name1 = 'Wheel' + get_wheel(i) + 'Means'
                                    h = file_name1.Get(name)
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

      c1 = TCanvas()
      histos['WheelM2Means'].SetLineColor(1)
      histos['WheelM2Means'].SetLineWidth(4)
      histos['WheelM2Means'].Draw()
      histos['WheelM1Means'].SetLineColor(2)
      histos['WheelM1Means'].SetLineWidth(3)
      histos['WheelM1Means'].Draw('SAMES')
      histos['Wheel00Means'].SetLineColor(4)
      histos['Wheel00Means'].SetLineWidth(2)
      histos['Wheel00Means'].Draw('SAMES')

      c1.Write()


      histo = TH1D('SummaryMeanCurrents','',7,0,7)
      histo.SetBinContent(1,histos['WheelM2Means'].GetMean())
      histo.SetBinError(1,histos['WheelM2Means'].GetMeanError())
      histo.SetBinContent(2,histos['WheelM1Means'].GetMean())
      histo.SetBinError(2,histos['WheelM1Means'].GetMeanError())
      histo.SetBinContent(3,histos['Wheel00Means'].GetMean())
      histo.SetBinError(3,histos['Wheel00Means'].GetMeanError())
      histo.SetBinContent(4, histos['Disk1Means'].GetMean() )
      histo.SetBinError(4, histos['Disk1Means'].GetMeanError())
      histo.SetBinContent(5,histos['Disk2Means'].GetMean())
      histo.SetBinError(5,histos['Disk2Means'].GetMeanError())
      histo.SetBinContent(6,histos['Disk3Means'].GetMean())
      histo.SetBinError(6,histos['Disk3Means'].GetMeanError())
      histo.SetBinContent(7,histos['Disk4Means'].GetMean())
      histo.SetBinError(7,histos['Disk4Means'].GetMeanError())

      histo1 = TH1D('SummaryRMSCurrents','',7,0,7)
      histo1.SetBinContent(1,histos['WheelM2Means'].GetRMS())
      histo1.SetBinError(1,histos['WheelM2Means'].GetRMSError())
      histo1.SetBinContent(2,histos['WheelM1Means'].GetRMS())
      histo1.SetBinError(2,histos['WheelM1Means'].GetRMSError())
      histo1.SetBinContent(3,histos['Wheel00Means'].GetRMS())
      histo1.SetBinError(3,histos['Wheel00Means'].GetRMSError())
      histo1.SetBinContent(4, histos['Disk1Means'].GetRMS() )
      histo1.SetBinError(4, histos['Disk1Means'].GetRMSError())
      histo1.SetBinContent(5,histos['Disk2Means'].GetRMS())
      histo1.SetBinError(5,histos['Disk2Means'].GetRMSError())
      histo1.SetBinContent(6,histos['Disk3Means'].GetRMS())
      histo1.SetBinError(6,histos['Disk3Means'].GetRMSError())
      histo1.SetBinContent(7,histos['Disk4Means'].GetRMS())
      histo1.SetBinError(7,histos['Disk4Means'].GetRMSError())
      
      c1 = TCanvas()
      gStyle.SetOptStat(0)
      histo.SetMarkerStyle(21)
      histo.SetMarkerColor(2)
      histo.SetMarkerSize(2)
      c1.SetTickx(1)
      c1.SetTicky(1)
      xaxis = histo.GetXaxis()
      xaxis.SetBinLabel(1,'Wheel -2')
      xaxis.SetBinLabel(2,'Wheel -1')
      xaxis.SetBinLabel(3,'Wheel 0')
      xaxis.SetBinLabel(4,'Disk +1')
      xaxis.SetBinLabel(5,'Disk +2')
      xaxis.SetBinLabel(6,'Disk +3')
      xaxis.SetBinLabel(7,'Disk +4')
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
      xaxis.SetBinLabel(1,'Wheel -2')
      xaxis.SetBinLabel(2,'Wheel -1')
      xaxis.SetBinLabel(3,'Wheel 0')
      xaxis.SetBinLabel(4,'Disk +1')
      xaxis.SetBinLabel(5,'Disk +2')
      xaxis.SetBinLabel(6,'Disk +3')
      xaxis.SetBinLabel(7,'Disk +4')
      yaxis = histo1.GetYaxis()
      yaxis.SetTitle('RMS Current #mu A')
      histo1.Draw()
      c1.SaveAs('plots/RMSCurrent.png')

      outfile.Close()      
      file_name.Close() 
      file_name1.Close() 
