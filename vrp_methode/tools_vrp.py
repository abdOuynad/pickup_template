import numpy as np
import pandas as pd
import os
import math
import regex
#
#
def Recuperer(nom_ficher):
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
def trie(key,position,list_client):
    list_position=sorted(position)
    for x in list_position:
        if x[1] in list_client and x[0]!=0 and x[1] not in key:
            return x
#
#
def affec(dict_client_distnace,list_client):
    result = []
    init = list_client[0]
    dict_position_trie_by_client={}
    for k, v in dict_client_distnace.items():
        list_position_trie = sorted(v)
        dict_position_trie_by_client[k] = [x for x in list_position_trie if x[1] in list_client]
    #
    #print(dict_position_trie_by_client)
    #
    for i in list_client:
        result.append(init)
        index = 1
        for x in list_client[:-2]:
            if dict_position_trie_by_client[init][index][1] in result:
                index += 1
            else:
                init = dict_position_trie_by_client[init][index][1]
                break
    print(result)

#
#
def compare(liste_client,pos):
    new_list=[]
    new_list.append(liste_client[0])
    if liste_client[1] ==pos[0][1]:
        #print("list_client ==>",liste_client)
        return liste_client
    else:
        [new_list.append(x[1]) for x in pos]
        #print("new_list ==>",new_list)
        return new_list
#
#
def annulation(client,k,list_client,data):
    result=list_client[:k]
    list_client=list_client[k:]
    list_client.remove(client)
    #
    d={}
    p=[]
    print(list_client)
    for c in list_client:
        #print(data[c].index)
        d[c]=list(zip(list(data[c]),list(data[c].index)))
    #
    key=[]
    for k,v in d.items():
        x=trie(key,v,list_client)
        p.append(x)
        key.append(x[1])
    #
    p=[x for x in p if x[1]!=list_client[0]]
    #print(p)
    #
    neveau=compare(list_client,p)
    return result+neveau
#
#
def remplace(new_client,client):
    for x in new_client:
        if x in client:
            return x
#
#
def ajout(client,k,list_client,data):
    print(list_client)
    result=list_client[:k]
    list_client=list_client[k:]
    list_client.append(client)
    #
    d={}
    p=[]
    #
    for c in list_client:
        # print(data[c].index)
        d[c] = list(zip(list(data[c]), list(data[c].index)))
    d[client]=list(zip(list(data[client]), list(data[client].index)))
    #
    my_list={}
    for k, v in d.items():
        list_position = sorted(v)
        my_list[k] = [x for x in list_position if x[1] in list_client]
    print(my_list)
    result=[]
    init=list_client[0]
    for i in list_client:
        print("init ==>",init)
        result.append(init)
        index=1
        for x in list_client[:-2]:
            if my_list[init][index][1] in result:
                index+=1
            else:
                init=my_list[init][index][1]
                break
    print(result)
    #list_new=[x[1] for x in p]
    #print(result+p)
#
#
if __name__ == '__main__':
    path = "inst1.txt"
    nbcren, nbrveh, distmax, nbclient, nbrdepot, capacite, colisnbr, affec, T = Recuperer(path)
    #
    #
    name_client=["c"+str(x) for x in range(len(T[0]))]
    #
    #
    val={'c10': [(0, 'c10'), (6, 'c11'), (8, 'c3'), (11, 'c9'), (17, 'c2')],
          'c9': [(0, 'c9'), (3, 'c11'), (4, 'c2'), (11, 'c10'), (12, 'c3')],
         'c3': [(0, 'c3'), (4, 'c2'), (6, 'c10'), (8, 'c9'), (10, 'c11')],
         'c11': [(0, 'c11'), (5, 'c9'), (6, 'c3'), (8, 'c10'), (9, 'c2')],
         'c2': [(0, 'c2'), (4, 'c9'), (5, 'c3'), (9, 'c11'), (17, 'c10')]}
    list=['c10','c11','c3','c9','c2']
    #
    #
    print(" ======== Dataframe ========")
    df=pd.DataFrame(data=T,columns=name_client,index=name_client)
    print(df)
    print("============================")
    #print(annulation('c9',1,['c1','c4','c10','c9','c3','c11'],df))
    print("=============================")
    #ajout('c2',2,['c1','c4','c10','c9','c3','c11'],df)
    print("=============================")
    print(affec(val,list))