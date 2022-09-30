#!/usr/bin/env python

import shlex


def get_purple_names():
    list_fillotages = []
    non_droit = False
    with open("graph.dot", 'r') as ingraph:
        for line in ingraph:
            if "####" in line:
                non_droit = not non_droit
            if "->" in line and not non_droit:
                list_fillotages.append(get_parrain_fillots(line))
    list_fillotages = list_fillotages[3:]
    origin = ['"Maxime Pulsar"', '"Yanis Pulsar"']
    purple = origin
    while True:
        new = iterate_sons(origin, list_fillotages)
        purple += new
        if new == origin:
            break
        origin = new
    return purple


def delete_links(names_to_keep):
    lines_to_keep = []
    with open("graph.dot", 'r') as ingraph:
        for line in ingraph:
            keep_name = False
            for name in names_to_keep:
                if "->" in line:
                    if name in line.split("->")[0]:
                        keep_name = True
                        break
                elif name in line:
                    keep_name = True
                    break
            if ("->" not in line and "fillcolor" not in line) or keep_name:
                lines_to_keep.append(line)
    with open("graph_purple.dot", 'w') as p:
        p.writelines(lines_to_keep)


def clean_promo_line(names_to_keep, line):
    names_to_keep = [names.strip('"') for names in names_to_keep]
    line = shlex.split(line)
    line = [name for name in line if name in names_to_keep]
    string = " ".join(['"' + name + '"' for name in line])
    return string


def delete_promo(names_to_keep):
    new_lines = []
    with open('graph_purple.dot', 'r') as p:
        stop = False
        for line in p.readlines():
            if stop and line != "}\n":
                new_lines.append(clean_promo_line(names_to_keep, line))
                stop = False
            elif "rank=" in line:
                stop = True
            else:
                new_lines.append(line)
    with open('graph_purple.dot', 'w') as p:
        p.writelines(new_lines)


def iterate_sons(name_list, link_list):
    new_name_list = []
    for link in link_list:
        if link[0] in name_list:
            new_name_list += link[1]
    return new_name_list


def get_parrain_fillots(line):
    parrain, fillots = line.split(" -> ")
    fillots = ''.join(c for c in fillots if c not in ["{", "}"])
    fillots = fillots.split(",")
    fillots = [nom.replace("\n", "").lstrip() for nom in fillots]
    return [parrain, fillots]


def main():
    names_to_keep = get_purple_names()
    delete_links(names_to_keep)
    delete_promo(names_to_keep)


if __name__ == "__main__":
    main()
