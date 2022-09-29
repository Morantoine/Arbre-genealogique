#!/usr/bin/env python


import re


def get_liste_noms():
    """
    Lit la liste des personnes dans les différentes promos
    """
    file = open("graph.dot", "r+")
    liste_noms = []
    line_list = file.readlines()
    for index in range(len(line_list)):
        line = line_list[index]
        if "Promo" in line:
            promo_line = line_list[index + 3]
            if promo_line != "}\n":
                liste_noms += [s.replace('"', '')
                               for s in promo_line.rstrip().split('" "')]
    file.close()
    return liste_noms


def insert_line(string):
    """Insère string à l'avant-dernière ligne"""
    with open("graph.dot", "r") as f:
        contents = f.readlines()

    num_lines = sum(1 for _ in open("graph.dot"))
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
    file = open("graph.dot", "r+")
    for line in file.readlines():
        if string in line:
            if "color" in line:
                file.close()
                return True
    file.close()
    return False


def new_node(nom, color_list, exceptions, same_names_list):
    """Crée le node avec les bonnes couleurs"""
    line = '    "{}"'.format(nom)
    names_sorted = list(exceptions.keys())
    names_sorted.sort(key=len)
    for exception in names_sorted:
        nom.replace(exception, exceptions[exception])
    nom.replace("'", " ")
    for exception in names_sorted:
        nom.replace(exceptions[exception], exceptions[exception])
    nom = nom.split()
    line += '[fillcolor="{}"]'.format(couleur(nom[1:], color_list))
    nom[0] = ''.join([c for c in nom[0] if not c.isdigit()])
    if nom[0] in same_names_list:
        line += '[label="{}"]'.format(nom[0])
    return line


def lists_init():
    """
    C'est ici que vous devez rajouter le mot-clef à chercher
    dans les noms (pratique pour les noms abregés)
    avec la couleur correspondante
    """
    color_list = {}
    color_list["puls"] = "#a300a3"
    color_list["storm"] = "#a300a3"
    color_list["valh"] = "#00BFFF"
    color_list["chap"] = "#00BFFF"
    color_list["valar"] = "#4b488c"
    color_list["bluff"] = "#4b488c"
    color_list["dice"] = "#ff4d5c"
    color_list["diab"] = "#ff4d5c"
    color_list["lord"] = "#ff4d5c"
    color_list["an'art"] = "#ff4d5c"
    color_list["abso"] = "#5d30ff"
    color_list["ghib"] = "#5d30ff"
    color_list["drag"] = "#3700ff"
    color_list["enig"] = "#97d9f0"
    color_list["jack"] = "#ff9654"
    color_list["wiz"] = "#afa4ce"
    color_list["jones"] = "#edc9af"
    color_list["clint"] = "#c28469"
    color_list["koh"] = "#f2be00"
    color_list["chill"] = "#f2be00"
    color_list["horn"] = "#f2be00"
    color_list["atlas"] = "#ffffff"
    color_list["troop"] = "#ffffff"
    color_list["legen"] = "#ff72fa"
    color_list["sharks"] = "#bdabda"
    color_list["katan'art"] = "#ffcba4"
    color_list["mist"] = "#9e0e40"
    color_list["gold"] = "#ffffff"
    # Ici vous pouvez rajouter des exceptions (par défaut les '
    # sont considérés comme des espaces entre 2 noms, il faut des fois
    # rajouter des exceptions, An'art donnerait An et Art sinon)
    # PS : Anart est arbitraire, il doit simplement être unique
    exceptions = {}
    exceptions["Katan'art"] = "Katanart"
    exceptions["An'art"] = "Anart"
    return (color_list, exceptions)


def longest_list_color(name, listnames):
    color = ""
    longest = ""
    trash = []
    for list_name, color_hex in listnames.items():
        if list_name in name and longest in list_name:
            color = color_hex
            trash.append(list_name)
            longest = list_name
    for name in trash:
        listnames.pop(name, None)
    listnames.pop(longest, None)
    return list, color, listnames


def couleur(liste_noms, color_list):
    """
    Renvoie le texte correspondant au dégradé de la personne
    """
    color = ""
    #print("LISTE DE NOMS : ", liste_noms)
    for nom in liste_noms:
        local_dico = color_list.copy()
        nom = nom.lower()
        list, color_hex, local_dico = longest_list_color(nom, local_dico)
        while len(color_hex) > 0:
            color += color_hex + ":"
            list, color_hex, local_dico = longest_list_color(nom, local_dico)

    if len(color) > 0:
        color = color[:-1]
    return color


def main():
    same_names_list = ["Anaïs"]
    delete_old_nodes()
    color_list, exceptions = lists_init()
    for nom in get_liste_noms():
        if not check_if_node(nom):
            insert_line(new_node(nom, color_list, exceptions, same_names_list))


if __name__ == "__main__":
    main()
