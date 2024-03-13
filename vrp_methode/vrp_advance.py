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
def affec(dict_client_distnace,init,list_client):
    result = []
    dict_position_trie_by_client={}
    for k, v in dict_client_distnace.items():
        list_position_trie = sorted(v)
        dict_position_trie_by_client[k] = [x for x in list_position_trie if x[1] in list_client]
    #
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
    return result
#
#
def ajout(client,k,list_client,data):
    print(list_client)
    result=list_client[:k]
    new_list_client=list_client[k:]
    new_list_client.append(client)
    #
    d={}
    #
    for c in new_list_client:
        # print(data[c].index)
        d[c] = list(zip(list(data[c]), list(data[c].index)))
    d[client]=list(zip(list(data[client]), list(data[client].index)))
    #
    print("d==>",d)
    print("init ==>",new_list_client[0])
    print("new_list_client ==>",new_list_client)
    trie=affec(d,new_list_client[0],new_list_client)
    print(trie)
    #print(result+p)
#
#
if __name__ == '__main__':
    path = "inst1.txt"
    val = {'c10': [(0, 'c10'), (6, 'c11'), (8, 'c3'), (11, 'c9'), (17, 'c2')],
           'c9': [(0, 'c9'), (3, 'c11'), (4, 'c2'), (11, 'c10'), (12, 'c3')],
           'c3': [(0, 'c3'), (4, 'c2'), (6, 'c10'), (8, 'c9'), (10, 'c11')],
           'c11': [(0, 'c11'), (5, 'c9'), (6, 'c3'), (8, 'c10'), (9, 'c2')],
           'c2': [(0, 'c2'), (4, 'c9'), (5, 'c3'), (9, 'c11'), (17, 'c10')]}
    list = ['c10', 'c11', 'c3', 'c9', 'c2']
    #
    #
    nbcren, nbrveh, distmax, nbclient, nbrdepot, capacite, colisnbr, affec, T = Recuperer(path)
    #
    #
    name_client = ["c" + str(x) for x in range(len(T[0]))]
    #
    #
    print('============== Dataframe =============')
    df = pd.DataFrame(data=T, columns=name_client, index=name_client)
    print(df)
    print('=======================================')
    ajout('c2',2,['c1','c4','c10','c9','c3','c11'],df)