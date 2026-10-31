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
    
    
def is_empty():