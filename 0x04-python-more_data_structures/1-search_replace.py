#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
        else:
            new_list
    return new_list

# another way:
# return [replace if i == search else i for i in my_list]