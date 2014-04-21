import sys, os

def get_layer(la):
    if(la == 1):
        return 'RB1in'
    elif(la == 2):
        return  'RB1out'
    elif(la == 3):
        return  'RB2in'
    elif(la == 4):
        return  'RB2out'
    elif( la == 5 ):
        return  'RB3'
    elif( la == 6):
        return  'RB4'
    return  -1    

def get_chamber(k,l,m):

    if( l == 1):
        return 'RB1in'
    elif(l == 2):
        return 'RB1out'
    elif(l == 3):
        return 'RB2in'
    elif( l == 4):
        return 'RB2out'
    elif(l == 5):
        if(k == 1):
            return 'RB3plus'
        elif(k == 2):
            return 'RB3minus'
    elif( l == 6):
        if(m == 1 or m == 2 or m == 3 or m == 5 or m == 6 or m == 7 or m == 8 or m == 10 or m == 12):
            if(k == 2):
                return 'RB4plus'
            elif(k == 3):
                return 'RB4minus'
        elif( m == 9 or m == 11):        
            if( k == 1):
                return 'RB4'
        elif( m == 4):
            if(k == 2):
                return 'RB4plus'
            elif(k == 3):
                return 'RB4minus'
            elif(k == 4):
                return 'RB4plusplus'
            elif(k == 5):
                return 'RB4minusminus'                  
    return '-1'            

def get_wheel(i):
    if( i == -2):
        return 'M2'
    elif(i == -1):
        return 'M1'
    elif(i == 0):
        return '00'
    elif( i == 1):
        return 'P1'
    elif( i == 2):
        return 'P2'
    return 'M3'      

def filter(day,hour,minute):
    if(day == 7): 
        if( hour == 7):
            if(minute >= 19 and minute <= 24):
                return 1
            elif(minute >= 41 and minute <= 50):
                return 1
        elif( hour == 10):
            if(minute >= 26 and minute <= 28):
                return 1
        elif( hour == 11):
            if(minute >= 1 and minute <= 9):
                return 1
        elif( hour == 19):
            if (minute >= 6 and minute <= 11):
                return 1
    elif (day == 8):
        if( hour == 7):
            if(minute >= 11 and minute <= 13):
                return 1
        elif( hour == 11 ):
            if(minute >= 36 and minute <= 40):
                return 1
    elif(day == 9):
        if( hour == 15):
            if(minute >= 3 and minute <= 6):
                return 1
        elif( hour == 16):
            if(minute >= 24 and minute <= 25):
                return 1
    elif(day == 10):
        if( hour == 1):
            if(minute >= 3 and minute <= 8):
                return 1
            elif(minute >= 12 and minute <= 14):
                return 1
        elif(hour == 13):
            if(minute >= 0 and minute <= 6):
                return 1
    elif(day == 11):
        if( hour == 13):
            if(minute >= 0 and minute <= 3):
                return 1
        elif( hour == 15):
            if(minute >= 1 and minute <= 5):
                return 1
        elif( hour == 14):
            if(minute >= 42 and minute <= 46):
                return 1
            elif(minute >= 52 and minute <= 54):
                return 1
    return 0

def filter_barrel(day,hour,minute):
    if(day == 7): 
        if( hour == 7):
            if(minute >= 19 and minute <= 24):
                return 1
            elif(minute >= 41 and minute <= 50):
                return 1
            elif(minute >= 13 and minute <= 13):
                return 1
        elif( hour == 10):
            if(minute >= 26 and minute <= 28):
                return 1
        elif( hour == 11):
            if(minute >= 1 and minute <= 9):
                return 1
        elif( hour == 19):
            if (minute >= 6 and minute <= 12):
                return 1
    elif (day == 8):
        if( hour == 7):
            if(minute >= 11 and minute <= 13):
                return 1
        elif( hour == 11 ):
            if(minute >= 36 and minute <= 47):
                return 1
    elif(day == 9):
        if( hour == 15):
            if(minute >= 3 and minute <= 6):
                return 1
        elif( hour == 16):
            if(minute >= 24 and minute <= 25):
                return 1
    elif(day == 10):
        if( hour == 1):
            if(minute >= 3 and minute <= 8):
                return 1
            elif(minute >= 12 and minute <= 14):
                return 1
        elif(hour == 13):
            if(minute >= 0 and minute <= 6):
                return 1
    elif(day == 11):
        if( hour == 13):
            if(minute >= 0 and minute <= 3):
                return 1
        elif( hour == 15):
            if(minute >= 1 and minute <= 5):
                return 1
        elif( hour == 14):
            if(minute >= 42 and minute <= 46):
                return 1
            elif(minute >= 52 and minute <= 54):
                return 1
    return 0



def update_progress(progress):
    barLength = 20 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "="*block + " "*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
