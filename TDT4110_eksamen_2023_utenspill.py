#-------------------------------------------------------------#
#-------------------------EKSAMEN 2023------------------------#
#-------------------------------------------------------------#

#OPPGAVE 1:
'''
Alternativ C (B) er riktig
'''

#OPPGAVE 2:
'''
Alternativ C (D) er riktig
'''

#OPPGAVE 3:
'''
Alternativ A og D (A,B,D) er riktig
'''

#Oppgave 4:
'''
Alternativ D (D) er riktig
'''

#Oppgave 5:
'''
Alle (B,C,D) alternativ er riktige
'''

#Oppgave 6:
'''
1 = ERROR   (ERROR)
2 = True    (False) 
3 = ERROR   (True)
4 = False   (False)
5 = '2'     ('2')
6 = True    (False) Mangler parantes rundt 9.0 for at denne skal bli true   
7 = ERROR   (2) Dette går visst an
8 = True    (True) 

poeng = 4
'''

#Oppgave 7:
'''
1 : ai is fun-  (alternativ 5) (ai is fun-)
2 : ai Fun-Is   (alternativ 6) (ai Fun-Is)
3 : aFN-I is U  (alternativ 7) (aFN-I is U)
4 : I S U-AIFN  (alternativ 1) (I S U-AIFN)
5 : I is fun-A  (alternativ 3) (I is fun-A)

poeng = 5
'''

#Oppgave 8
'''
Alternativ C er riktig (20/10)

poeng = 2/2
'''

#Oppgave 9
'''
[4,16] alternativ B (B)

poeng = 2
'''

#Oppgave 10
elements_sum = 0
max_elements = 10

for i in range(max_elements):
    if i % 2 == 0:    
        elements_sum += i+1

print(elements_sum) #Denne fungerer!

#Oppgave 11
def not_mutual(D):
    nøkkler = list(D.keys())
    tuppler = []
    for i in range(len(nøkkler)):
        A = nøkkler[i]
        for j in range(len(D[nøkkler[i]])):
            B = list(D[nøkkler[i]])[j]

            if B not in nøkkler or B in D[A] and A not in D[B]:
                tuppler.append((A,B))
    return tuppler

dic0 = {1:[2,3] , 2:[1,3] , 3:[1,4]}
print(not_mutual(dic0))
#Denne fungerer

#Oppgave 12
def midtkvadratet(n):
    tall = n**2
    streng_tall = str(tall)

    if tall < 1000:
        return tall
    
    elif len(streng_tall) % 2 == 0:
        midten = streng_tall[(len(streng_tall)//2)-2 : (len(streng_tall)//2)+2]
        return int(midten)
    
    else:
        midten = streng_tall[(len(streng_tall)//2)-1 : (len(streng_tall)//2)+3]
        return int(midten)
#Denne fungerer

#Oppgave 13
def mac(key , message , hash):
    return hash(hash(key*message)*key)

#Oppgave 14
def compress(tekst):
    lengde = len(tekst)
    compressed = ''
    for i in range(lengde):
        antall_like = 0
        for j in range(lengde - i):
            if tekst[i] == tekst[i+j] and tekst[i] not in compressed:
                antall_like += 1

        if antall_like == 1:
            compressed += tekst[i]

        elif antall_like != 0:
            compressed += str(antall_like) + tekst[i]

    return compressed
print(compress('AAAAccaBBBB'))
#Denne fungerer