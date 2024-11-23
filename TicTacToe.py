import numpy as np

def make_board(n):
    brett_liste = [['*' for i in range(n)]for j in range(n)]
    return np.array(brett_liste)

def start_UI():
    while True:
        try:
            spill = int(input('Hvilken type vil du spille?\n1 : Standard\n2 : egendefinert'))
            
            if spill == 1:
                return True , 3
            elif spill == 2:
                while True:
                    try:
                        på_rad = int(input('Hvor mange på rad skal det være?Max er 5'))
                        if på_rad <= 5:
                            return False , på_rad
                    except:
                        print('du må skrive et heltall...')
            else:
                print('Du må enten trykke "1" eller "2"')
        
        except:
            print('Du må skrive heltall')
       
def skrivut(brett):
    linjer = [' '.join(brett[i][j]for j in range(len(brett[i]))) for i in range(len(brett))]
    rad = list(range(len(brett),0,-1))
    kol = list(range(1 , len(brett)+1))
    for i in range(len(linjer)):
        print(str(rad[i]) + ' | ' + linjer[i])
    print('-'*(len(brett[0]) + 6))
    print(' '*4 + ' '.join(str(kol[i]) for i in range(len(kol))))

def omgjøring(koordinat , dim):
    x = int(koordinat[0])
    y = int(koordinat[1])

    indeks_y = list(range(dim ,-1,-1))

    return (x-1 , indeks_y[y])

def spiller_UI(dim):
    while True:
        koordinat = str(input('Hvor vil du plassere brikken?'))
        koordinat = koordinat.lower()

        if len(koordinat) == 2 and koordinat[0] in [str(i+1) for i in range(dim)] and koordinat[1] in [str(i+1) for i in range(dim)]:
            break
    indeks = omgjøring(koordinat , dim)
    return indeks

def plasser_brikke(brett , spiller , dim):
    while True:
        x , y = spiller_UI(dim)
        if brett[y][x] == '*':
            break
        else:
            print('Der er det allerede en brikke. prøv på nytt')

    if spiller == True:
        brett[y][x] = 'X'
    else:
        brett[y][x] = 'O'
    
    return brett

def scan_brett(brett , dim):
    x = dim
    rader = brett
    kolonner = brett.transpose()
    vinner = np.array([['O','O','O'],['X','X','X']])
    #skjekker rader og kolonner:
    for i in range(x):
        if np.array_equal(rader[i],vinner[0]) or np.array_equal(kolonner[i],vinner[0]):
            print('Running vant')
            return True
        elif np.array_equal(rader[i], vinner[1]) or np.array_equal(kolonner[i],vinner[1]):
            print('Kryss vant')
            return True
        
    #skjekker diagonaler:

def main():
    a , på_rad = start_UI()

    if a == True:
        dim = 3
        brett = make_board(dim)
        spiller = True
        vinner = False
        while True: 
            skrivut(brett)

            if vinner == True:
                break

            brett = plasser_brikke(brett , spiller , dim)
            vinner = scan_brett(brett , dim)
            spiller = not spiller
    else:
        while True:
            dim = int(input('Hvilke dimensjoner skal brettet ha?'))
            if type(dim) == int:
                break
        
        brett = make_board(dim)

main()
