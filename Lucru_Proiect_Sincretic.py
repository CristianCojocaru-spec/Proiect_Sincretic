

# Proiect sincretic 

from dataclasses import dataclass
from msilib.schema import File

@dataclass
# structura unui nod din arbore
class node:
    def __init__(self, cheie):
        self.cheie: int = cheie
        self.stanga = None
        self.dreapta = None


#structura arborelui binar ordonat
class arbore:    
    # functie pentru inserare noduri in arbore
    
    def inserare_nod(self, radacina, cheie):
        if radacina == None:
            return node(cheie)
        else:
            if radacina.cheie < cheie:
                radacina.dreapta = self.inserare_nod(radacina.dreapta, cheie)
            else:
                if radacina.cheie > cheie:
                    radacina.stanga =self.inserare_nod(radacina.stanga, cheie)

        return radacina


    # functie pentru afisarea in inordine
    def __inordine__(self,radacina):
        if radacina:
            self.__inordine__(radacina.stanga)
            print(radacina.cheie,end=" ")
            self.__inordine__(radacina.dreapta)


    # functie pentru parcurgere in postordine
    def __postordine__(self,radacina):
        if radacina:
            self.__postordine__(radacina.stanga)
            self.__postordine__(radacina.dreapta)
            print(radacina.cheie, end=" ")

    
    # functie pentru parcurgere in preordine
    def __preordine__(self,radacina):
        if radacina:
            print(radacina.cheie, end=" ")
            self.__preordine__(radacina.stanga)
            self.__preordine__(radacina.dreapta)
     
    #functie pentru parcurgere arborelui pe nivel       
    def traversare_nivel(self,radacina):
        if radacina==None:
            return

         
        queue=[]
        queue.append(radacina)
        queue.append(None)
        i=1
        while len(queue)!=1:
            current=queue.pop(0)
            if current is not None:
                print(current.cheie,end=' ')
                if current.stanga is not None:
                    queue.append(current.stanga)
                if current.dreapta is not None:
                    queue.append(current.dreapta)
            else:
                # daca se ajunge aici inseamna ca s-a trecut la alt nivel
                print("\n")
                print("Nivel ",i,":",sep='',end=" ")
                i=i+1
                queue.append(None)  # semnalam inceputul nivelului urmator
                
        return     
                
            
def read_fromFile(file_name, nodes_buffer=[]):
    with open(file_name) as f:
        for i in f:
            nodes_buffer.append((int)(i.strip('\n')))
    
def MENIU():
    print("\n----------------------------------")
    print("1.Adaugare noduri din fisier")
    print("2.Afisare parcurgere in inordine")
    print("3.Afisare parcurgere in preordine") 
    print("4.Afisare parcurgere in postordine")
    print("5.Afisare parcurgere pe nivel")
    print("6.Iesire din program")

    print("\n----------------------------------")    
        


def main():

    
    while(1):
        MENIU()
        opt=int(input("Alegeti optiunea dorita:"))
        if opt==1:
            radacina=None
            nodes_buffer=[]
        
        
            read_fromFile("input_nodes.txt",nodes_buffer) 
            print("\n---Nodurile sunt:---")
            print(nodes_buffer)
            arbore1 = arbore()

            for i in nodes_buffer:
                radacina=arbore1.inserare_nod(radacina,i)
            
            
        elif opt==2:
            print("\nAfisare in inordine: ",end=" ")
            arbore1.__inordine__(radacina)
        elif opt==3:
            print("\nAfisare in preordine: ",end=" ")
            arbore1.__preordine__(radacina)

        elif opt==4:
            print("\nAfisare in postordine: ",end=" ")
            arbore1.__postordine__(radacina)

        elif opt==5:
            print("\n---Afisare pe nivel:--- ")
            print()
            print("Nivel 0:",end=" ")
            arbore1.traversare_nivel(radacina)

        elif opt==6:
            return
            
    
# Code execution starts here
if __name__ == '__main__':
    main()
