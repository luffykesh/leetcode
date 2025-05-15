from collections import deque as deque
class MyHashSet:

    def __init__(self):
        self.hashKey = 1000
        self.hashes = [ deque() for _  in range(0,self.hashKey) ]
    
    def getHash(self, key):
        return key % self.hashKey

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        hashIdx = self.getHash(key)
        self.hashes[hashIdx].append(key)

    def remove(self, key: int) -> None:
        hashIdx = self.getHash(key)
        if not self.contains(key):
            return
        self.hashes[hashIdx].remove(key)

    def contains(self, key: int) -> bool:
        hashIdx = self.getHash(key)
        try:
            _ = self.hashes[hashIdx].index(key)
        except ValueError:
            return False

        return True

