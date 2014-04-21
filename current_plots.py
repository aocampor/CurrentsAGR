import sys,os
from ROOT import *
from array import array
#import numpy as np

if __name__ == "__main__":
      
      file_name = TFile.Open("Currents_tree.root")
      tree = file_name.Get('T1')

      histories = {}

      histos = {}

      histos['Disk1'] = TH1D("Disk1_Currents","",125,0,50)
      histos['Disk2'] = TH1D("Disk2_Currents","",125,0,50)
      histos['Disk3'] = TH1D("Disk3_Currents","",125,0,50)
      histos['Disk4'] = TH1D("Disk4_Currents","",125,0,50)

      histos['Disk1Ring2'] = TH1D("Disk1_Ring2_Currents","",125,0,50)
      histos['Disk1Ring3'] = TH1D("Disk1_Ring3_Currents","",125,0,50)

      for i in range(1,5):
            for j in range(1,37): 
                  if(i == 1):
                        if( j%2 != 0):
                              key = 'Disk' + str(i) + 'Ring2C' + str(j)
                              Name = 'Disk' + str(i) + '_Ring2_C' + str(j) + '_Currents'
                              histos[key] = TH1D(Name,"",125,0,50)
                              key = 'Disk' + str(i) + 'Ring3C' + str(j)
                              Name = 'Disk' + str(i) + '_Ring3_C' + str(j) + '_Currents'
                              histos[key] = TH1D(Name,"",125,0,50)
                  elif( i >= 2):
                        key = 'Disk' + str(i) + 'C' + str(j)
                        Name = 'Disk' + str(i) + '_C' + str(j) + '_Currents'
                        histos[key] = TH1D(Name,"",125,0,50)
                        
      

      outfile = TFile("current_distros.root","RECREATE") 

      for ev in tree:
            if( sys.argv[1] == 'Filter'):
                  if( 
                              (ev.Day == 7 and ( ev.Hour == 7  and (ev.Minute >= 19 and ev.Minute <= 24))) or 
                              (ev.Day == 7 and ( ev.Hour == 7  and (ev.Minute >= 41 and ev.Minute <= 50))) or 
                              #(ev.Day == 7 and ( ev.Hour == 9  and (ev.Minute >= 44 and ev.Minute <= 44))) or 
                              (ev.Day == 7 and ( ev.Hour == 10 and (ev.Minute >= 26 and ev.Minute <= 28))) or
                              (ev.Day == 7 and ( ev.Hour == 11 and (ev.Minute >= 1 and ev.Minute <= 9))) or
                              (ev.Day == 7 and ( ev.Hour == 19 and (ev.Minute >= 6 and ev.Minute <= 11))) or
                              (ev.Day == 8 and ( ev.Hour == 7 and (ev.Minute >= 11 and ev.Minute <= 13))) or
                              (ev.Day == 8 and ( ev.Hour == 11 and (ev.Minute >= 36 and ev.Minute <= 40))) or
                              (ev.Day == 9 and ( ev.Hour == 15 and (ev.Minute >= 3 and ev.Minute <= 6))) or
                              (ev.Day == 9 and ( ev.Hour == 16 and (ev.Minute >= 24 and ev.Minute <= 25))) or
                              (ev.Day == 10 and ( ev.Hour == 1 and (ev.Minute >= 3 and ev.Minute <= 8))) or
                              (ev.Day == 10 and ( ev.Hour == 1 and (ev.Minute >= 12 and ev.Minute <= 14))) or
                              (ev.Day == 10 and ( ev.Hour == 13 and (ev.Minute >= 0 and ev.Minute <= 6))) or
                              (ev.Day == 11 and ( ev.Hour == 13 and (ev.Minute >= 0 and ev.Minute <= 3))) or
                              (ev.Day == 11 and ( ev.Hour == 15 and (ev.Minute >= 1 and ev.Minute <= 5))) or
                              (ev.Day == 11 and ( ev.Hour == 14 and (ev.Minute >= 42 and ev.Minute <= 46))) or
                              (ev.Day == 11 and (ev.Hour == 14 and (ev.Minute >= 52 and ev.Minute <= 54)))
                  ):
                        continue

            if(ev.Disk == 1):
                  histos['Disk1'].Fill(ev.Current)
                  key = 'Disk' + str(ev.Disk) + 'Ring' + str(ev.Ring) +  'C' + str(ev.Chamber)
                  histos[key].Fill(ev.Current)
                  if(ev.Ring == 2):
                        histos['Disk1Ring2'].Fill(ev.Current)                        
                  elif(ev.Ring == 3):
                        histos['Disk1Ring3'].Fill(ev.Current)                        
            else:       
                  key = 'Disk' + str(ev.Disk) + 'C' + str(ev.Chamber)
                  histos[key].Fill(ev.Current)
                  if(ev.Disk == 2):
                        histos['Disk2'].Fill(ev.Current)
                  elif(ev.Disk == 3):
                        histos['Disk3'].Fill(ev.Current)
                  elif(ev.Disk == 4):
                        histos['Disk4'].Fill(ev.Current)

      c1 = TCanvas()                  
      c1.SetFillColor(0)

      for item in histos:
            histos[item].SetLineColor(2)
            histos[item].SetLineWidth(2)
            xaxis = histos[item].GetXaxis()
            xaxis.SetTitle('Currents (#mu A)')
            xaxis.SetRangeUser(0,15)
            histos[item].DrawNormalized()
            c1.SaveAs('plots/' + item + '.png')
            histos[item].Write()


      histos['Disk1'].SetLineColor(1)      
      histos['Disk2'].SetLineColor(2)      
      histos['Disk3'].SetLineColor(3)      
      histos['Disk4'].SetLineColor(4)      
      legend=TLegend(0.6,0.6,0.8,0.8)
      legend.AddEntry(histos['Disk1'], histos['Disk1'].GetName(), "l")
      legend.AddEntry(histos['Disk2'], histos['Disk2'].GetName(), "l")
      legend.AddEntry(histos['Disk3'], histos['Disk3'].GetName(), "l")
      legend.AddEntry(histos['Disk4'], histos['Disk4'].GetName(), "l")
      histos['Disk1'].DrawNormalized()
      histos['Disk2'].DrawNormalized("SAMES")
      histos['Disk3'].DrawNormalized("SAMES")
      histos['Disk4'].DrawNormalized("SAMES")
      legend.Draw('SAME')
      c1.SaveAs('plots/DisksComparison.png')

      c1.Write()
      
      outfile.Close()
      file_name.Close() 
