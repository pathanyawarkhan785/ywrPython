# # Set items are unchangeable, but you can remove items and add new items.
# """Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key."""

# # The values True and 1 are considered the same value in sets, and are treated as duplicates:
# # The values False and 0 are considered the same value in sets, and are treated as duplicates:
# # A set is a collection which is unordered, unchangeable*, and unindexed.

# st = {1, 4, 6, 2, 4, 1, 2, 3, 4}
# print(st)
# print(len(st))

# for item in st:
#     print(item)

# # to create empty set

# emptySet = set()
# print(type(emptySet))

# set methods

set1 = {"a", "b", "c", "d"}
set2 = {"d", "c", "y", "z"}

# print(set1.union(set2))
# print(set1.intersection(set2))

# set1.intersection_update(set2)
# print(set1)

# print(set1.symmetric_difference(set2))
# print(set1.difference(set2))

# print(set1.isdisjoint(set2))  # disjoint means both sets have no common values.

# print(
#     set1.issuperset(set2)
# )  # superset means set2's all values available in set1, so set1 is superset of set2
# print(
#     set1.issubset(set2)
# )  # subset means set2's all values available in set1, so set2 is subset of set1

# set1.add("k")
# print(set1)

# set1.remove("a")
# print(set1)

# pop
# pop randomly remove values from set but you can access pop value by assign it to a variable.

# popVal = set1.pop()
# print(popVal, set1)

# del
# for deleting a set

# del set1
# print(set1)

# clear
# remove all items from set and make empty set

# set1.clear()
# print(set1, type(set1))

# if "a" in set1:
#     print("present")
# else:
#     print("absent")
