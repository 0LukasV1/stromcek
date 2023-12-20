import os
info = input("ktoru zlozku chces prechadzat: ")
def hladat(path, depth=0):
    for item in os.listdir(path):
        if os.path.isdir(path + "\\" + item) and item[0] not in ".$":
            print("-" * depth, item)
            if os.listdir(path + "\\" + item):
                hladat(path + "\\" + item, depth + 1)
hladat(info)