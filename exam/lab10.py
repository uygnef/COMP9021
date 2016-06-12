from general_tree import *

file = open('tree.txt','r')
none_blank_lines = []

for line in file:
    line = line.rstrip()
    for i in line:
        if i.isdigit():
            none_blank_lines.append(line)
            break

none_blank_lines.reverse()
def get_level(element):
    count = 0
    for i in element:
        if not i.isdigit():
            count += 1
        else:
            return count

def build_tree(List,now_level):
    now_using = List.pop()
 #   now_level = get_level(now_using)
    now_value = int(now_using[now_level:])
    tree = GeneralTree(now_value)
    while List:
        next_line = List[-1]
        if get_level(next_line) > now_level +1:
            return None
        if get_level(next_line) == now_level + 1:
            tree.children.append(build_tree(List,get_level(next_line)))
        else:
            return tree
    return tree

def print_tree(tree,level):
    print('\t'*level, tree.value)
    for child in tree.children:
        print_tree(child, level + 1)
print(none_blank_lines)
print_tree(build_tree(none_blank_lines, 0),0)




