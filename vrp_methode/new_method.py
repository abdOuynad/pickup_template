def affectation(init,dict_client_distnace,exist):
    new_dict={}
    #
    new_dict[init]=[x for x in dict_client_distnace[init] if x[1] in exist and x[1]!=init ]
    new_dict[init]=sorted(new_dict[init])
    val=new_dict[init][0][1]
    #
    #print(" new dict ===>",new_dict)
    #
    return val

#
#
def affect(init,list_client_rest,dict_client):
    new_dict=[x for x in dict_client[init] if x[1] in list_client_rest ]
    return new_dict
#
def minimal(dict,list_client_rest):
    l=[x for x in dict if x[1] in list_client_rest]
    return l
#
def min_dis(list_dis_client):
    list_dis_client=sorted(list_dis_client)
    return list_dis_client[0][1]
#
def list_client_rest(init_dict,list_client):
    full = []
    # main
    for x in init_dict:
        print('list_client_rest x ====>', x)
        init = list(x.values())[0][-1]
        #
        if init not in full:
            full.append(init)
        #
    return [x for x in list_client if x not in full]

#
if __name__ == '__main__':
    list_client=['c1', 'c4', 'c5', 'c2', 'c8']
    init_vrp=[{'v1': ['c2']}, {'v2': ['c8']}, {'v3': ['c5']}]
    dict_client={
     'c1': [(25, 'c0'), (0, 'c1'), (8, 'c2'), (6, 'c3'), (15, 'c4'), (20, 'c5'), (9, 'c6'), (10, 'c7'), (8, 'c8'),
            (12, 'c9'), (3, 'c10'), (2, 'c11'), (5, 'c12'), (6, 'c13')],
     'c4': [(8, 'c0'), (15, 'c1'), (6, 'c2'), (4, 'c3'), (0, 'c4'), (3, 'c5'), (5, 'c6'), (10, 'c7'), (6, 'c8'),
            (13, 'c9'), (20, 'c10'), (7, 'c11'), (6, 'c12'), (5, 'c13')],
     'c5': [(9, 'c0'), (3, 'c1'), (10, 'c2'), (3, 'c3'), (9, 'c4'), (0, 'c5'), (12, 'c6'), (12, 'c7'), (11, 'c8'),
            (21, 'c9'), (13, 'c10'), (8, 'c11'), (17, 'c12'), (18, 'c13')],
     'c2': [(10, 'c0'), (8, 'c1'), (0, 'c2'), (5, 'c3'), (6, 'c4'), (10, 'c5'), (8, 'c6'), (5, 'c7'), (3, 'c8'),
            (4, 'c9'), (17, 'c10'), (9, 'c11'), (10, 'c12'), (13, 'c13')],
     'c8': [(16, 'c0'), (10, 'c1'), (3, 'c2'), (9, 'c3'), (6, 'c4'), (10, 'c5'), (10, 'c6'), (9, 'c7'), (0, 'c8'),
            (9, 'c9'), (7, 'c10'), (8, 'c11'), (13, 'c12'), (8, 'c13')]}
    #
    #
    #affectation('c1',dict_client,list_client,full)
    rest = list_client_rest(init_vrp,list_client)
    #
    print('rest ==>', rest)
    while (len(rest) != 0):

        for x in init_vrp:
            init = list(x.values())[0][-1]
            aff = affect(init, rest, dict_client)
            print('dict client ==>',dict_client)
            nrml = min_dis(aff)
            v = list(x.keys())[0]
            x[v].append(nrml)
            rest.remove(nrml)
            if len(rest) == 0:
                break
    print("result ==>", init_vrp)