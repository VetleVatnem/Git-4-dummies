
#testet OK
def make_board():
        
    try:
        with open('sjakkbrett.txt' , 'r') as sjakkbrett:
            gammelt_nytt = sjakkbrett.readlines() 
            gammelt_nytt = [gammelt_nytt[i].replace('.' , ' ').split(',') for i in range(len(gammelt_nytt))]
        
        rader_ny = [[gammelt_nytt[j][1][i] for i in range(8)] for j in range(8)]
        rader_start = [[gammelt_nytt[j][0][i] for i in range(8)] for j in range(8)]
        return rader_start , rader_ny
    
    except FileNotFoundError:
        print('Error: File not found')
        return 1,1
    except PermissionError:
        print('Error: Permission denied')
        return 1,1
    except Exception as e:
        print(f'Error reading file: {e}')
        return 1,1

#Denne må fikses.
def lagre_brett(rader_gammel , rader_ny):
    streng_gammel = ''.join(rader_gammel[i][j] for i in range(8) for j in range(8))
    streng_ny = ''.join(rader_ny[i][j] for i in range(8) for j in range(8))
    
    with ('sjakkbrett.txt' , 'w') as sjakkbrett:
        sjakkbrett = streng_gammel + ',' + streng_ny

#testet OK
def omgjoring_til_indeks(a):
    b = [a[i] for i in range(len(a))]
    bokstav = ['a','b','c','d','e','f','g','h']
    tall_liste = [7-i for i in range(8)]

    x_faktisk = bokstav.index(b[0])
    y_faktisk = int(a[1])

    #omgjøring til indeks i en 2d liste
    x = x_faktisk 
    y = tall_liste[y_faktisk - 1]

    return (x , y)

#testet OK
def er_hvit(koordinat , brett):
    x,y = koordinat

    if brett[y][x].isupper():
        return True
    else:
        return False

#BONDE LOGIKK
#testet OK
def skjekk_om_bonde_kan_slå(koordinat , brett):
    x,y = koordinat
    kan_slå_koordinater = []

    if x < 7 and x > 0:
        for i in range(2):
            if er_hvit((x-1 + 2*i , y-1) , brett) == False and brett[y-1][x-1 + 2*i] != ' ' and get_piece((x-i + 2*i , y-1) , brett) != 'k':
                kan_slå_koordinater.append((x-1+2*i,y-1))
    elif x == 7:
        if er_hvit((x-1 , y-1) , brett) == False and brett[y-1][x-1] != ' ' and get_piece((x-1 , y-1) , brett) != 'k':
            kan_slå_koordinater.append((x-1,y-1))
    else:
        if er_hvit((x+1 , y-1) , brett) == False and brett[y-1][x+1] != ' ' and get_piece((x+1 , y-1) , brett) != 'k':
            kan_slå_koordinater.append((x+1,y-1))

    return kan_slå_koordinater

#testet OK
def bonde_kan_gå_frem(koordinat , brett):
    x,y = koordinat
    
    gyldig_trekk = []
    
    if y == 6 and brett[y-2][x] == ' ' and brett[y-1][x] == ' ':
        gyldig_trekk.append((x , y-2))
        gyldig_trekk.append((x , y-1))
    
    elif brett[y-1][x] == ' ':
        gyldig_trekk.append((x , y-1))
    
    else:
        gyldig_trekk = []
    return gyldig_trekk

#testet OK
def bonde_hvit(koordinat , brett):
    x,y = koordinat
    lovlige_trekk = []
    try:
        a = skjekk_om_bonde_kan_slå((x,y) , brett)
        b = bonde_kan_gå_frem((x,y) , brett)

        for i in range(len(a)):
            lovlige_trekk.append(a[i])
        for j in range(len(b)):
            lovlige_trekk.append(b[j])
        
        return lovlige_trekk

    except:
        print('Error executing bonde_hvit')

#TÅRN LOGIKK
def skann_brett(koordinat , brett , opp , høyre):
    x , y = koordinat
    
    if opp == True:
        for i in range()


    elif opp == False:

    elif høyre == True:
    
    else:

def tårn_hvit(koordinat , brett):
    x , y = koordinat

    gyldige_trekk = []

    #Skjekker gyldige trekk i y retning
    for i in range(7 - y):
        if brett[y - i][x] == ' ' or er_hvit((x , y-i) , brett):
            gyldige_trekk.append((x , y-i))

        if brett[y + i][x] == ' ' or er_hvit((x , y+i) , brett):
            gyldige_trekk.append((x , y+i))

    #Skjekker gyldige trekk i x retning
    for i in range(7 - x):

#MAIN FUNKSJONER OG HJELPEFUNKSJONER
#testet OK
def utskrift(brett):
    linjer = []
    for j in range(len(brett)):
        linjer.append(' '.join(brett[j][i] for i in range(len(brett[j]))))

    tall = [str(i+1)for i in range(8)]
    rader = [tall[7-i] for i in range(len(tall))]

    for i in range(len(linjer)):
        print(rader[i] + ' | ' + linjer[i] )       
    print('   ' + '-'*(16))
    print('    ' + 'A ' + 'B ' + 'C ' + 'D ' + 'E ' + 'F ' + 'G ' + 'H ')

def get_piece(koordinat , brett):
    
    x , y = koordinat
    brikke = brett[y][x]
    
    return brikke

#testet OK
def main():
    ny_eller_gammel = str.lower((input('For å fortsette med forrgie skriv: "Fortsett"\nFor å starte ny skriv:             "Ny"')))

    if ny_eller_gammel == 'fortsette':
        brett_orginal , brett = make_board()
        if brett_orginal == 1:
            loop = False
        else:
            loop = True

    elif ny_eller_gammel == 'ny':
        brett , lol = make_board()
        if brett == 1:
            loop = False
        else:
            loop = True

    while loop == True:
        utskrift(brett)
        brikke_streng = str(input('Hvilket brikke vil du flytte? Skriv lagre hvis du vil fortsette senere og ikke lagre hvis du vil starte på nytt'))
        flytte_streng = omgjoring_til_indeks(str(input('Hvor vil du flytte denne brikken?')))
        
        if brikke_streng.lower() == 'lagre':
            loop = False

        else:
            brikke_streng = omgjoring_til_indeks(brikke_streng)
            brikke = get_piece(brikke_streng , brett)
            hvit = er_hvit(brikke_streng , brett)
            
            if brikke == 'B' and hvit == True:
                gyldige_trekk = bonde_hvit(brikke_streng , brett)

                if flytte_streng in gyldige_trekk:
                    x,y = flytte_streng
                    x_1 , y_1 = brikke_streng
                    brett[y][x] = brikke 
                    brett[y_1][x_1] = ' '
                else:
                    print('Ugyldig trekk') 
            
        #lagre_brett(brett_orginal , brett)

main()