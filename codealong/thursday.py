"""
Sets

unordered
unindexed
so, can't search for items by index number since not indexed. Likewise, can't search for index number by item name.
does not allow duplicates

When printed, seem to come in same order every time anyway, even though considered unordered.

In the below example - it did keep changing the order!!

"""

fruits = {"apple", "banana", "mango"}
print(fruits)

fruits.add("cherry")  # add an item
fruits.remove("banana")  # remove an item
fruits.add("cherry")  # does not allow duplicates
print(fruits)
fruits.discard("mango")  # also removes, but doesn't cause an error message if the item you are trying to remove doesn't exist.

"""
frozen sets

immutable sets
"""

frozen_set = frozenset(["hello", "world"])
print(frozen_set)
# frozen_set.add("more")  # not possible - it's immutable (frozen), therefore can't add to it.

frozen_normal_set = frozenset(fruits)  # can create a frozen set from a normal set
print(frozen_normal_set)

fruits.add(frozen_set)
print(fruits)