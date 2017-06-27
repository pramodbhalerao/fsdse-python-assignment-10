def convert(l):
    converted_list = []
    for i in l :
        f = (i * 1.8) + 32
        converted_list.append(f)
    return converted_list



my_list = [32,31,34,33,29,35,30]
convert(my_list)
