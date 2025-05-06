
import networkx as nx
import matplotlib.pyplot as plt
import csv
import time

a=open("C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_article.csv.csv",'r', newline='', encoding='utf-8')

b=open('C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_book.csv','r', newline='', encoding='utf-8')

c=open('C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_incollection.csv','r', newline='', encoding='utf-8')

d=open('C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_inproceedings.csv','r', newline='', encoding='utf-8')

e=open('C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_mastersthesis.csv','r', newline='', encoding='utf-8')

f=open('C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_phdthesis.csv','r', newline='', encoding='utf-8')

g=open('C:\\Users\\User\\Desktop\\Algoritmi e Programmazione\\progetto 2022-23\\out-dblp_proceedings.csv','r', newline='', encoding='utf-8')


lista_indirizzi=[a,b,c,d,e,f,g]

lista_colonne_autori=[1,1,1,1,1,1,6]

lista_colonne_titoli=[29,22,22,24,10,22,28]


def prima_e_terza_domanda():
    
    start_time = time.time()
    
    for counter in range(7): #questo counter legge l'indice da 1 a 7 in ogni lista autori e titoli che indica la colonna di interesse
        
        G=nx.Graph() #creiamo un nuovo grafo per ogni file
        
        authors_dict = {}  #creiamo un dizionario degli autori 
        
        titles_dict = {}  #creiamo un dizionario dei titoli delle pubblicazioni
        
        
        with lista_indirizzi[counter] as csvfile: #apriamo ogni file csv
        
            csvreader = csv.reader(csvfile, delimiter=';') 
            
            next(csvreader)  #con questo comando iteratore saltiamo l'header
        
            for row in csvreader: #leggiamo ogni riga
            
                if len(row[counter]) != 0: #se la colonna degli autori NON è vuota
                
                    authors = row[lista_colonne_autori[counter]].split('|') #spacchettiamo la lista degli autori
                else:
                    authors = [] #se la lista autori è vuota creiamo una lista vuota
                 
                title = row[lista_colonne_titoli[counter]] #leggiamo il titolo della pubblicazione di ogni riga
                
                year=row[-1]
                
                id= row[0]
                
                titles_dict[id] = [title,year]  
                    
                G.add_node(id,type='Pubblication',color='White',bipartite=0)                 
                
                if len(authors)!=0:
                    
                    for author in authors: #per ogni autore nella lista autori creata precedentemente
                    
                        if author !='':
                            
                            if not G.has_node(author):   
                                G.add_node(author,type='Author',color='White', bipartite=1)
                                
                            authors_dict[author] = authors_dict.get(author, 0) + 1 # andiamo a incrementare nel dizionario degli autori, per ogni autore trovato (key), si incrementa il corriispettivo value di 1: si conta il numero di volte che troviamo un autore in una pubblicazione
                            
                            G.add_edge(author, id) #creiamo un arco dall'autore al titolo della pubblicazione, in questo modo facciamo crescere il grafo
                         
        

        max_author = max(authors_dict, key=authors_dict.get) #sfruttiamo il parametro opzionale key della funzione max, il quale prende attraverso il metodo .get() dei dizionari il value quindi il conteggio di ogni autore, e secondo questo criterio estraiamo il massimo
        
        print("L'autore con piu' pubblicazioni e':", max_author, "con", authors_dict[max_author], "pubblicazioni")
        
        # Calcola la somma delle pubblicazioni totali per ciascuna pubblicazione
        publication_total_counts = {}

        for publication in titles_dict:  #scorriamo la lista delle pubblicazioni nel corrispettivo dizionario
            
            total_count = 0 #questa è la variabile che ci interessa trovare: un counter della somma della popolarità degli autori
            
            for author in G.neighbors(publication): #scorriamo per ogni nodo-pubblicazione i suoi vicini che sono autori
            
                total_count += authors_dict.get(author, 0) #andiamo a sommare il numero delle pubblicazioni totali di ciascun autore salvate nel corrispettivo dizionario
            
            publication_total_counts[publication] = total_count #associamo ad ogni pubblicazione la variabile total_count
            
            
        # Trova la pubblicazione con la somma più grande delle pubblicazioni totali dei suoi autori
        
        most_popular_publication = max(publication_total_counts, key=publication_total_counts.get) # riutilizziamo il parametro opzionale della funzione max: key che estrae con il metodo dei dizionari .get() la pubblicazione con item somma (popolarità). Quindi prendo il massimo
        
        
        title_most_popular=titles_dict[most_popular_publication][0]
        
        print("La pubblicazione più popolare è:", title_most_popular, ' il cui ID è: ', most_popular_publication)
        
        print('**********************************************************')
    
    end_time = time.time()  # Registra il momento di fine
    
    elapsed_time = end_time - start_time  # Calcola il tempo totale trascorso
    
    print("Tempo totale di esecuzione:", elapsed_time, "secondi")

prima_e_terza_domanda() 