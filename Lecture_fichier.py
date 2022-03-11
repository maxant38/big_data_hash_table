import TD


def maxline():
    maxLine = 0
    #document in the same folder
    for doc in ['texte_Shakespeare.txt', 'corncob_lowercase.txt',
                'word2.txt']:  # pour compter le nombre de mot, on compte le nombre de ligne car il y a un mot par lignr
        f = open(doc, 'r')
        text = f.readlines()
        NumberOfLine = len(text)
        if maxLine < NumberOfLine:
            maxLine = NumberOfLine
    print(maxLine)


def hashage_fichier_ascii(fichier):
    lst_fichier_hashe=[]
    f = open(fichier,'r')
    mots = f.readlines()
    for i in range (0,len(mots)):
        mots[i] = mots[i][:-1]
        lst_fichier_hashe.append(TD.hashage_ascii(mots[i]))
    return lst_fichier_hashe

def hashage_fichier_Jenkins(fichier):
    lst_fichier_hashe=[]
    f = open(fichier,'r')
    mots = f.readlines()
    for i in range (0,len(mots)):
        mots[i] = mots[i][:-1]
        lst_fichier_hashe.append(TD.hash_justin_maxence_Jenkins(70769, mots[i]))
    return lst_fichier_hashe

def hashage_fichier_multiplication(fichier):
    lst_fichier_hashe=[]
    f = open(fichier,'r')
    mots = f.readlines()
    for i in range (0,len(mots)):
        mots[i] = mots[i][:-1]
        lst_fichier_hashe.append(TD.hash_justin_maxence_multiplication(70769, mots[i]))
    return lst_fichier_hashe

