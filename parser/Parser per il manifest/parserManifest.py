# -*- coding: utf-8 -*-
#serie di funzioni che permettono di fare il parser di un file manifest


import xml.etree.cElementTree as ET
import csv
import sys
import os
import os.path


#funzione che dato un file xml restituisce il root
#il percorso va scritto  con una r prima (esempio r"c:\utenti") or con due backslash (""c:\\utenti") or con uno slash("c:/utenti")
def getRoot(percorso):
    tree = ET.parse(percorso)
    root = tree.getroot()
    return root;


#dato un root restituisce un array con tutti i permessi trovati
def getPermessi(root):
    permessi = [] #la lista con i permessi che verrà poi restituita
    # https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
    # con elementtree si ha un problema col namespace, xmlns:android e va messo per esteso
    for member in root.findall('uses-permission'):
        attribute = member.attrib
        permessi.append(attribute["{http://schemas.android.com/apk/res/android}name"])
    return permessi


# restituisce il complemento dell'intersezione tra due liste (controllare complessità del codice)
def diffList(li1, li2):
    l = list(set(li1) - set(li2))
    l = l + list(set(li2) - set(li1))
    return (l)

#restituisce tutti i duplicati in una lista
def cercaDuplicati(lista):
    elementi = []
    duplicati = []
    for x in lista:
        if x not in elementi:
            elementi.append(x)
        else:
            duplicati.append(x)
    return(duplicati)

#dato un percorso e un nome file scrive la lista passata su quel file (in modalità w)
def scriviListaSuFile(file, lista):
    file = open(file, "w")
    for item in lista:
        file.write("%s\n" % item)
    file.close()



# ------------------ Parte di codice usata solo per fare dei test di funzionamento ----------------------#
root = getRoot(r"C:\Users\Francesco\Desktop\AndroidManifest.xml")
permessi = getPermessi(root)
##print(*permessi, sep = "\n") # stamppa tutta la lista senza parentesi e dividendo ogni oggetto della lista con il valore sep
root2 = getRoot(r"C:\Users\Francesco\Desktop\AndroidManifest2.xml")
permessi2 = getPermessi(root2)
##print(*permessi2, sep = "\n")
differenzaPermessi = diffList(permessi2, permessi)
#print(diffList(permessi2, permessi))
duplicati2 =  cercaDuplicati(permessi2)
#print( cercaDuplicati(permessi2) )
scriviListaSuFile(r"C:\Users\Francesco\Desktop\prova.txt", duplicati2)
# -------------------------------------------------------------------------------------------------------#
