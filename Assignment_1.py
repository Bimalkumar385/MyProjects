# Different functions used in LIST

list_value=['pizzaHut','KFC','Dominos','burgerKing']
print(list_value)
list_value.append('McDonalds')
print(list_value)
list_value.remove('KFC')
print(list_value)
del list_value[2]
print(list_value)
list_value.append('CCD')
print(list_value)
list_value.sort()
print(list_value)
list_value.reverse()
print(list_value)
x=list_value.count('pizzaHut')
print(x)
list_value.clear()
print(list_value)





# METHODS OF DICTIONARY.

weeks={"sun":"sunday","mon":"monday","tues":"tuesday","wed":"wednesday"}
print(weeks)
x=weeks.get("mon")
print(x)
x=weeks.keys()
print(x)
x=weeks.items()
print(x)
x=weeks.copy()
print(x)
x=weeks.pop("wed")
print(x)
x=weeks.popitem()
print(x)




# METHODS OF TUPLE

tuple_value=(9,8,6,0,8,3,1,2,3,2)
print(tuple_value)
x=tuple_value.count(8)
print(x)
x=tuple_value.index(3)
print(x)




# METHODS OF SET

set1={0,1,2,3,4}
set2={3,4,5,6,7}
print(set1)
print(set2)
set1.add(5)
print(set1)
set1.copy()
print(set1)
set1.discard(5)
print(set1)
x=set1.union(set2)
print(x)
set1.update(set2)
print(set1)
x=set1.symmetric_difference(set2)
print(x)
set2.pop()
print(set2)
x=set1.issuperset(set2)
print(x)
x=set1.intersection(set2)
print(x)
set1.clear()
print(set1)
