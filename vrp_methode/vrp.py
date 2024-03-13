import matplotlib as mtp
import numpy as np
import pandas as df
import random
#
cnv=[]
#
k=0
exist=0
pos=0
#
def Recuperer(nom_ficher,nbcren,nbrveh,distmax,
              nbclient,nbrdepot,
              capacite,colisnbr,T,affec):
    """

    :param nom_ficher:
    :param nbcren:
    :param nbrveh:
    :param distmax:
    :param nbclient:
    :param nbrdepot:
    :param capacite:
    :param colisnbr:
    :param T:
    :param affec:
    :return:
    """
    vect=[]
    x:int
    file=open(nom_ficher,'r')
    nbcren=file.readline()
    nbrveh=file.readline()
    distmax=file.readline()
    nbclient=file.readline()
    nbrdepot=file.readline()
    #
    for v in nbrveh.strip('\n').split(' '):
        capacite.append(v)
    #
    for c in nbclient.strip('\n').split(' '):
        colisnbr.append(c)
    #
    for x in zip(nbrveh.strip('\n').split(' '),nbclient.strip('\n').split(' ')):
        for x in zip(nbrveh.strip('\n').split(' '), nbclient.strip('\n').split(' ')):
            vect.append(x)
        T.append(vect)
        vect=[]
    #
    for c in nbclient.strip('\n').split(' '):
        affec.append(c)

    file.close()
#
def duplication(vl,valeur,dup):
    """

    :param vl:
    :param valeur:
    :param dup:
    :return:
    """
    dup=0
    k=0
    while(dup<3 and k<len(vl)):
        if(vl[k]==valeur):
            dup+=1
        k+=1
#
def minimum2(vl):
    """

    :param vl:
    :return:
    """
    min=vl[0]
    for v in vl:
        if v!=99999999999:
            if(min>v):
                min=v
    return min
#
def ocroissant2(vl,v2,v3,v4):
    rep=0
    k=0
    for v in vl:
        for a in vl:
            min=minimum2(vl)
        for a in vl:
            if (a == min and v !=9999):
                v4.append(v2[vl.index(v)])
                rep+=1
        while(k<rep):
            v3.append(min)
            k+=1
            for a in vl:
                if(a==min):
                    a=999
def existence(vl,valeur,exist=0,pos=0):
    """

    :param vl:
    :param valeur:
    :param exist:
    :param pos:
    :return:
    """
    k=0
    while(exist==0 and k<len(vl)):
        if(vl[k]==valeur):
            exist=1
            pos=k
        k+=1
#
def ajout(client,nbrcolis,nbrclient,tournees):
    global k
    global exist
    global pos
    distance=[]
    v2=[]
    v3=[]
    v4=[]
    for c in range(len(nbrclient)):
        distance.append(random.randint(1,20))
        v2.append(c+1)
        printr(distance)
    for c in distance:
        print(c)
    #
    exist=0
    kl=0
    #
    ocroissant2(distance,v2,v3,v4)
    vpp=v4[0]
    #
    print('vpp ==>',vpp)
    exist=0
    while(exist==0 and kl<len(tournees)):
        print('while')
        existence(tournees[kl],vpp,exist,pos)
        if(exist==0):
            kl+=1
        tournees[kl].insert(tournees[kl][0]+pos+1,client)
        print("apres l'ajoute")
        for j in tournees[kl]:
            print(j)
    #
    #
def annulation(client,tournees):
        """

        :param client:
        :return:
        """
    global cnv
    exist=0
    kl=0
    #
    while(exist==0):
        existence(tournees[kl],client,exist,pos)
        if exist ==0:
            kl+=1
            print('fin while annulation')
            taille=len(tournees[kl])-1
            print('taille :',taille)
            print('position :',pos)
        for i in range(len(tournees[kl]))[pos+1:]:
            cnv.append(tournees[kl][i])
        print('fin for annulation')
        print('cnv',cnv)
        for c in cnv:
            print(c)
        #
        for x in tournees[kl][pos:]:
            tournees.remove(x)
        print('touenees[kl]')
        for x in tournees[kl]:
            print('tournees',x)
        while(len(cnv)!=0):
            print('while cnv')
            b=tournees[kl][-1]
            print('b:',b)
            vl=[]
            v2=[]
            v3=[]
            v4=[]
            #
            for c in cnv:
                v2.append(c)
                v1.append(T[b-1][cnv.index(c)-1])
            ocroissant2(vl,v2,v3,v4)
            #
            tournees[kl].append(v4[0])
            existence(cnv,v4[0],exist,pos)
            cnv.remove(pos)
        print("l'ensemble des tournees apres la suppression")
        for x in tournees:
            print(' ')
            for c in tournees[kl]:
                print('tournees',x[c])
