# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13L4DGa_yph51QgsAIuybPlx5N8MiKtdm
"""

import numpy as np
import pandas as pd
import os
import math
import regex

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
    trie=affec(d,new_list_client[0],new_list_client)
    return(result+trie)

def vrp_init(list_client,dipo_ds,matrice,list_vondeur):
    sol={}
    result=[]
    rslt=[]
    dipo=[x for x in dipo_ds if x[1] in list_client]
    dipo=sorted(dipo)
    #print('dipo \n',dipo)
    #
    sol[list_vondeur[0]]= dipo[0]
    result.append(sol)
    rslt.append({list_vondeur[0]:dipo[0][1]})
    #print("result ==>",result)
    for v in list_vondeur[1:]:
      #print('v ===>',v)
      sol={}
      chemin=[list(x.values())[0][1] for x in result]
      #print('chemin ==>',chemin)
      rest=[x for x in list_client if x not in chemin]
            #
      dis={}
      for r in rest:
        s=0
        for n in chemin:
          a=matrice.loc[r][n]
          b=matrice.loc[n][r]
          if a>b:
            s+=a
          else:
            s+=b
        dis[s]=r
      dis=sorted(dis.items(),key=lambda item:item[1])
      #print('dis ===>', dis)
      max=dis[-1]
            #
      #print('max===>',max[1])
      sol[v]=max
            #
      result.append(sol)
      rslt.append({v:max[1]})

    #return result
    return rslt
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
    trie=affec(d,list_client[0],list_client)
    return result+trie

def convert (data,list_client):
  d={}
  for c in list_client:
    d[c]=list(zip(list(data[c]),list(data[c].index)))
  return d

def compare(all_tourne,list_vehicule):
  basket=[]
  rslt=[]
  for index in range(len(all_tourne[0])):
    #print(index)
    for line in list(zip(all_tourne,list_vehicul)):
      print('line ==>', line)
      print(line[0][index])
      if line[0][index]  not in basket:
        rslt.append((line[1],line[0][index]))
        basket.append(line[0][index])
  return rslt
#
def compare_1(all_tourne,list_vehicule):
    basket = []
    rslt = []
    for index in range(len(all_tourne[0])):
        # print(index)
        for i,line in enumerate(list(zip(all_tourne, list_vehicule))):
            # print(line[0][index])
            if line[0][index]  not in basket:
                rslt.append((line[1], line[0][index]))
                basket.append(line[0][index])
            else:
                for x in line[0][index+1:]:
                    if x not in basket:
                        rslt.append((line[1],x))
                        basket.append(x)
                        break
    return rslt

def affected(list_vehicul,optmz_list):
  aff=[]
  for v in list_vehicul:
    d={}
    d[v]=[y for x,y in optmz_list if x == v]
    aff.append(d)
  return(aff)

T=[[0, 25, 10, 7, 8, 9, 12, 4, 16, 12, 10, 11, 2, 8], [25, 0, 8, 6, 15, 3, 20, 9, 10, 8, 12, 3, 2, 5], [10, 8, 0, 4, 6, 10, 8, 5, 3, 4, 17, 9, 10, 13], [7, 6, 5, 0, 4, 3, 2, 7, 9, 12, 8, 6, 10, 17], [8, 15, 6, 3, 0, 9, 11, 10, 6, 13, 20, 7, 6, 5], [9, 20, 10, 2, 3, 0, 21, 19, 10, 12, 13, 14, 9, 8], [12, 9, 8, 7, 5, 12, 0, 10, 10, 12, 8, 22, 9, 10], [4, 10, 5, 9, 10, 12, 9, 0, 9, 12, 15, 11, 18, 19], [16, 8, 3, 12, 6, 11, 7, 9, 0, 6, 12, 9, 8, 5], [12, 12, 4, 8, 13, 21, 10, 8, 9, 0, 11, 5, 7, 8], [10, 3, 17, 6, 20, 13, 15, 6, 7, 11, 0, 8, 16, 15], [11, 2, 9, 10, 7, 8, 15, 12, 8, 3, 6, 0, 19, 16], [2, 5, 10, 12, 6, 17, 11, 7, 13, 7, 8, 9, 0, 14], [8, 6, 13, 7, 5, 18, 9, 12, 8, 12, 19, 17, 15, 0]]

name_client = ["c" + str(x) for x in range(len(T[0]))]
    #
    #  
print('============== Dataframe =============')
df = pd.DataFrame(data=T, columns=name_client, index=name_client)
print(df)
print('=======================================')
print(ajout('c2',2,['c1','c4','c10','c9','c3','c11'],df))
print('=======================================')
print(annulation('c9',2,['c1','c4','c10','c9','c3','c11'],df))
print("=======================================")
list_client =['c1','c4','c5','c2','c8','c9']
ds=[(70,'c1'),(55,'c4'),(46,'c5'),(9,'c2'),(71,'c8'),(12,'c9'),(14,'c10')]
vendeur=['v1','v2','v3','v4']
print(vrp_init(list_client,ds,df,vendeur))
print('=======================================')
print(convert(df,list_client))

if __name__=='__main__':
  print("============== Recupere ==============")
  #path = "inst1.txt"
  #nbcren, nbrveh, distmax, nbclient, nbrdepot, capacite, colisnbr, affec, T = Recuperer(path)
  print('=========== init creaneu =============')
  list_creneaux=[{'cr1':{'debut':'9:30','fin':'12:00','client':['c1','c4','c5','c2','c8'],'vehicule':['v1','v2','v3']},
                  'cr2':{'debut':'12:30','fin':'15:00','client':['c3','c7','c9'],'vehicule':['v1','v4','v2']},
                  'cr3':{'debut':'15:30','fin':'18:00','client':['c10','c12','c6','c11'],'vehicule':['v3','v1','v5']}
                  }]
  dipo_distance=[(70,'c1'),(55,'c4'),(46,'c5'),(9,'c2'),(71,'c8'),(12,'c9'),(14,'c10')]
  print('============== Dataframe =============')
  name_client = ["c" + str(x) for x in range(len(T[0]))]
  df = pd.DataFrame(data=T, columns=name_client, index=name_client)
  print(df)
  print('============== creneaux ==================')
  for index,creneau in enumerate(list_creneaux):
    #
    #recuperation de donne
    #
    debut=list(creneau.values())[0]['debut']
    fin=list(creneau.values())[0]['fin']
    list_client=list(creneau.values())[0]['client']
    print("list client ==>",list_client)
    list_vehicul=list(creneau.values())[0]['vehicule']
    #
    #========== initialisation ===========
    #
    init_tourn=vrp_init(list_client,dipo_distance,df,list_vehicul)#this variable for recive the point init for eache car 
    print(init_tourn)
    #
    all_affec=[]#this list for recive all affect posible 
    print('=========== vrp affectation ================================')
    print('=========== convert data to dictionair client distance =====')
    df_to_dict=convert(df,list_client)
    print("dataframe to vector ==> \n",df_to_dict)
    print('=========== star affectation ===============================')
    for x,c in enumerate(init_tourn):
      print('=============== determene initial point ==================')
      init=list(init_tourn[x].values())[0]
      print("init ==>",init)
      print('=============== propose voisgne chemin ===================')
      all_affec.append(affec(df_to_dict,init,list_client))
    print(all_affec)
    print("now we have compage and affect each point for each car")
    optm=compare_1(all_affec,list_vehicul)
    print("list optimize ==>",optm)
    print("we have list optimaze now we affect eache point of car")
    print(affected(list_vehicul,optm))
    #
    break

compare([['c2', 'c8', 'c4', 'c5', 'c1'], ['c8', 'c2', 'c4', 'c5', 'c1'], ['c5', 'c1', 'c2', 'c8', 'c4']],['v1','v2','v3'])

affected(['v1','v2','v3'],[('v1', 'c2'), ('v2', 'c8'), ('v3', 'c5'), ('v3', 'c1'), ('v1', 'c4')])

list_creneaux=[{'cr1':{'debut':'9:30','fin':'12:00','client':['c1','c4','c5','c2','c8'],'vehicule':['v1','v2','v3']}},
                {'cr2':{'debut':'12:30','fin':'15:00','client':['c3','c7','c9'],'vehicule':['v1','v4','v2']}},
                {'cr3':{'debut':'15:30','fin':'18:00','client':['c10','c12','c6','c11'],'vehicule':['v3','v1','v5']}
                  }]
for index,creneau in enumerate(list_creneaux):
  #
  #recuperation de donne
  #
  debut=list(creneau.values())[0]['debut']
  fin=list(creneau.values())[0]['fin']
  list_client=list(creneau.values())[0]['client']
  list_vehicul=list(creneau.values())[0]['vehicule']
  #
  
  break