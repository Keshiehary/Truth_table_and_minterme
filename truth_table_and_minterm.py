def function(f):
   return f
ligne=0
colonne=0
a,b,c=0,0,0
print("Respectivement posons b_bar  , c_bar les negations b et c")
b_bar=0
c_bar=0
ab=0
b_barc=0
ac_bar=0

#fixer la puissance de 2 maximale
puis=3

#tab juste pour l'affichage
rows = 2**puis
cols = 9

#initialisation de la matrice d'affichage
tab = [[0 for _ in range(cols)] for _ in range(rows)]


nbr_lg=rows
nbr_col=cols

#affection automatique des valeurs binaires
#de A B et C

dics = []
step = 0
tic=0
#stop=tic+(puis-1)

print ("---------------------------")
print("voici la table de vérité")
for step in range (rows):
   # nbr=bin(step) nombre de ligne
   #conversion en binaire de chaque nombre
   #tronqué le résutat à partir du 3e caractère
    nbr=format(step, '#05b')[2:]
    #print(nbr)
    sub=[]
    for tic in range (len(nbr)):
        #print(tic) nombre de colonnes
        #creation d'un sous-tableau avec les bits
        #pris dans la chaîne tronquée précédamment
        sub.append(nbr[tic])
    # print(sub)
    #dictionnaire des valeurs de chaque bits
    #pour chaque nombre binaire considéré
    dics = dics +[sub]

print ("---------------------------")
print ("   |a||b||c|!b|!c|ab|!bc|a!c|f|")
print ("---------------------------")
#  pparcours ligne par ligne puis colonne par colonne
for ligne in range (nbr_lg):
    for colonne in range((nbr_col)):
        
     
        #completion du tableau avec la valeur a ou b ou c
        #ex lgn=5 
        if colonne<puis:
            if colonne==0:
                a=int(dics[ligne][0])
                tab[ligne][colonne]=a
            else:
                if colonne==1:
                    b=int(dics[ligne][1])
                    tab[ligne][colonne]=b
                else:
                    c=int(dics[ligne][2])
                    tab[ligne][colonne]=c
                    
        #calcul des autres colonnes des b/ et c/
        if colonne<5:
            if b==0:
                b_bar =1
            else:
                b_bar=0
                
            if c==0:
              c_bar=1
            else:
              c_bar=0
        
        tab[ligne][3],tab[ligne][4]= b_bar,c_bar
        
  #b_bar=0 c_bar=0 ab=0 b_barc=0 ac_bar=0 f=0      
        ab,b_barc,ac_bar=a*b,b_bar*c,a*c_bar
        tab[ligne][5],tab[ligne][6],tab[ligne][7]=ab,b_barc,ac_bar
        
    #f
        
        f=ab+b_barc+ac_bar
        if f>0:
            f=1
            
            
        tab[ligne][8]=f
        
# afficher le tableau final !! présentation à revoir                                         
for ligne in range (nbr_lg):
    print ("["+str(ligne)+"]"+str(tab[ligne]))
            

mint=[[],[]]
minterme=""

   
for ligne in range (nbr_lg):
    
       
        a=tab[ligne][0]
        b=tab[ligne][1]
        c=tab[ligne][2]
        f=tab[ligne][8]
        if a==1:
            a="a"
        else:
            a="!a"
        if b==1:
            b="b"
        else:
            b="!b"
        if c==1:
            c="c"
        else:
            c="!c"
 
        
        minterme=a+" "+b+" " + c
        
        if f==1:
            
            mint[0].append(minterme)
        else:
            mint[1].append(minterme)
            
print ("---------------------------------------------------------------")
print("Les mintermes de la 1ere forme canonique:")
step=0
strv=""
for step in range (len(mint[0])):
    strv=strv+" + " + mint[0][step]

print("f=" + strv[2:])
strv=""
print("Les mintermes de la 2eme forme canonique:")

for step in range (len(mint[1])):
    strv=strv+" + "+mint[1][step]

print("f=" + strv[2:])
