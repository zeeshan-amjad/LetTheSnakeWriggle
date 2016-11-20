def nonUnique (data):
    data = [i for i in data if data.count (i) > 1]
    return data
    
print (nonUnique ([1, 2, 3, 3, 1]))
