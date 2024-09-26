def count(sequence, item):
    tipo = type(item)
    print (tipo)
    count = 0
    if tipo == str or tipo == int or tipo == float:
        for element in sequence:
            if element == item:
                count +=1
    if tipo == list:
        for element in sequence:
            # print (element)
            for value in item:
                # print (value)
                if value == element:
                    count +=1
    return count
         

print (count([1, 2, 1.2, 1], [2,1]))