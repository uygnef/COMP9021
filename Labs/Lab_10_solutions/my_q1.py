from general_tree import *

file = open('tree.txt','r')
none_blank_lines = []
for lines in file:
    now_line = lines.rstrip()
    if now_line:
        none_blank_lines.append(now_line)
none_blank_lines.reverse()

def get_level(a):
    count = 0
    for i in a:
        if i =='\t':
            count += 1
    return count

def build_general_tree(List,level):
    now_item = List.pop()
    now_level = get_level(now_item)
    now_value = int(now_item[now_level:])
    tree = GeneralTree(now_value)
    while List:
        next_level = get_level(List[-1])
        if next_level == now_level + 1:
            tree.children.append(build_general_tree(List,level + 1))
        elif next_level > now_level + 1:
            return None
        else:
            return tree
    return tree

tree = build_general_tree(none_blank_lines,0)
'''for i in none_blank_lines:
    print(get_level(i))'''
