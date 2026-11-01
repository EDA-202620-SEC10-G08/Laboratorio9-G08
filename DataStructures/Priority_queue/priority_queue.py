from DataStructures.Priority_queue import pq_entry as pqe
from DataStructures.List import array_list as al

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    return False

def exchange(my_heap, pos_1, pos_2):
    al.exchange(my_heap["elements"], pos_1, pos_2)
    return my_heap["elements"]

def new_heap(is_min_pq=True):
    if is_min_pq:
        cmp = default_compare_lower_value
    else:
        cmp = default_compare_higher_value
    heap = {
        "elements": al.new_list(),
        "size": 0,
        "cmp_function": cmp
    }
    al.add_first(heap["elements"], None)
    return heap


def insert(my_heap, priority, value):
    entrada = pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], entrada)
    my_heap["size"] += 1
    swim(my_heap, my_heap["size"])  
    return my_heap

def swim(my_heap, pos):
    while pos // 2 != 0:
        padre_pos = pos // 2
        elem_hijo = al.get_element(my_heap["elements"], pos)
        elem_padre = al.get_element(my_heap["elements"], padre_pos)
        if not my_heap["cmp_function"](elem_padre, elem_hijo):
            exchange(my_heap, pos, padre_pos)
            pos = padre_pos
        else:
            break
    return my_heap

def size(my_heap):
    return my_heap["size"]
        
def is_empty(my_heap):
    if size(my_heap) == 0:
        return True
    else:
        return False

#Nick
def priority(my_heap, parent, child):
    pass

#JP
def sink(my_heap, pos):
    pass

#Nick
def remove(my_heap):
    pass

#Nick
def get_first_priority(my_heap):
    pass

#JP
def is_present_value(my_heap, value):
    pass

#JP
def contains(my_heap, value):
    pass

#Nick
def improve_priority(my_heap, priority, value):
    pass
