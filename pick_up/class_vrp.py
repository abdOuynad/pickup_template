import pandas as pd
import numpy as np
from geopy.distance import geodesic
#
class vrp_by_geopy_class:
    #
    def __init__(self,clients,cars,coordonne,init):
        self.clients=clients
        self.cars=cars
        self.coordonne=coordonne
        self.init=init
    #
    def add_client(self,client):
        self.clients.append(client)
    #
    def add_coordonne(self,cord):
        self.coordonne.append(cord)
    #
    def add_client_dist(self,client,cord):
        self.add_client(client)
        self.add_coordonne(cord)
        #
        new_client_dis = list(
            zip(list(map(lambda x: float(str(geodesic(cord, x)).strip('km')),
                         self.coordonne)),
                         self.clients))

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
    def affec(self,dict_client_distnace,init,list_client):
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
    def affec_rcv(self,init, list_client, dict_client_distance, result=[]):
        if len(list_client) == 1:
            result.append(list_client[-1])
            return result
        else:
            list_dist = dict_client_distance[init]
            list_dist = sorted(list_dist)
            list_dist = [x for x in list_dist if x[1] in list_client]
            next = list_dist[0][1]
            list_client.remove(next)
            result.append(next)
            return affec_rcv(next, list_client, dict_client_distance, result)
    #
    #
    def ajout(self,clients,client, k, data):
        result = clients[:k]
        new_list_client = clients[k:]
        new_list_client.append(client)
        #
        d = {}
        #
        for c in new_list_client:
            # print(data[c].index)
            d[c] = list(zip(list(data[c]), list(data[c].index)))
        d[client] = list(zip(list(data[client]), list(data[client].index)))
        #
        trie = self.affec(d, new_list_client[0], new_list_client)
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
        rslt.append({self.cars[0]: [dipo[0][1]]})
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
            rslt.append({v: [max[1]]})

        # return result
        return rslt
    #
    def annulation(self,client, k,clients,data):
        result = clients[:k]
        list_client = clients[k:]
        list_client.remove(client)
        #
        d = {}
        #p = []
        #print(list_client)
        for c in list_client:
            # print(data[c].index)
            d[c] = list(zip(list(data[c]), list(data[c].index)))
        #
        trie = self.affec(d, list_client[0],list_client)
        return result + trie
    #
    def find_and_annulation(self,vrp_sol,client,data,k=0):
        for x in vrp_sol:
            if client in list(x.values())[0]:
                list_client=list(x.values())[0]
                new_list_affec=self.annulation(client,k,list_client,data)
                x[list(x.keys())[0]]=new_list_affec
                return vrp_sol
        return "the client :"+client+" not find"
    #
    def convert(self,data):
        d = {}
        for c in self.clients:
            d[c] = list(zip(list(data[c]), list(data[c].index)))
        return d
    #
    def compare(self,init_vrp,all_tourne):
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
    def affect(slef,init, list_clients_rest, dict_client):
        #print('affect ===>',dict_client,'list rest ===>',list_clients_rest)
        new_dict = [x for x in dict_client[init] if x[1] in list_clients_rest]
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
    def affectation_client (self,init_vrp,dict_client):
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
    def vrp_affec_rcv(self,cars, dict_dist, list_client, car_index=0, list_affec=[]):
        if len(list_client) == 1:
            # list(cars[car_index].values())[0].append(list_client[-1])
            return cars
        #
        if len(list_affec) == 0:
            for c in cars:
                list_affec.append(list(c.values())[0][0])
                # print(list(c.values())[0][0])
        #
        if len(list_client) != 1:
            init = list(cars[car_index].values())[0][-1]
            # print('init ==>',init)
            list_client = [x for x in list_client if x not in list_affec]
            # print('list client ==>',list_client)
            #
            list_dis = [x for x in dict_dist[init] if x[1] in list_client]
            list_dis = sorted(list_dis)
            next = list_dis[0][1]
            list_affec.append(next)
            list(cars[car_index].values())[0].append(next)
            #
            if car_index == len(cars) - 1:
                car_index = 0
            else:
                car_index += 1
            #
            # print('cars ==>',cars)
            # print('list_dis ==>',list_dis)
            # print('next ==>',next)
            #
            return self.vrp_affec_rcv(cars, dict_dist, list_client, car_index, list_affec)

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
    def all_distance(self,init_vec,x,data):
        s = [i[0] for i in init_vec if i[1] == list(x.values())[0][0]]
        # print(x)
        for y, z in enumerate(list(x.values())[0][1:-1]):
            # print(list(x.values())[0][y])
            a = list(x.values())[0][y]
            # print(list(x.values())[0][y+1])
            b = list(x.values())[0][y + 1]
            s += data.loc[a][b]
            # print('==================================')
        return s[0]

    #
    def max_distance(self,init_vec,x,data):
        list_dist=[]
        init = [i[0] for i in init_vec if i[1] == list(x.values())[0][0]]
        s =( init[0],
             'dipo',
             list(x.values())[0][0])
        # print(x)
        list_dist.append(s)
        for y, z in enumerate(list(x.values())[0][1:-1]):
            # print(list(x.values())[0][y])
            a = list(x.values())[0][y]
            # print(list(x.values())[0][y+1])
            b = list(x.values())[0][y + 1]
            s = (data.loc[a][b],a,b)
            list_dist.append(s)
            # print('==================================')
        return sorted(list_dist)[-1]
    #
    def vrp_sol_info(self,vrp_sol,vec_dis,data):
        info=[]
        for x in vrp_sol:
            d={}
            d['name']=list(x.keys())[0]
            d['size']=len(list(x.values())[0])
            d['full_Distance']=self.all_distance(vec_dis,x,data)
            d['max_Distance']=self.max_distance(vec_dis,x,data)
            #
            info.append(d)
        #
        return info
    #
    def __repr__(self):
        return f"{self.clients}{self.cars}"
    #
#
if __name__ == '__main__':
    #
    #creat data for test the model vrp_by_geopy
    #
    data=pd.read_excel('testdata.xls')
    list_client = list(data['Client '])
    crdn = list(zip(list(data['latitude']), list(data['longitude'])))
    #
    depo = (36.7149768, 3.2094611)
    cars=['v1','v2','v3','v4']
    #
    #creat new vrp_by_geopy_class
    #
    tour=vrp_by_geopy_class(list_client,cars,crdn,depo)
    #
    #creat matrix of the distance by geopy
    #
    matrix=tour.create_distance_matrix()
    #
    #convert the matrix to dataframe
    #
    df=tour.matrix_to_df(matrix)
    #
    #create dict client and all distance between other clients
    #
    dict_client_dict=tour.convert(df)
    #
    #create vector of the distance between depo and client
    #
    vec_dis_depo=tour.vector_init_distance()
    #
    #create dict of any car with init client
    #
    init_vrp=tour.vrp_init(vec_dis_depo,df)
    #
    #affectation the rest clients use the vrp methode
    #
    l=list_client
    vrp_dict_affec =tour.vrp_affec_rcv(init_vrp,dict_client_dict,l)
    #
    print(vrp_dict_affec)
    #
    print(tour.find_and_annulation(vrp_dict_affec,'sas',df,3))
    print(tour.vrp_sol_info(vrp_dict_affec,vec_dis_depo,df))