def get_liste_noms():
    file = open("graph.dot", 'r+')
    L = []
    get_in = False
    for line in file.readlines():
        if get_in:
            L.append(line.rstrip("\n"))
        if "----" in line:
            if not get_in:
                get_in = True
            else:
                break
    L.pop()
    file.close()
    return(L)


def insert_line(string):
    with open("graph.dot", "r") as f:
        contents = f.readlines()

    contents.insert(num_lines - 1, string + "\n")

    with open("graph.dot", "w") as f:
        contents = "".join(contents)
        f.write(contents)


def check_if_node(string):
    file = open("graph.dot", 'r+')
    for line in file.readlines():
        if string in line:
            if "color" in line:
                file.close()
                return True
    file.close()
    return False


def new_node(nom):
    line = '    "{}"'.format(nom)
    exceptions = [("An'art", "Anart")]
    for exception, replacement in exceptions:
        nom.replace(exception, replacement)
    nom.replace("'", " ")
    for exception, replacement in exceptions:
        nom.replace(replacement, exception)
    nom = nom.split()
    line += '[fillcolor="{}"]'.format(couleur(nom[1:]))
    return(line)


def dic_init():
    color_dico = {}
    color_dico["puls"] = "#a300a3"
    color_dico["storm"] = "#a300a3"
    color_dico["valh"] = "#00BFFF"
    color_dico["chap"] = "#00BFFF"
    color_dico["valar"] = "#4b488c"
    color_dico["bluff"] = "#4b488c"
    color_dico["dice"] = "#ff4d5c"
    color_dico["diab"] = "#ff4d5c"
    color_dico["lord"] = "#ff4d5c"
    color_dico["an'art"] = "#ff4d5c"
    color_dico["abso"] = "#5d30ff"
    color_dico["ghib"] = "#5d30ff"
    color_dico["enig"] = "#97d9f0"
    color_dico["jack"] = "#ff9654"
    color_dico["wiz"] = "#afa4ce"
    color_dico["jones"] = "#edc9af"
    color_dico["clint"] = "#c28469"
    color_dico["koh"] = "#f2be00"
    color_dico["chill"] = "#f2be00"
    color_dico["horn"] = "#f2be00"
    color_dico["atlas"] = "ffffff"
    color_dico["troop"] = "ffffff"


def couleur(liste_noms):
    color = ""
    for liste in liste_noms:
        liste = liste.lower()
        if "puls" in liste or "storm" in liste:
            color += "#a300a3:"
        if "valh" in liste or "chap" in liste:
            color += "#00BFFF:"
        if "valar" in liste or "bluff" in liste:
            color += "#4b488c:"
        if "dice" in liste or "lord" in liste or "diab" in liste or "an'art" in liste:
            color += "#ff4d5c:"
        if "abso" in liste or "ghib" in liste:
            color += "#5d30ff:"
        if "enig" in liste:
            color += "#97d9f0:"
        if "jack" in liste:
            color += "#ff9654:"
        if "wiz" in liste:
            color += "#afa4ce:"
        if "jones" in liste:
            color += "#edc9af:"
        if "clint" in liste:
            color += "#c28469:"
        if "koh" in liste or "chill" in liste or "horn" in liste:
            color += "#f2be00:"
        if "atlas" in liste or "troop" in liste:
            color += "#ffffff:"
    if len(color) > 0:
        color = color[:-1]
    return color


num_lines = sum(1 for _ in open('graph.dot'))


def main():
    dic_init()
    for nom in get_liste_noms():
        if not check_if_node(nom):
            insert_line(new_node(nom))


if __name__ == "__main__":
    main()
