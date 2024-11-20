def make_board():
    filsti = r'C:\\Users\\vetle\\OneDrive\\Skolegang\\Universitet\\Elektronisk systemdesign & innovasjon\\1. Semester\\TDT 4110 Informasjonsteknologi grunnkurs\\Spill\\sjakkbrett'
    
    try:
        with open(filsti , 'r') as sjakkbrett:
            gammelt_nytt = sjakkbrett.readlines() 
            gammelt_nytt = [gammelt_nytt[i].replace('.' , ' ').split(',') for i in range(len(gammelt_nytt))]

        rader_ny = [[gammelt_nytt[i][1]]for i in range(8)]
        rader_start = [[gammelt_nytt[i][0]] for i in range(8)]
            
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

def lagre_brett(rader_gammel , rader_ny):
    streng_gammel = ''.join(rader_gammel[i][j] for i in range(8) for j in range(8))
    streng_ny = ''.join(rader_ny[i][j] for i in range(8) for j in range(8))
    
    with ('sjakkbrett.txt' , 'w') as sjakkbrett:
        sjakkbrett = streng_gammel + ',' + streng_ny

def omgjoring_til_indeks(a):
    a = a.split(',')
    a = [a[i].lowercase() for i in range(len(a))]
    bokstav = ['a','b','c','d','e','f','g','h']
    tall_liste = [7-i for i in range(8)]

    x_faktisk = bokstav.indeks(a[0] - 1) + 1
    y_faktisk = a[1]

    #omgjøring til indeks i en 2d liste
    x = x_faktisk 
    y = tall_liste[y_faktisk - 1]

    return (x , y)

def er_hvit(koordinat , brett):
    x,y = koordinat

    if brett[y][x].isupper():
        return True
    else:
        return False


#BONDE LOGIKK
def skjekk_om_bonde_kan_slå(koordinat , brett):
    x,y = koordinat

    kan_slå_koordinater = []

    if x < 6 or x < 1:
        for i in range(2):
            if er_hvit((x-1 + 2*i , y+1) , brett) == False:
                kan_slå_koordinater.append([x-1+2*i,y+1])
    elif x == 7:
        if er_hvit((x-1 , y+1) , brett) == False:
            kan_slå_koordinater.append([x-1,y+1])
    else:
        if er_hvit((x+1 , y+1) , brett) == False:
            kan_slå_koordinater.append([x+1,y+1])
    
    return kan_slå_koordinater

def bonde_kan_gå_frem(koordinat , brett):
    x,y = koordinat
    gyldig_trekk = []

    if y == 1 and brett[y+2][x] == ' ':
        gyldig_trekk.append([x , y+2])
    
    elif brett[y+1][x] == ' ':
        gyldig_trekk.append([x , y+1])
    
    else:
        gyldige_trekk = []
    
    return gyldig_trekk

def bonde_hvit(koordinat , brett):
    x,y = koordinat
    lovlige_trekk = []
    try:
        lovlige_trekk.append(skjekk_om_bonde_kan_slå((x,y) , brett))
        lovlige_trekk.append(bonde_kan_gå_frem((x,y) , brett))

        return lovlige_trekk

    except:
        print('Error executing bonde_hvit')
    
#MAIN FUNKSJONER OG HJELPEFUNKSJONER
def get_piece(koordinat , brett):
    
    x , y = koordinat
    brikke = brett[y][x]
    
    return brikke

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
            
    else:
        print('Neivel...ingenting da')

    while loop == True:
        brikke_streng = omgjoring_til_indeks(str(input('Hvilket brikke vil du flytte? Skriv lagre hvis du vil fortsette senere og ikke lagre hvis du vil starte på nytt')))
        flytte_streng = omgjoring_til_indeks(str(input('Hvor vil du flytte denne brikken?')))

        if brikke_streng.lower() == 'lagre':
            loop = False

        else:
            brikke = get_piece(brikke_streng , brett)
            hvit = er_hvit(brikke_streng , brett)

            if brikke == 'B' and hvit == True:
                gyldige_trekk = bonde_hvit(brikke_streng , brett)

                if flytte_streng in gyldige_trekk:
                    brett[flytte_streng[1]][flytte_streng[0]].replace(brikke)
                    brett[brikke_streng[1]][brikke_streng[0]].replace(' ')
                else:
                    print('Ugyldig trekk') 
        
        lagre_brett(brett_orginal , brett)

main()