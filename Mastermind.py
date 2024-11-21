def lagbrett(a):
    brett = [['','','','']]*a
    return brett

def skrivut(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '':
                board[i][j] = '*'
    
    for i in range(len(board)):
        print(' '.join(board[i][a] for a in range(len(board[i]))))

import random as r
def nykombinasjon():
    farger = ['R' , 'G' , 'Y' , 'B' , 'P' , 'O']
    kombi = []

    for i in range(4):
        randomtall = r.randint(0, len(farger)-1)
        kombi.append(farger[randomtall])

    return kombi

def lesinn():
    guess = []
    forsøk = ['Første' , 'Andre' , 'Tredje' , 'Fjerde']
    farger = ['R' , 'G' , 'Y' , 'B' , 'P' , 'O']
    farger_norsk = ['rød' , 'grønn' , 'gul' , 'blu' , 'pink' , 'oransje']

    engelsk_norsk = {}

    for i in range(len(farger)):
        engelsk_norsk[farger[i]] = farger_norsk[i]

    i = 0
    print('Skriv in første bokstaven i det engelske ordet for fargen du tipper.')
    while i < 4:
        farge = str(input(f'{forsøk[i]} farge:'))

        if farge not in farger:
            print('Du må skrive inn en gyldig farge...')
        else:
            print(f'Du tippet {engelsk_norsk[farge]}')
            guess.append(farge)
            i += 1
    
    return guess

def nyttgjett(brett , gjett):
    
    if ['*','*','*','*'] in brett:
        forsøk = brett.index(['*','*','*','*'])
        brett[forsøk] = gjett
        return brett , True
    else:
        print('Du har brukt opp dine forsøk...')
        return [] , False
def evaluer(gjett , fasit):
    hvit = 0
    svart = 0
    rett_farge_plass = []
    for i in range(len(gjett)):
        if gjett[i] == fasit[i]:
            svart += 1
            rett_farge_plass.append(i)
    gjett = set(gjett)
    fasit = set(fasit)

    hvit_set = fasit & gjett
    hvit_liste = list(hvit_set)
    hvit = len(hvit_liste) - svart
    if hvit < 0:
        hvit = 0

    if svart == 4:
        print('Du har vunnet!!!!')
        return False
    else: 
        print(f'Du har {svart} antall på riktig plass og riktig farge')
        print(f'Du har {hvit} antall riktig farge men feil plass')
        return True

def main():
    loop = True
    forsøk = int(input('Hvor mange forsøk skal du ha?'))
    fasit = nykombinasjon()
    brettet = lagbrett(forsøk)
    skrivut(brettet)

    while loop == True:

        gjettet = lesinn()
        brettet , tap = nyttgjett( brettet , gjettet )
        
        if tap == False:
            break
        else:
            skrivut(brettet)
            loop = evaluer(gjettet , fasit)

main()