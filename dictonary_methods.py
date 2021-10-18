"Some Dictonary methods"

from os import PRIO_PGRP


Dic = {
    "name":"samad",
    "age":19,
    "dict":"comilla"
}

### copy methods copys dictonary

dic_copy = Dic.copy()
print(dic_copy)

### clear methods clear all dict data
print(dic_copy.clear())

### fromkeys methos take list or topul  and value  . 1 st value make keys 2nd value make values
key1 = ["shakil","main","payer"]
val = [2,4,5]
print(dict.fromkeys(key1,val)) 

####
dic_items = Dic.items()
for i in dic_items:
    print(i)
#### get methods take keys and return value
get_met = Dic.get("name")
print(get_met)

### keys methods return all kes
get_keys = Dic.keys()
print(get_keys)

## values methods return all values
get_valus = Dic.values()
print(get_valus)

### pop methods remove item
pop_item = Dic.pop("age")
print(pop_item, Dic)

#### update methods add new data
Dic.update({"country":"bd"})
print(Dic)

### setdefault methods takes keys and return value
print(Dic.setdefault("country"))
###

#### popitem remove last dictonary value
items = Dic.popitem()
print(items)