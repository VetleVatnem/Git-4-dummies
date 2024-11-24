import numpy as np

def make_board(n):
    brett_liste = [['*' for i in range(n)]for j in range(n)]
    return np.array(brett_liste)

def start_UI():
    while True:
        try:
            spill = int(input('Hvilken type vil du spille?\n1 : Standard\n2 : egendefinert\n'))
            if spill == 1:
                return True
            elif spill == 2:
                return False
            else:
                print('Du må enten trykke alternativ "1" eller "2"')
        
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

    return x-1 , indeks_y[y]

def spiller_UI(dim):
    while True:
        koordinat = str(input('Hvor vil du plassere brikken?'))
        koordinat = koordinat.lower()

        if len(koordinat) == 2 and koordinat[0] in [str(i+1) for i in range(dim)] and koordinat[1] in [str(i+1) for i in range(dim)]:
            break

    x , y = omgjøring(koordinat , dim)
    return x , y

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

def scan_rad(rad , n):
    
    for i in range(len(rad)-n+1):
        x = 1
        for j in range(n-1):
            if rad[j+i] == rad[j+i+1] == 'O' or rad[j+i] == rad[j+i+1] == 'X':
                x += 1
                spiller = rad[i+j]
                if x == n:
                    return True , 'Running' if spiller == 'O' else 'Kryss'
    
    return False , '*'             

def scan_brett(brett , dim , n = 3):
    x = dim
    rader = brett
    kolonner = brett.transpose()
    
    #skjekker rader og kolonner:
    for i in range(x):

        vunnet_rad , spiller1 = scan_rad(rader[i] , n)
        vunnet_kol , spiller2 = scan_rad(kolonner[i] , n)
        
        if vunnet_rad == True:
            print(f'{spiller1} vant')
            return True
        elif vunnet_kol == True:
            print(f'{spiller2} vant')
            return True
        
    #skjekker diagonaler:
    diagonaler = [brett[::-1,:].diagonal(i) for i in range(-x+1,x)]
    diagonaler.extend(np.fliplr(brett)[::-1,:].diagonal(i) for i in range(-x+1 , x ))
    
    for i in range(len(diagonaler)):
        if len(diagonaler[i]) > n-1:
            
            vunnet , spiller = scan_rad(diagonaler[i] , n) 
            
            if vunnet == True:  
                print(f'{spiller} vant')
                return True
    
    return False

def egendefinert_UI():
    while True:
        try:
            dim = int(input('Hvilke dimensjoner skal brettet ha?'))
            på_rad = int(input('Hvor mange på rad skal det være?'))
        except:
            print('Du må skrive inn et heltall')
        
        if type(dim) == int and type(på_rad) == int and på_rad <= dim:
            break
        else:
            print('Antall på rad kan ikke være høyere enn dimensjonen på brettet.')

    return dim , på_rad

def main():
    a = start_UI()

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
        dim , n = egendefinert_UI()
        brett = make_board(dim)
        spiller = True
        vinner = False

        while True:
            skrivut(brett)

            if vinner == True:
                break

            brett = plasser_brikke(brett , spiller , dim)
            vinner = scan_brett(brett , dim , n)
            spiller = not spiller        
        
        brett = make_board(dim)

main()




