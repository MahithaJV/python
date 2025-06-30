collection={1,2,3,"mahitha","bablu",2}

#print(collection,type(collection),collection[1],collection[3],len(collection))
#since the order of the set is not defined the access of members in the set is not possible
print(collection,len(collection))
collection2={12,2}
#print(collection2,type(collection2),len(collection2))

# set methods
collection.add("iiitp")
print(collection)
print(collection.intersection(collection2))

print(collection.union(collection2))
