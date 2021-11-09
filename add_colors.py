#!/usr/bin/env python

def get_liste_noms():
    """
        Lit la liste des personnes entre les
        ----
        ----
        dans l'en-tête
    """
    file = open("graph.dot", 'r+')
    liste_noms = []
    get_in = False
    for line in file.readlines():
        if get_in:
            liste_noms.append(line.rstrip("\n"))
        if "----" in line:
            if not get_in:
                get_in = True
            else:
                break
    liste_noms.pop()
    file.close()
    return liste_noms


def insert_line(string):
    """Insère string à l'avant-dernière ligne"""
    with open("graph.dot", "r") as f:
        contents = f.readlines()

    num_lines = sum(1 for _ in open('graph.dot'))
    contents.insert(num_lines - 1, string + "\n")

    with open("graph.dot", "w") as f:
        contents = "".join(contents)
        f.write(contents)


def delete_old_nodes():
    with open("graph.dot", "r") as graph:
        lines = graph.readlines()

    with open("graph.dot", "w") as graph:
        for line in lines:
            if not "fillcolor" in line:
                graph.write(line)


def check_if_node(string):
    """Vérifie si une coloration existe déjà pour la personne"""
    file = open("graph.dot", 'r+')
    for line in file.readlines():
        if string in line:
            if "color" in line:
                file.close()
                return True
    file.close()
    return False


def new_node(nom, color_list, exceptions):
    """Crée le node avec les bonnes couleurs"""
    line = '    "{}"'.format(nom)
    for exception, replacement in exceptions:
        nom.replace(exception, replacement)
    nom.replace("'", " ")
    for exception, replacement in exceptions:
        nom.replace(replacement, exception)
    nom = nom.split()
    line += '[fillcolor="{}"]'.format(couleur(nom[1:], color_list))
    return(line)


def lists_init():
    """
        C'est ici que vous devez rajouter le mot-clef à chercher
        dans les noms (pratique pour les noms abregés) 
        avec la couleur correspondante
    """
    color_list = []
    color_list.append(("puls", "#a300a3"))
    color_list.append(("storm", "#a300a3"))
    color_list.append(("valh", "#00BFFF"))
    color_list.append(("chap", "#00BFFF"))
    color_list.append(("valar", "#4b488c"))
    color_list.append(("bluff", "#4b488c"))
    color_list.append(("dice", "#ff4d5c"))
    color_list.append(("diab", "#ff4d5c"))
    color_list.append(("lord", "#ff4d5c"))
    color_list.append(("an'art", "#ff4d5c"))
    color_list.append(("abso", "#5d30ff"))
    color_list.append(("ghib", "#5d30ff"))
    color_list.append(("enig", "#97d9f0"))
    color_list.append(("jack", "#ff9654"))
    color_list.append(("wiz", "#afa4ce"))
    color_list.append(("jones", "#edc9af"))
    color_list.append(("clint", "#c28469"))
    color_list.append(("koh", "#f2be00"))
    color_list.append(("chill", "#f2be00"))
    color_list.append(("horn", "#f2be00"))
    color_list.append(("atlas", "#ffffff"))
    color_list.append(("troop", "#ffffff"))
    # Ici vous pouvez rajouter des exceptions (par défaut les '
    # sont considérés comme des espaces entre 2 noms, il faut des fois
    # rajouter des exceptions, An'art donnerait An et Art sinon)
    # PS : Anart est arbitraire, il doit simplement être unique
    exceptions = []
    exceptions.append(("An'art", "Anart"))
    return(color_list, exceptions)


def couleur(liste_noms, color_list):
    """
        Renvoie le texte correspondant au dégradé de la personne
    """
    color = ""
    for nom in liste_noms:
        nom = nom.lower()
        for (liste, color_hex) in color_list:
            if liste in nom:
                color += color_hex + ":"

    if len(color) > 0:
        color = color[:-1]
    return color


def main():
    delete_old_nodes()
    color_list, exceptions = lists_init()
    for nom in get_liste_noms():
        if not check_if_node(nom):
            insert_line(new_node(nom, color_list, exceptions))


if __name__ == "__main__":
    main()
