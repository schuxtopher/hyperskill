
from collections.abc import Hashable

# remove not hashable objects
only_hashable = [hash(x) for x in object_list if isinstance(x, Hashable)]
# count occurrence
occurrence = {f'{x}': only_hashable.count(x) for x in only_hashable}
# remove singles
dupes = sum(x for x in occurrence.values() if x > 1)
# print duplicates
print(dupes)
