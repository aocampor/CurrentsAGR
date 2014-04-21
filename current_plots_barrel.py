import sys,os
from ROOT import *
from array import array
sys.path.append('useful_func.py')
from useful_func import *

if __name__ == "__main__":
      
      file_name = TFile.Open("ROOT/Barrel_Currents_tree.root")
      tree = file_name.Get('T1')

      histos = {}

      for i in range(-2,3):
            name = 'Wheel' + get_wheel(i) 
            histos[name] = TH1D(name,'',125,0,50)
            for j in range(1,13):
                  name1 = name + 'S' + str(j)
                  histos[name1] = TH1D(name1,'',125,0,50)
                  for k in range(1,7):
                      if( k < 5):
                          if(get_chamber(1,k,j) != '-1' ):
                              name2 = name1 + get_chamber(1,k,j)
                              histos[name2] = TH1D(name2,'',125,0,50)
                      else:    
                          for l in range(1,6):
                              if(get_chamber(l,k,j) != '-1' ):
                                    name2 = name1 + get_chamber(l,k,j)
                                    histos[name2] = TH1D(name2,'',125,0,50)
            for j in range(1,7):
                  name1 = name +  get_layer(j)
                  histos[name1] = TH1D(name1,'',125,0,50)

      outfile = TFile("ROOT/barrel_current_distros.root","RECREATE") 

      en = tree.GetEntries()
      entr = 0
      for ev in tree:
            entr = entr + 1
            if( entr%1000 == 0 or entr == 1):
                  update_progress( float(entr)/float(en)  )
            if( sys.argv[1] == 'Filter'):
                if(filter_barrel(ev.Day , ev.Hour, ev.Minute) == 1):
                    continue
            cu = ev.Current
            we = ev.Wheel
            la = ev.Layer
            se = ev.Sector
            ch = ev.Chamber
            name = 'Wheel' + str( get_wheel( we ) )            
            histos[name].Fill(cu)
            namel = name + str( get_layer( la ) )
            histos[namel].Fill(cu)
            name = name + 'S' + str(se)
            histos[name].Fill(cu)
            if(get_chamber(ch,la,se) != -1):
                name = name + str(get_chamber(ch,la,se))
                histos[name].Fill(cu)
            
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


      histos['WheelM2'].SetLineColor(1)      
      histos['WheelM1'].SetLineColor(2)      
      histos['Wheel00'].SetLineColor(4)      
      legend=TLegend(0.6,0.6,0.8,0.8)
      legend.AddEntry(histos['WheelM2'], histos['WheelM2'].GetName(), "l")
      legend.AddEntry(histos['WheelM1'], histos['WheelM1'].GetName(), "l")
      legend.AddEntry(histos['Wheel00'], histos['Wheel00'].GetName(), "l")
      histos['WheelM2'].DrawNormalized()
      histos['WheelM1'].DrawNormalized("SAMES")
      histos['Wheel00'].DrawNormalized("SAMES")
      legend.Draw('SAME')
      c1.SaveAs('plots/WheelsComparison.png')

      c1.Write()
      
      outfile.Close()
      file_name.Close() 
