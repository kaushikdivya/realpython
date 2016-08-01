def makePoem():
    import random
    nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
    verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
    adj = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
    prep = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over","within"]
    adv = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

    n=[]
    v=[]
    aj=[]
    av=[]
    pep=[]

    while True:
        n1 = random.choice(nouns)
        if n1 not in n:
            if len(n) < 3:
                n.append(n1)
            else:
                break

    while True:
        v1 = random.choice(verbs)
        if v1 not in v:
            if len(v) < 3:
                v.append(v1)
            else:
                break

    while True:
        aj1 = random.choice(adj)
        if aj1 not in aj:
            if len(aj) < 3:
                aj.append(aj1)
            else:
                break

    while True:
        pep1 = random.choice(prep)
        if pep1 not in pep:
            if len(pep) < 2:
                pep.append(pep1)
            else:
                break

    while True:
        av1 = random.choice(adv)
        if av1 not in av:
            if len(av) < 1:
                av.append(av1)
            else:
                break
    if aj[0][0] in ["a", "e", "i", "o", "u"]:
        A_An = "An"
    else:
        A_An = "A"


                
    poem = """    {} {} {}\n
    {} {} {} {} {} the {} {}\n
    {}, the {} {}\n
    the {} {} {} a {} {}""".format(A_An,aj[0],n[0],A_An,aj[0],n[0],v[0],pep[0],aj[1],n[1],av[0],n[0],v[1],n[1],v[2],pep[1],aj[2],n[2])
    return poem
        
print makePoem()        
