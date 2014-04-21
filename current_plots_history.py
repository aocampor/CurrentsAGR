import sys,os
from ROOT import *
from array import array
import datetime
import random
import matplotlib.pyplot as plt
import time
#import numpy as np

if __name__ == "__main__":
      
      file_name = TFile.Open("Currents_tree.root")
      tree = file_name.Get('T1')

      histories = {}
      
      sti = 1
      endi = 5
 
      for i in range(sti,endi):
            for j in range(1,37): 
                  if(i == 1):
                        if( j%2 != 0):
                              keyx = 'Disk' + str(i) + 'Ring2C' + str(j) + 'Time'
                              keyy = 'Disk' + str(i) + 'Ring2C' + str(j) + 'Current'
                              histories[keyx] = []
                              histories[keyy] = []
                              keyx = 'Disk' + str(i) + 'Ring3C' + str(j) + 'Time'
                              keyy = 'Disk' + str(i) + 'Ring3C' + str(j) + 'Current'
                              histories[keyx] = []
                              histories[keyy] = []
                  elif( i >= 2):
                        keyx = 'Disk' + str(i) + 'C' + str(j) + 'Time'
                        keyy = 'Disk' + str(i) + 'C' + str(j) + 'Current'
                        histories[keyx] = []
                        histories[keyy] = []
                        
      outfile = TFile("current_history.root","RECREATE") 

      for ev in tree:
            if( sys.argv[1] == 'Filter'):
                  if( (ev.Day == 7 and ( ev.Hour == 7  and (ev.Minute >= 19 and ev.Minute <= 24))) or 
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

            #if(ev.Current > 8 and ev.Disk == 1 and ev.Chamber == 23 and ev.Ring == 3):
            #      print ev.Current , ev.Day, ev.Hour, ev.Minute , ev.Second 
            if(ev.Disk == 1):
                  keyx = 'Disk' + str(ev.Disk) + 'Ring' + str(ev.Ring) +  'C' + str(ev.Chamber) + 'Time'
                  keyy = 'Disk' + str(ev.Disk) + 'Ring' + str(ev.Ring) +  'C' + str(ev.Chamber) + 'Current'
                  tim = TDatime(2014,04,ev.Day,ev.Hour,ev.Minute,ev.Second)
                  histories[keyx].append(tim.Convert())#time.mktime(time.strptime(str(ev.Day) +'.' + '04.2014 '+str(ev.Hour) +':' +str(ev.Minute)+':'+str(ev.Second), "%d.%m.%Y %H:%M:%S")))
                  histories[keyy].append(float(ev.Current))
            else:       
                  keyx = 'Disk' + str(ev.Disk) + 'C' + str(ev.Chamber) + 'Time'
                  keyy = 'Disk' + str(ev.Disk) + 'C' + str(ev.Chamber) + 'Current'
                  tim = TDatime(2014,04,ev.Day,ev.Hour,ev.Minute,ev.Second)
                  histories[keyx].append(tim.Convert())#time.mktime(time.strptime(str(ev.Day) +'.' + '04.2014 '+str(ev.Hour) +':' +str(ev.Minute)+':'+str(ev.Second), "%d.%m.%Y %H:%M:%S")) )
                  histories[keyy].append(float(ev.Current))


      
      c1 = TCanvas()                  

      for i in range(sti,endi):
            for j in range(1,37): 
                  if(i == 1):
                        if( j%2 != 0):
                              keyx = 'Disk' + str(i) + 'Ring2C' + str(j) + 'Time'
                              keyy = 'Disk' + str(i) + 'Ring2C' + str(j) + 'Current'
                              plot_name = 'plots/Disk' + str(i) + 'Ring2C' + str(j) + '_history.png'
                              g1 = TGraph(len(histories[keyx]),array('d',histories[keyx]),array('d',histories[keyy]))
                              g1.SetMarkerStyle(20) 
                              g1.GetXaxis().SetTimeDisplay(1) 
                              g1.GetXaxis().SetNdivisions(-503) 
                              g1.GetXaxis().SetTimeFormat("%d %H:%M") 
                              g1.GetXaxis().SetTimeOffset(0,"gmt") 
                              g1.Draw('AP')
                              c1.SaveAs(plot_name)
                              g1.Write()
                              keyx = 'Disk' + str(i) + 'Ring3C' + str(j) + 'Time'
                              keyy = 'Disk' + str(i) + 'Ring3C' + str(j) + 'Current'
                              plot_name = 'plots/Disk' + str(i) + 'Ring3C' + str(j) + '_history.png'
                              g1 = TGraph(len(histories[keyx]),array('d',histories[keyx]),array('d',histories[keyy]))
                              g1.SetMarkerStyle(20) 
                              g1.Draw("AP") 
                              g1.GetXaxis().SetTimeDisplay(1) 
                              g1.GetXaxis().SetNdivisions(-503) 
                              g1.GetXaxis().SetTimeFormat("%d %H:%M") 
                              g1.GetXaxis().SetTimeOffset(0,"gmt") 
                              c1.SaveAs(plot_name)
                              g1.Write()
                  
                  elif( i >= 2):
                        keyx = 'Disk' + str(i) + 'C' + str(j) + 'Time'
                        keyy = 'Disk' + str(i) + 'C' + str(j) + 'Current'
                        plot_name = 'plots/Disk' + str(i) + 'C' + str(j) + '_history.png'
                        g1 = TGraph(len(histories[keyx]),array('d',histories[keyx]),array('d',histories[keyy]))
                        g1.SetMarkerStyle(20) 
                        g1.Draw("AP") 
                        g1.GetXaxis().SetTimeDisplay(1) 
                        g1.GetXaxis().SetNdivisions(-503) 
                        g1.GetXaxis().SetTimeFormat("%d %H:%M") 
                        g1.GetXaxis().SetTimeOffset(0,"gmt") 
                        c1.SaveAs(plot_name)
                        g1.Write()


      outfile.Close()
      file_name.Close() 
