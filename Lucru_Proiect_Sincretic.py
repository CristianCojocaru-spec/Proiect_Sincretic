

# inceput lucru la proiect


from dataclasses import dataclass
from math import radians


@dataclass

# structura unui nod din arbore
class node:
    def __init__(self,cheie):
        self.cheie:int=cheie
        self.stanga=None
        self.dreapta=None



# functie pentru inserare noduri in arbore
def __inserare_nod__(radacina,cheie):
    if radacina == None:
        return node(cheie)
    else: 
        if radacina.cheie<cheie:
            radacina.dreapta=__inserare_nod__(radacina.dreapta,cheie)
        else: 
            if radacina.cheie>cheie:
                radacina.stanga=__inserare_nod__(radacina.stanga,cheie)
    
    
     
    return radacina
 
 
            
# functie pentru afisarea in inordine           
def __inordine__(radacina):
    if radacina:
        __inordine__(radacina.stanga)
        print(radacina.cheie,end=" ")
        __inordine__(radacina.dreapta)  
        

# functie pentru parcurgere in postordine
def __postordine__(radacina):
    if radacina:
        __postordine__(radacina.stanga)
        __postordine__(radacina.dreapta)
        print(radacina.cheie, end=" ")
        
#functie pentru parcurgere in preordine

def __preordine__(radacina):
    if radacina:
        print(radacina.cheie, end=" ")
        __preordine__(radacina.stanga)
        __preordine__(radacina.dreapta)
        
   
def main():
    
    radacina=None
    
    # testare cu 7 noduri
    vector_noduri = [30,20,40,70,60,80,50]
    
    for i in range(0,len(vector_noduri)):
         radacina = __inserare_nod__(radacina,vector_noduri[i])
    
    print("\nAfisare in inordine: ") 
    
    
    __inordine__(radacina)
    
    print("\n\nAfisare in postordine: ")
    __postordine__(radacina)
    
    print("\n\nAfisare in preordine: ")
    __preordine__(radacina)
    
    print()
    
    
     
# Code execution starts here
if __name__=='__main__':
    main()

  
    

    
   



