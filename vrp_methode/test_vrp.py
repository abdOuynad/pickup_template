import numpy as np
import pandas as pd
import random
import math
import sys
#
#
def Recuperer(nom_ficher):
    """
    :param nom_ficher:
    :param capacite:
    :param colisnbr:
    :param T:
    :param affec:
    :return:nbcren,nbrveh,distmax,nbclient,nbrdepot,capacite,colisnbr,affec,T
    """
    T=[]
    file=open(nom_ficher,'r')
    nbcren=int(file.readline())
    nbrveh=int(file.readline())
    distmax=int(file.readline())
    nbclient=int(file.readline())
    nbrdepot=int(file.readline())
    #
    capacite= [int(x) for x in file.readline().strip('\n').split(' ')[:nbrveh]]
    #
    colisnbr= [int(x) for x in file.readline().strip("\n").split(' ')[:nbclient]]
    #
    b=[]
    for x in range(nbclient+nbrveh):
        b.append(file.readline().strip('\n').split(' '))
    for x in b:
        x = [int(z) for z in x if z != '']
        T.append(x)
    #
    #
    affec = [int(x) for x in file.readline().strip("\n").split(' ')[:int(nbclient)]]
    file.close()
    return nbcren,nbrveh,distmax,nbclient,nbrdepot,capacite,colisnbr,affec,T
#
#
def duplication(v1,valeur):
    #
    return v1.count(valeur)
#
#
def minimum2(vl):
    return min(vl)
#
#
def ocroissant(v):
    """
    :param v: vecteur of the number
    :return: list of tuple croissant of the index and value
    """
    d={}
    for x,a in enumerate(v):
        d[x]=a
    return (sorted(d.items(),key=lambda item: item[1]))
#
#
def existence(v,value):
    if value in v:
        return v.index(value)
    return False
#
#
def remplace(new_client,client):
    for x in new_client:
        if x in client:
            return x
#
#
def ajout(client,tournees):
    for t in tournees:
        for x in t.values():
            if (len(x['client'])!= x['capacite']):
                client=sorted(client)
                index=[y for x,y in client]
                pos=remplace(index,x['client'])
                x['client'].insert(x['client'].index(pos)+1,len(client)+1)
                break

    return tournees
#
#
def trie(client,list_client,matrice):
    d={}
    for x in list_client:
        d[x]=list(matrice[x])
    print(d)
#
#
def annule(client,k,list_client,matrice):
    #list_client=list_client[k:]
    #cordonne=
    pass
#
#
def annulation(client,list_client,matrice):
    #
    new_matrice={}
    new_list=[]
    for x,c in enumerate(list_client):
        if c != client:
            new_list.append(c)
            new_matrice[c]=list(matrice[c])
        else:
            if x ==0 or x==len(list_client)-1:
                list_client.remove(c)
                print(list_client)
                return list_client
            else:
                initial=list_client[x-1]
                #list_client.remove(list_client[x])
    #
    for k,v in new_matrice.items():
        l=[]
        print(v)
        for c in new_list:
            l.append(v[c])
        new_matrice[k]=l
    #
    i=1
    for k,v in enumerate(new_matrice.items()):
        print(new_list.index(k))
    #
    print(list_client)
    print(new_list)
    print(initial)
    print(new_matrice)
    #

if __name__ == '__main__':
    #Recuperer('inst1.txt')
    v=[80, 20, 30, 70, 23, 32, 18, 30, 42, 15, 80, 45]
    m=[9,6,1,4,2,7,5,8,11,3,0,10]
    ds=[(31,1),(18,2),(20,3),(41,4),(23,5),(16,6),(11,7),(37,8),(36,9),(28,10)]
    c=[(9, 15), (6, 18), (1, 20), (4, 23), (2, 30), (7, 30), (5, 32), (8, 42), (11, 45), (3, 70), (0, 80), (10, 80)]
    c1=[(31,1),(11,2),(20,3),(41,4),(23,5),(16,6),(16,7),(37,8),(36,9),(28,10),(66,11)]
    tournees=[{1: {'client': [2,5,7,1], 'capacite': 6}}, {2: {'client': [6,9,3,4,8,10], 'capacite': 6}}]
    #print(minimum2(v))
    #print(ocroissant(v))
    #print(existence(v,70))
    #print(enplace((31,11),m,c))
    #print(v[a[1]])
    #a=ajout(ds,tournees)
    #print(a)
    #b=[{1: {'client': [2, 5, 11, 7, 1], 'capacite': 6}}, {2: {'client': [6, 9, 3, 4, 8, 10], 'capacite': 6}}]
    #print(annulation(11,a))
    #
    #step 1 read the information
    #
    #print(ajout(c1,a))

    creneau=1
    path="inst1.txt"
    nbcren, nbrveh, distmax, nbclient, nbrdepot, capacite, colisnbr, affec, T = Recuperer(path)
    #print(nbcren, nbrveh, distmax, nbclient, nbrdepot, capacite, colisnbr, affec,T)
    #
    #
    matrice=np.array(T)
    print(matrice)
    print()
    #annulation(7,[2,5,7,8,1],matrice)
    trie(7,[2,5,7,8,1],matrice)
