import sys,os
from ROOT import *
from array import array
import datetime
import random
import matplotlib.pyplot as plt
import time
sys.path.append('useful_func.py')
from useful_func import *

if __name__ == "__main__":
      
      file_name = TFile.Open("ROOT/Barrel_Currents_tree.root")
      tree = file_name.Get('T1')

      histories = {}
      
      for i in range(-2,3):
            for j in range(1,13):
                  for k in range(1,7):
                        if( k < 5):
                              name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(1,k,j) + 'Time'
                              histories[name] = []
                              name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(1,k,j) + 'Current'
                              histories[name] = []
                        else:    
                              for l in range(1,6):
                                    if(get_chamber(l,k,j) != '-1' ):
                                          name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(l,k,j) + 'Time'
                                          histories[name] = []
                                          name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(l,k,j) + 'Current'
                                          histories[name] = []
      
                        
      outfile = TFile("ROOT/current_history_barrel.root","RECREATE") 

      en = tree.GetEntries()
      entr = 0      
      for ev in tree:
            entr = entr + 1
            cu = ev.Current
            we = ev.Wheel
            la = ev.Layer
            se = ev.Sector
            ch = ev.Chamber
            da = ev.Day
            ho = ev.Hour 
            mi = ev.Minute
            sec = ev.Second
            if( sys.argv[1] == 'Filter'):
                  if( entr%1000 == 0 ):
                        update_progress( float(entr)/float(en)  )
                  if( filter_barrel(da, ho, mi) == 1):
                        continue
            if( cu > 20 and we == 0 and se == 1 and get_chamber(ch,la,se) == 'RB2in' ):
                  print cu, da, ho, mi, sec 
            name = 'Wheel' + str( get_wheel( we ) ) + 'S' + str(se) + str(get_chamber(ch,la,se)) 
            tim = TDatime(2014,04,da,ho,mi,sec)
            histories[name+'Time'].append(tim.Convert())
            histories[name+'Current'].append(cu)

      c1 = TCanvas()                  

      for i in range(-2,3):
          for j in range(1,13):
              for k in range(1,7):
                  if( k < 5):
                      if(get_chamber(1,k,j) != '-1'):
                          name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(1,k,j) + 'Time'
                          name1 = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(1,k,j) + 'Current'
                          plot_name = 'plots/'+'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(1,k,j) + '_history.png'
                          #print len(histories[name]),len (array('d',histories[name])), len(array('d',histories[name1]))
                          if(len(histories[name]) == 0):
                              continue
                          g1 = TGraph(len(histories[name]),array('d',histories[name]),array('d',histories[name1]))
                          g1.SetMarkerStyle(20) 
                          g1.GetXaxis().SetTimeDisplay(1) 
                          g1.GetXaxis().SetNdivisions(-503) 
                          g1.GetXaxis().SetTimeFormat("%d %H:%M") 
                          g1.GetXaxis().SetTimeOffset(0,"gmt") 
                          g1.Draw('AP')
                          c1.SaveAs(plot_name)
                          g1.Write()

                  else:    
                      for l in range(1,6):
                          if(get_chamber(l,k,j) != '-1' ):
                              name = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(l,k,j) + 'Time'
                              name1 = 'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(l,k,j) + 'Current'
                              plot_name = 'plots/'+'Wheel' + get_wheel(i) + 'S' + str(j) + get_chamber(l,k,j) + '_history.png'
                              #print name, name1  
                              #print len(histories[name]),len(array('d',histories[name])),len(array('d',histories[name1]))
                              if(len(histories[name]) == 0 ):
                                  continue
                              g1 = TGraph(len(histories[name]),array('d',histories[name]),array('d',histories[name1]))
                              g1.SetMarkerStyle(20) 
                              g1.GetXaxis().SetTimeDisplay(1) 
                              g1.GetXaxis().SetNdivisions(-503) 
                              g1.GetXaxis().SetTimeFormat("%d %H:%M") 
                              g1.GetXaxis().SetTimeOffset(0,"gmt") 
                              g1.Draw('AP')
                              c1.SaveAs(plot_name)
                              g1.Write()
                                          

      outfile.Close()
      file_name.Close() 
