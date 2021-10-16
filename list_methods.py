
" About Some List methods"


my_list =[1,2,3,4,1,1,1]
##
my_list.append(3)
##
my_list.insert(0,9)
##
list_copy = my_list.copy()
##
rev = my_list.reverse()
print(rev)
#
clear =my_list.clear()
##sort
sort = my_list.sort()
###
my_list.pop(3)
print(my_list)
##
list_ =[8,5,4]
ext_list =my_list.extend(list_)
print(ext_list)
###
print(my_list)
print(my_list.index(1))