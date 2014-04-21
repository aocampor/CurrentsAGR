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
            if( entr%1000 == 0 ):
                #update_progress( float(entr/en)  )
                sys.stdout.flush()
                print entr, 'over', en ,  str(float(entr/en) ), '%'
            if( sys.argv[1] == 'Filter'):
                  if( filter(ev.Day, ev.Hour, ev.Minute) == 1):
                        continue
            cu = ev.Current
            we = ev.Wheel
            la = ev.Layer
            se = ev.Sector
            ch = ev.Chamber
            name = 'Wheel' + str( get_wheel( we ) ) + 'S' + str(se) + str(get_chamber(ch,la,se)) 
            tim = TDatime(2014,04,ev.Day,ev.Hour,ev.Minute,ev.Second)
            histories[name+'Time'].append(tim.Convert())
            histories[name+'Current'].append(ev.Current)

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