#
if __name__ == '__main__':
    nom_fichier='instl.txt'
    ll=[]
    #
    creneau=1
    a=0
    #
    #
    Recuperer(nom_fichier,nbcren,nbrveh,distmax,nbclient,nbrdepot,
              ,capacite,colisnbr,T,affec)
    print('ouil')
    print('nbrcreneau',nbcren)
    print("nbrcreneau",nbcren)
    print("nbvehicule",nbrveh)
    print("distmax",distmax)
    print("nbclient",nbclient)
    print("nbdepot",nbrdepot)
    print('capacite')
    #
    for c in capacite:
        print(c)
    print("matrice")
    for t in T:
        print(' ')
        for c in t:
            print('',c)
    print('affec')
    for f in affec:
        print(f)

    print('fin affec')
    #
    for j in nbrveh:
        colismar.append(0)
    #
    creneau=1
    for n,a in enumerate(affec):
        if a==creneau:
            cnv.append(n+1)
            print('cnv boucle')
            for c in cnv:
                print('c')
            if T[0][n]<= distmax:
                print('T[0][n] ==>',T[0][n])
                ll.append(n+1)
            #
        #
        print('------------------------')
        print('cnv')
        for c in cnv:
            print(c)
        print('ll')
        for l in ll:
            print(l)
        k=0
        exist=0
        pos=0
        #
        tournee[:len(nbrveh)]
        while(k<nbrveh):
            print('while')
            print('a',a)
            print('ll[a]',ll[a])
            existence(cnv,ll[a],exist,pos)
            print('exist',exist)
            print('pos')
            if exist == 1:
                print('if')
                print('taille',len(tournees))
                tournees[k].append(ll[a])
                for k in tournees[k]:
                    print(tournees)
                print('ajout')
                cnv.remove(cnv.index(cnv[pos]))
                print('suppression')
                print('cnv')
                for c in cnv:
                    print(c)
                k+=1
     #
    print('fin while')
    print("l'ensemble des tournees de creneau 1")
    for t in tournees:
        print(' ')
        for x in t:
            print('tournees[i1][j1]',x)
         #
    while(len(cnv)!=0):
        print('while1')
        k=0
        while(k<nbrveh and len(cnv)!=0):
            print('while2')
            k=0
            #
            b= tournees[k][-1]
            v1=[]
            v2=[]
            v3=[]
            v4=[]
            for i,x in enumerate(cnv):
                v1.append(T[b-1][x-1])
                v2.append(x)
            ocroissant2(v1,v2,v3,v4)
            tournees[k].append(v4[0])
            existence(cnv,v4[0],exist,pos)
            cnv.remove(cnv.index(cnv[pos]))
            k+=1
    #
    print("l'ensemble des tournees de creneau 1")
    for c in tournees:
        print("  ")
        for x in c:
            print("tournees[i1][j1]",c[x])
        #
    t=2
    while(t<= nbcren):
        for t,f in enumerate(affec):
            if f ==t:
                cnv.append(t+1)
        #
        print('cnv de creneau',t)
        for c in cnv:
            print(c)
        while len(cnv)!=0:
            k=0
            while(k<nbrveh and len(cnv)!=0):
                print('while2')
                b=tournees[k][-1]
                v1=[]
                v2=[]
                v3=[]
                v4=[]
                for c in cnv:
                    v1.append(T[b-1][c-1])
                    v2.append(c)
                ocroissant2(v1,v2,v3,v4)
                tournees[k].append(v4[0])
                existence(cnv,v4[0],exist,pos)
                cnv.remove(cnv[pos])
                k+=1
    cnv=[]
    t+=1
    #
    print("l'ensemble des tournees a la des creneaux")
    for t in tournees:
        print(" ")
        for x in t:
            print("tournees[i1][j1]",t)
    print('client a supprimer')
    c1=input('donne votre index')
    c1=int(c1)
    annulation(c1,tournnes)
    print('client ajout')
    c2=input("")
    ajout(c2,nbrcolis,nbrclient)





