

# inceput lucru la proiect


from dataclasses import dataclass


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
        print(radacina.cheie)
        __inordine__(radacina.dreapta)  
        
    
        
   
def main():
    
    radacina=None
    
    # testare cu 7 noduri
    vector_noduri = [30,20,40,70,60,80,50]
    
    for i in range(0,len(vector_noduri)):
         radacina = __inserare_nod__(radacina,vector_noduri[i])
    
    print("Afisare in inordine:\n")
    
    
    __inordine__(radacina)
    
    
     
# Code execution starts here
if __name__=='__main__':
    main()

  
    

    
   



