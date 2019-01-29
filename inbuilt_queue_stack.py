import queue
import heapq

# min heap 1
Q = queue.PriorityQueue(maxsize=6)


Q.put((5, "a"))
Q.put((9, "b"))
Q.put((1, "c"))
Q.put((7, "d"))

print("Full: ", Q.full())

Q.put((9, "e"))
Q.put((10, "f"))
print("Full: ", Q.full())

print(Q.get())
print(Q.get())
print(Q.get())
print(Q.get())


# min heap 2
li = [(5, "a"), (9, "b"), (1, "c"), (7, "d"), (10, "e")]
print("The initial lost is : ",end="")
print(list(li))

heapq.heapify(li)
print("The created heap is : ",end="")
print(list(li))
