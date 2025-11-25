def count_items(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


my_list = ['Radiohead', 'Radiohead', 'Coldplay',
           'Oasis', 'Radiohead', 'Oasis', 'Nigga']
counts = count_items(my_list)
print(counts)
