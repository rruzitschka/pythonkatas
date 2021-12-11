#implementation

def minimum_val(val_set):
    return min(val_set)

def maximum_val(val_set):
    return max(val_set)

def num_elements(val_set):
    return len(val_set)

def average_val(val_set):
    sum=0.0
    set_len = len(val_set)
    for i in range(set_len):
        sum += val_set[i]

    return sum/set_len

