#!/usr/bin/env python

class SquareHeap:
    def __init__(self):
        self._key_dict = {}
        self._heap = []
        self._length = 0
         
    def _lt(self, index1, index2):
        return self._heap[index1][1] < self._heap[index2][1]
 
    def _swap(self, index1, index2):
        elem1 = self._heap[index1]
        elem2 = self._heap[index2]
        self._heap[index1] = elem2
        self._heap[index2] = elem1
        self._key_dict[elem1[0]] = index2
        self._key_dict[elem2[0]] = index1
         
    def _decreaseOrder(self, child):
        while child > 0:
            parent = (child - 1)/ 2
            if not self._lt(child, parent):
                break
            self._swap(parent, child)
            child = (child - 1) / 2
 
    def _increaseOrder(self):
        parent = 0
        lchild = 1
        while lchild < self._length:
            rchild = lchild + 1
            if rchild == self._length:
                if self._lt(lchild, parent):
                    self._swap(lchild, parent)
                    parent = lchild
                else:
                    break
            else:
                if self._lt(lchild, parent):
                    if self._lt(lchild, rchild):
                        self._swap(lchild, parent)
                        parent = lchild
                    else:
                        self._swap(rchild, parent)
                        parent = rchild
                else:
                    if self._lt(rchild, parent):
                        self._swap(rchild, parent)
                        parent = rchild
                    else:
                        break
            lchild = parent * 2 + 1
             
    def empty(self):
        return self._length == 0
         
    def push(self, key, weight):
        self._heap.append((key, weight))
        self._key_dict[key] = self._length
        self._decreaseOrder(self._length)
        self._length = self._length + 1
 
    def pop(self):
        self._length = self._length - 1
        old_elem = self._heap[0]
        self._swap(0, self._length)
        del self._key_dict[old_elem[0]]
        del self._heap[self._length]
        self._increaseOrder()
        return old_elem
     
    def decreaseKey(self, key, weight):
        if self._key_dict.has_key(key):
            index = self._key_dict[key]
            if weight < self._heap[index][1]:
                self._heap[index] = (key, weight)
                self._decreaseOrder(index)
        else:
            self.push(key, weight)



if __name__ == "__main__":
    import sys
    sq_heap = SquareHeap()
    sq_heap.push("a", 4)
    sq_heap.push("b", 3)
    sq_heap.push("c", 1)
    sq_heap.push("d", 2)
    sq_heap.push("e", 5)
    sq_heap.push("f", 6)
    sq_heap.push("g", 4)
    sq_heap.push("h", 7)
    while not sq_heap.empty():
        print sys.stdout.write(str(sq_heap.pop()) + ' ')
    print 
