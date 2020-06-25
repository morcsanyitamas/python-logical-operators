true_list = []


def add_true_to_list(*input):
    for elem in list(*input):
        if elem is True:
            true_list.append(elem)


def logical_and(*input):
    add_true_to_list(*input)
    if len(true_list) == len(*input):
        return True
    else:
        return False


def logical_or(*input):
    add_true_to_list(*input)
    if len(true_list) == 0:
        return False
    else:
        return True


def logical_xor(*input):
    add_true_to_list(*input)
    if len(true_list) % 2 == 0:
        return False
    else:
        return True


def logical_nor(*input):
    add_true_to_list(*input)
    if len(true_list) != 0:
        return False
    else:
        return True


def logical_nand(*input):
    add_true_to_list(*input)
    if len(true_list) == len(*input):
        return False
    else:
        return True
