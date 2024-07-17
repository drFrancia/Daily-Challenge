## Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos.
class Stack:
    def __init__(self, capacity=5):
        self.stack = []
        self.capacity = capacity
    
    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            print("La pila está llena")
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print("La pila está vacía")
            return None
    
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("La pila está vacía")
            return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity


class Queue:
    def __init__(self, capacity=5):
        self.queue = []
        self.capacity = capacity
    
    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            print("La cola está llena")
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            print("La cola está vacía")
            return None
    
    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("La cola está vacía")
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) == self.capacity

print("Prueba de la pila:")
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6) 

print("Elemento superior:", stack.peek())

print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop())
print("Pop:", stack.pop()) 

print("\nPrueba de la cola:")
queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

print("Elemento frontal:", queue.front())

print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
print("Dequeue:", queue.dequeue())
