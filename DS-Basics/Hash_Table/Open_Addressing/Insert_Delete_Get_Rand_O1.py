"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

"""
import random

# Slow
class RandomizedSet1:

    def __init__(self):
        self.set = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        rr = random.randint(0,len(self.set)-1)
        for i,e in enumerate(self.set):
            if i == rr:return e

# Fast
class RandomizedSet2:
    def __init__(self):
        self.list = []
        self.dict = {}
        
    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            index = self.dict[val]
            self.dict[self.list[-1]] = index
            self.list[index], self.list[-1] = self.list[-1], self.list[index]
            self.list.pop()
            del self.dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


if __name__ == "__main__":
    obj = RandomizedSet2()
    print(obj.insert(1))
    print(obj.remove(2))
    print(obj.insert(2))
    print(obj.getRandom())
    print(obj.remove(1))
    print(obj.insert(2))
    print(obj.getRandom())