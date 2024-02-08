def find_common_elements(list1,list2):
    return list(set(list1)&set(list2))

list1 = input().split()
list2 = input().split()
common_elements = find_common_elements(list1, list2)
print(common_elements)