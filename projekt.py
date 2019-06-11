def przycisk_akapity():
    lista=[]
    for i in range(int(pole_akapity.get())+1):
        for j in range(0,random.randint(3,15)):
            cytat=random.choice(baza)
            baza.remove(cytat)
            lista.append(cytat+ " ")
        if i==1:
            None
        else:
            lista.append('\n\n')
