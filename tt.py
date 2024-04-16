def NotVar(var):
    if var==1:
        notvar=0
    else:
        notvar=1
    return notvar


#def listAlphabet():
#    return [chr(i) for i in range(ord("a"), ord("z") + 1)]

def SaisieMinterme(step):
    mins=input("entrer le minterme "+ str(step+ 1)+ " : ")
    splt=mins.split()
    return mins,splt
    
    
tab,minus,var,var1,var2=[],[],[],[],[]

minst=input("combien de mintermes comporte la fonction: ")

print("le minterme ab sera saisie comme a b avec un espace  ")
print ("le minterme abarre b sera saisie comme : nota b ")
print ('--------------------------------------')

for step in range (int(minst)):
    
    mins,splt=SaisieMinterme(step)
    for elem in enumerate(mins.split()):
        var.append(elem[1])     
    
    minus.append(mins)
    

for elem in enumerate(var):
    if len(elem[1])>2:
        var1.append(elem[1][3])
        var2.append(elem[1])
    else:
        var1.append(elem[1])
        
            
var1,var2= sorted(list(set(var1))),sorted(list(set(var2)))


bits=0

for elem in enumerate (var1):
    if len(elem[1])==1:
       bits=bits+1

rows = 2**bits
cols = len(var)+1
 
tab = []+[[0 for _ in range(cols)] for _ in range(rows+1)]

tab[0]=var1+var2


lengths = max([len(s) for s in tab[0]])

param='#0'+str(bits+2)+'b'

nbr_lg=rows
nbr_col=cols

dics = []
step,tic,f=0,0,0

for step in range (nbr_lg):
    nbr=format(step,param )[2:]
    sub=[]
    for tic in range (len(nbr)):
        sub.append(nbr[tic])
    dics = dics +[sub]

var= {}
for ligne in range (nbr_lg):
    var.update({ligne:0})
    subs={}
    for step in range (bits):
        subs.update({var1[step]: int(dics[ligne][step])})
    var.update({ligne : subs}) 
    
    if len(var2)>0:
        for elem in enumerate (var2):
            io=int(var[ligne][elem[1][3]])
            subs.update({elem[1]: int(NotVar(io))})
            var.update({ligne : subs})
            
    fonc=0
        
    #minus
    
    
    for elem in enumerate(minus):
        min_str=""
        min_x=1
        for elt in enumerate (elem[1].split()):
           
           min_str=min_str+"*"+elt[1]
           min_x=min_x*int(var[ligne][elt[1]])
        subs.update({min_str[1:]: min_x})
        tab[0].append(min_str[1:])
        #print(min_str[1:]+":"+str( min_x))
        
        
        item=min_x
        fonc=fonc+item
        if fonc>1:
            fonc=1
            
    
    var.update({ligne : subs})        
    subs.update({'fonction': fonc})
       
    
tab[0]= sorted(list(set(tab[0])), key=lambda item: (len(item), item))
    
tab[0].append('fonction')
    
 
                
step=1
for elt in enumerate (var.values()):
    
    tab[step]=list(elt[1].values())
   
    step=step+1
 
print('-------------------------------')
print("la table de vérité")
print('-------------------------------')



tabs=tab
for steps in range(1,len(tabs)):
    
    tabs[steps]=str(tab[steps]).split("[")[1].split("]")[0].split(",")
    
    #print(tab[steps])        

format_row = "{:>12}" * (len(tab[0]) + 1)
#print(format_row.format("", *tab[0]))
step=0
for  row in  tabs:
    if step==0:
        print(format_row.format("", *row))
    else:
         print(format_row.format(step-1, *row))
    step=step+1

