matrice=[]
n=int(input('introdu numarul de linii (2<=n<=10):'))
if((n>=2)and(n<=10)):
    print("introdu elementele matricei:")
    for line in range(0,n):
        linie=[]
        for element in range(0,n):
            element=int(input())
            linie.append(element)
        matrice.append(linie)
    print(matrice)
    d_principala=[]
    d_secundara=[]
    msus_principala=[]
    mjos_principala=[]
    msus_secundara=[]
    mjos_secundara=[]
    for a in range(len(matrice)):
        for b in range(len(matrice[0])):
            if a==b:
                d_principala.append(matrice[a][b])
            if (a+b)==(len(matrice)-1):
                d_secundara.append(matrice[a][b])
            if a<b:
                msus_principala.append(matrice[a][b])
            if a>b:
                mjos_principala.append(matrice[a][b])
            if(a+b)<(len(matrice)-1):
                msus_secundara.append(matrice[a][b])
            if(a+b)>(len(matrice)-1):
                mjos_secundara.append(matrice[a][b])
    print('Suma elementelor diagonale principale=',sum(d_principala))
    print('Suma elementelor diagonale secundare=',sum(d_secundara))
    print('Suma elementelor mai sus de diagonala principala=',sum(msus_principala))
    print('Suma elementelor mai jos de diagonala principala=',sum(mjos_principala))
    print('Suma elementelor mai sus de diagonala secundara=',sum(msus_secundara))
    print('Suma elementelor mai jos de diagonala secundara=',sum(mjos_secundara))






