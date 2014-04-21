import sys,os
from ROOT import *
from array import array

def get_layer(la):
    if(la == 'RB1in'):
        return 1
    elif(la == 'RB1out'):
        return  2
    elif(la == 'RB2in'):
        return  3
    elif(la == 'RB2out'):
        return  4
    elif( len(la.rsplit('RB3')) > 1):
        return  5
    elif( len(la.rsplit('RB4')) > 1):
        return  6
    return  -1    

def get_chamber(la):
    if(la == 'RB1in'):
        return 1
    elif(la == 'RB1out'):
        return  2
    elif(la == 'RB2in'):
        return  1
    elif(la == 'RB2out'):
        return  2
    elif( la == 'RB3plus' ):
        return  1
    elif( la == 'RB3minus' ):
        return  2
    elif( la == 'RB4'):
        return  1
    elif( la == 'RB4plus'):
        return  2
    elif( la == 'RB4minus'):
        return  3
    elif( la == 'RB4plusplus'):
        return  4
    elif( la == 'RB4minusminus'):
        return  5
    return  -1    
        


if __name__ == "__main__":

    lines = [line.strip() for line in open('BarrelCurrents_work.txt')]
    #print lines
    alias = ''
    date = ''
    tree_file = TFile("Barrel_Currents_tree.root","RECREATE")
    tree = TTree("T1","Tree currents");
    current = array('f',[0])
    wheel = array('i',[0])
    sector = array('i',[0])
    layer = array('i',[0])
    chamber = array('i',[0])
    day = array('i',[0])
    hour = array('i',[0])
    minute = array('i',[0])
    second = array('i',[0])
    milisecond = array('i',[0])
    tree.Branch('Current',current,'Current/F')
    tree.Branch('Wheel',wheel,'Wheel/I')
    tree.Branch('Sector',sector,'Sector/I')
    tree.Branch('Layer',layer,'Layer/I')
    tree.Branch('Chamber',chamber,'Chamber/I')
    tree.Branch('Day',day,'Day/I')
    tree.Branch('Hour',hour,'Hour/I')
    tree.Branch('Minute',minute,'Minute/I')
    tree.Branch('Second',second,'Second/I')
    tree.Branch('MiliSecond',milisecond,'MiliSecond/I')
    current[0] = -1
    wheel[0] = -3
    layer[0] = -1
    chamber[0] = -1
    sector[0] = -1
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
            la = alias.rsplit('_')[3]
            if(di == 'WM2'):
                wheel[0] = -2
            elif(di == 'WM1'):
                wheel[0] = -1
            elif(di == 'W00'):
                wheel[0] = 0
            elif(di == 'WP1'):
                wheel[0] = 1
            elif(di == 'WP2'):
                wheel[0] = 2

            sector[0] = int( ri.rsplit('S')[1] )
            chamber[0] = get_chamber(la)
            layer[0] = get_layer(la)
                    
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
            print wheel[0], layer[0], sector[0], chamber[0], day[0], hour[0], minute[0], second[0], milisecond[0]
            tree.Fill()
            alias = ''
            current[0] = -1
            date = ''
    tree.Write()        
    tree_file.Close()        
