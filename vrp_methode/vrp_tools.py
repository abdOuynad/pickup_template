import pandas as pd
import numpy as np
import itertools
#
distance_matrix =[[0,1,2,10,32,31],[2,0,5,20,6,14],[5,6,0,15,8,4],
                  [10,20,15,0,6,8],[12,4,7,8,0,9],[70,55,46,9,71,0]]
clients=['c1','c2','c3','c4','c5','d']
vehicule=['v1','v2','v3','v4']
#
def vrp_init(client,distance_matrix,vehicule):
    com=[]
    sol={}
    result=[]
    data= pd.DataFrame(data=distance_matrix,columns=client,index=client)
    print(data)
    dipo=dict(data['d'])
    dipo=sorted(dipo.items(),key=lambda item: item[1])
    print('dipo \n',dipo)
    dipo.pop(0)
    sol[vehicule[0]]= dipo[0]
    result.append(sol)
    print(list(result[-1].values())[0][0])
    for v in vehicule:
        sol={}
        if v not in [list(x.keys())[0] for x in result]:
            chemin=[list(x.values())[0][0] for x in result]
            chemin.append('d')
            rest=[x for x in client if x not in chemin]
            chemin.remove('d')
            #
            dis={}
            for r in rest:
                s=0
                for n in chemin:
                    a=data.loc[r][n]
                    b=data.loc[n][r]
                    if a>b:
                        s+=a
                    else:
                        s+=b
                dis[r]=s
            dis=sorted(dis.items(),key=lambda item:item[1])
            print('dis ===>', dis)
            max=dis[-1]
            #
            sol[v]=max
            #
            result.append(sol)
            print("chemain==>", chemin)
            print('rest ==>', rest)
            print('"""""""""""""')


    print('resultat ===>',result)
#
if __name__ == '__main__':
    vrp_init(clients,distance_matrix,vehicule)
