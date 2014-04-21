import sys,os
from ROOT import *
from array import array

if __name__ == "__main__":

    lines = [line.strip() for line in open('RE4Currents_work.txt')]
    #print lines
    alias = ''
    date = ''
    tree_file = TFile("Currents_tree.root","RECREATE")
    tree = TTree("T1","Tree currents");
    current = array('f',[0])
    disk = array('i',[0])
    ring = array('i',[0])
    chamber = array('i',[0])
    day = array('i',[0])
    hour = array('i',[0])
    minute = array('i',[0])
    second = array('i',[0])
    milisecond = array('i',[0])
    tree.Branch('Current',current,'Current/F')
    tree.Branch('Disk',disk,'Disk/I')
    tree.Branch('Ring',ring,'Ring/I')
    tree.Branch('Chamber',chamber,'Chamber/I')
    tree.Branch('Day',day,'Day/I')
    tree.Branch('Hour',hour,'Hour/I')
    tree.Branch('Minute',minute,'Minute/I')
    tree.Branch('Second',second,'Second/I')
    tree.Branch('MiliSecond',milisecond,'MiliSecond/I')
    current[0] = -1
    disk[0] = -1
    ring[0] = -1
    chamber[0] = -1
    day[0] = -1
    hour[0] = -1
    minute[0] = -1
    second[0] = -1
    milisecond[0] = -1
    #print current
    for line in lines:
        #print line
        #print line.rsplit('RPC')
        if( len(line.rsplit('RPC')) > 1):
            alias = line
            di = alias.rsplit('_')[1]
            ri = alias.rsplit('_')[2]
            if(di == 'EP1'):
                disk[0] = 1
                chamber[0] = int(alias.rsplit('_C')[1])
                if( ri == 'R2' ):
                    ring[0] = 2
                else:
                    ring[0] = 3
            else:
                ring[0] = 2
                ch = alias.rsplit('_')[4]
                #print ch.rsplit('C')
                chamber[0] = int(ch.rsplit('C')[1])
                if(di == 'EP2'):
                    disk[0] = 2
                elif(di == 'EP3'):
                    disk[0] = 3
                elif(di == 'EP4'):
                    disk[0] = 4
                    
        elif( len(line.rsplit('-APR-14')) > 1):
            date = line
            ar = date.rsplit('-APR-14 ')
            day[0] = int(ar[0])
            ar1 = ar[1]
            #print ar1.rsplit('.')[0]
            hour[0] = int(ar1.rsplit('.')[0])
            minute[0] = int(ar1.rsplit('.')[1])
            second[0] = int(ar1.rsplit('.')[2])
            mi = ar1.rsplit('.')[3]
            milisecond[0] = int(mi[:-9])
            if( ar1.rsplit(' ')[1] == 'AM' and hour[0] == 12):
                hour[0] = 0
            elif( ar1.rsplit(' ')[1] == 'PM' and hour[0] != 12 ):
                hour[0] = hour[0] + 12
            
        elif( len(line.rsplit('1')) > 1 or len(line.rsplit('2')) > 1 or len(line.rsplit('3')) > 1 or 
              len(line.rsplit('4')) > 1 or len(line.rsplit('5')) > 1 or len(line.rsplit('6')) > 1 or 
              len(line.rsplit('7')) > 1 or len(line.rsplit('8')) > 1 or len(line.rsplit('9')) > 1 or len(line.rsplit('0')) > 1 ):    
            current[0] = float(line)
            #print current
            
        if (alias != '' and current[0] != -1 and date != ''):    
            print alias, date, current[0] 
            print disk[0], ring[0], chamber[0], day[0], hour[0], minute[0], second[0], milisecond[0]
            tree.Fill()
            alias = ''
            current[0] = -1
            date = ''
    tree.Write()        
    tree_file.Close()        
