from geopy.distance import geodesic
import pandas as pd
import numpy as np
import time
#
class vrp_by_geopy:
    #
    def __init__(self,clients,cars,coordonne,init):
        self.clients=clients
        self.cars=cars
        self.coordonne=coordonne
        self.init=init
    #
    def create_distance_matrix(self):
        matrix=[]
        for cor in self.coordonne:
            distance=list(map(lambda x:float(str(geodesic(cor,x)).strip('km')),self.coordonne))
            matrix.append(distance)
        #
        return matrix
    #
    def vector_init_distance(self):
        init_dis=list(zip(list(map(lambda x:float(str(geodesic(self.init,x)).strip('km')),self.coordonne)),self.clients))
        return init_dis
    #
    def matrix_to_df(self,matrix):
        df=pd.DataFrame(data=matrix,columns=self.clients,index=self.clients)
        #
        return df
    #
    def affec(self,dict_client_distnace, init_client):
        result = []
        dict_position_trie_by_client = {}
        for k, v in dict_client_distnace.items():
            list_position_trie = sorted(v)
            dict_position_trie_by_client[k] = [x for x in list_position_trie if x[1] in list_client]
        #
        #
        for i in self.clients:
            result.append(init_client)
            index = 1
            for x in self.clients[:-2]:
                if dict_position_trie_by_client[init_client][index][1] in result:
                    index += 1
                else:
                    init_client = dict_position_trie_by_client[init_client][index][1]
                    break
        return result
    #
    #
    def ajout(self,client, k, data):
        result = self.clients[:k]
        new_list_client = self.clients[k:]
        new_list_client.append(client)
        #
        d = {}
        #
        for c in new_list_client:
            # print(data[c].index)
            d[c] = list(zip(list(data[c]), list(data[c].index)))
        d[client] = list(zip(list(data[client]), list(data[client].index)))
        #
        trie = affec(d, new_list_client[0], new_list_client)
        return (result + trie)
    #
    def vrp_init(self,dipo_ds, matrix):
        sol = {}
        result = []
        rslt = []
        dipo = [x for x in dipo_ds if x[1] in self.clients]
        dipo = sorted(dipo)
        # print('dipo \n',dipo)
        #
        sol[self.cars[0]] = dipo[0]
        result.append(sol)
        rslt.append({self.cars[0]: dipo[0][1]})
        # print("result ==>",result)
        for v in self.cars[1:]:
            # print('v ===>',v)
            sol = {}
            chemin = [list(x.values())[0][1] for x in result]
            # print('chemin ==>',chemin)
            rest = [x for x in self.clients if x not in chemin]
            #
            dis = {}
            for r in rest:
                s = 0
                for n in chemin:
                    a = matrix.loc[r][n]
                    b = matrix.loc[n][r]
                    if a > b:
                        s += a
                    else:
                        s += b
                dis[s] = r
            dis = sorted(dis.items(), key=lambda item: item[1])
            # print('dis ===>', dis)
            max = dis[-1]
            #
            # print('max===>',max[1])
            sol[v] = max
            #
            result.append(sol)
            rslt.append({v: max[1]})

        # return result
        return rslt
    #
    def annulation(self,client, k, data):
        result = self.clients[:k]
        list_client = self.clients[k:]
        list_client.remove(client)
        #
        d = {}
        #p = []
        print(list_client)
        for c in list_client:
            # print(data[c].index)
            d[c] = list(zip(list(data[c]), list(data[c].index)))
        #
        trie = affec(d, list_client[0], list_client)
        return result + trie
    #
    def convert(self,data):
        d = {}
        for c in self.clients:
            d[c] = list(zip(list(data[c]), list(data[c].index)))
        return d

    def compare(self,init_vrp,):
        basket = []
        rslt = []
        for index in range(len(all_tourne[0])):
            # print(index)
            for line in list(zip(all_tourne, self.cars)):
                # print(line[0][index])
                if line[0][index] not in basket:
                    rslt.append((line[1], line[0][index]))
                    basket.append(line[0][index])
        return rslt
    #
    def affect(slef,init, list_client_rest, dict_client):
        new_dict = [x for x in dict_client[init] if x[1] in list_client_rest]
        return new_dict

    #
    def min_dis(self,list_dis_client):
        list_dis_client = sorted(list_dis_client)
        return list_dis_client[0][1]

    #
    def list_client_rest(self,init_dict):
        full = []
        # main
        for x in init_dict:
            init = list(x.values())[0][-1]
            #
            if init not in full:
                full.append(init)
            #
        return [x for x in self.clients if x not in full]

    #
    def affectation_client (self,init_vrp):
        #
        init_vrp_copy=init_vrp
        rest=self.list_client_rest(init_vrp_copy)
        #
        while (len(rest) != 0):

            for x in init_vrp_copy:
                init = list(x.values())[0][-1]
                aff = self.affect(init, rest, dict_client)
                nrml = self.min_dis(aff)
                v = list(x.keys())[0]
                x[v].append(nrml)
                rest.remove(nrml)
                if len(rest) == 0:
                    break
        #print("result ==>", init_vrp_copy)
        return init_vrp_copy
    #
    def possible(self,df,init_tourn):
        all_affec = []  # this list for recive all affect posible
        df_to_dict = self.convert(df)
        for x, c in enumerate(init_tourn):
            init = list(init_tourn[x].values())[0]
            all_affec.append(self.affec(df_to_dict, init))
        return all_affec
    #
    def affected(self, optmz_list):
        aff = []
        for v in self.cars:
            d = {}
            d[v] = [y for x, y in optmz_list if x == v]
            aff.append(d)
        return (aff)
    #
    def __repr__(self):
        return f"{self.clients}{self.cars}"
    #

if __name__ == '__main__':
    start=time.time()
    list_client=['c1','c4','c5','c2','c8','c9','cr']
    depo=(12,15)
    vendeur=['v1','v2','v3','v4']
    crdn=[(70,40),(55,15),(46,12),(9,13),(71,87),(12,39),(75,52)]
    tour=vrp_by_geopy(list_client,vendeur,crdn,depo)
    print('######### create class vrp #########')
    print(tour)
    distance_matrix=tour.create_distance_matrix()
    print('##### convert the matrix to df ######')
    df_matrix=tour.matrix_to_df(distance_matrix)
    print('dataframe matrix ===> \n',df_matrix)
    print('## the vecture of the init piont #####')
    init_vec=tour.vector_init_distance()
    print('init vecture ===> \n',init_vec)
    print('##### initialistion the clients ######')
    dist_init=tour.vrp_init(init_vec,df_matrix)
    print('the dict of client with car ===>: \n',dist_init )
    print('#### Show all affectation ############')
    all=tour.possible(df_matrix,dist_init)
    print('all possible affect ===> \n',all)
    print('#### optimaze the all affectation #####')
    opt=tour.compare(all)
    print('the list optimiz \n',opt)
    print('##### affecte the optimaze sol and return the final result ########')
    vrp=tour.affected(opt)
    print('the final list of vrp its \n',vrp)
    print('######### Time execution ###########')
    fin=time.time()
    print(fin-start)
