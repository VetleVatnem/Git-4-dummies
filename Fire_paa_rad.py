#Fire på rad fra eksamen 2023
import numpy as np

def lag_brett():
    brett = [['*' for i in range(7)]for j in range(6)]
    return brett

def skrivut(a):
    for i in range(len(a)):
        print(' '.join(a[i][j] for j in range(len(a[i]))))

def UI():
    
    while True:
        try:
            kolonne = int(input('Hvilken kolonne vil du plassere brikken i?'))
            if kolonne < 8 and kolonne > 0:
                return kolonne - 1
            else:
                print('Kolonnen må være å brettet')
        except ValueError:
            print('Du må skrive inn en kolonne på brettet')

def plaser_brikke(a , spiller):
    while True:
        kolonne = UI()
        
        if a[0][kolonne] != '*':
            print('Denne kolonnen er full')
        else:
            break
      
    if spiller == True:
        if a[5][kolonne] == '*':
            a[5][kolonne] = 'R'
            
        else:
            for i in range(len(a)):
                if a[i][kolonne] != '*':
                    a[i - 1][kolonne] = 'R'
                    break

    else:
        if a[5][kolonne] == '*':
            a[5][kolonne] = 'Y'
        else:
            for i in range(len(a)):
                if a[i][kolonne] != '*':
                    a[i - 1][kolonne] = 'Y'
                    break
    return a

def skjekk_rader(a):
    y , x = np.shape(a)

    for j in range(x - 3):    
        for i in range(len(a)):
            if a[i][j] == a[i][j+1] == a[i][j+2] == a[i][j+3] == 'R':
                print('Rød vant')
                return True
            if a[i][j] == a[i][j+1] == a[i][j+2] == a[i][j+3] == 'Y':
                print('Gul vant')
                return True
    return False
 
def skjekk_diagonal(a):
    
    for i in range(3):
        for j in range(4):
            if a[i][j] == a[i+1][j+1] == a[i+2][j+2] == a[i+3][j+3] == 'R' or a[i][6-i] == a[i+1][5-i] == a[i+2][4-i] == a[i+3][4-i] == 'R':
                print('Rød har vunnet')
                return True
            elif a[i][j] == a[i+1][j+1] == a[i+2][j+2] == a[i+3][j+3] == 'Y' or a[i][6-i] == a[i+1][5-i] == a[i+2][4-i] == a[i+3][4-i] == 'Y':
                print('Gul har vunnet')
                return True
    return False

def evaluer(a):
    ferdig = False
    brett = np.array(a)
    rader = kolonner = diag = fullt = False

    #skjekker rader:
    rader = skjekk_rader(brett)
    kolonner = skjekk_rader(brett.transpose())

    #skjekker diagonalene
    if 'R' in a[2] or 'Y' in a[2]:
        diag = skjekk_diagonal(a)
    
    #skjekker om brettet er fullt
    for i in range(len(a[0])):
        if '*' not in a[0]:
            fullt = True 
            
    if fullt == True:
        print('Brettet er fullt... dere er begge tapere...')
        
    if rader == True or kolonner == True or diag == True or fullt == True:
        ferdig = True
    
    return ferdig

def main():
    brett = lag_brett()
    skrivut(brett)
    spiller = True

    while True:
        #try:
            brett = plaser_brikke(brett , spiller)
            skrivut(brett)
            ferdig = evaluer(brett)
            spiller = not spiller
            if ferdig:
                break
        #except:
        #    print('heeeell naaah')
    
main()
