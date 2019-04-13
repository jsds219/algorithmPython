import random

random_list = [random.randint(1, 100) for i in range(50)]

def qsort(qlist):
    lower = []
    higher = []
    sorted_list = []

    if len(qlist) < 1:
        return           # None returned

    center = qlist[0]

    for element in qlist[1:]:
        if element <= center:
            lower.append(element)
        else:
            higher.append(element)

    lower = qsort(lower)

    if  lower != None:
        sorted_list += lower

    sorted_list.append(center)

    higher = qsort(higher)
    if  higher  != None:
        sorted_list += higher

    return sorted_list

print(qsort(random_list))
