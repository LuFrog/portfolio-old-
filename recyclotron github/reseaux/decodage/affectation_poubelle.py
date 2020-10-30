def affectation(type_dechet):
    if type_dechet=='cardboard':
        return 'carton : poubelle jaune'
    # elif type_dechet=='fabric':
    #     return 'bac vert'
    elif type_dechet=='glass':
        return 'verre : poubelle verte'
    elif type_dechet=='metal':
        return 'metal : poubelle jaune'
    elif type_dechet=='paper':
        return 'papier : poubelle jaune'
    elif type_dechet=='plastic':
        return 'platique : poubelle jaune'
    # elif type_dechet=="wood":
    #     return 'bac vert'
    elif type_dechet=='battery':
        return 'piles : poubelle piles'
    elif type_dechet=='organic':
        return 'organique : poubelle marron'
    else:
        return 'Error'