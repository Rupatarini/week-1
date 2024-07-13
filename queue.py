class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, key, value):
        self.queue.append((key, value))
        print(f"Enqueued node ({key}: {value}) onto the queue.")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        else:
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def display(self):
        print("Current queue:", dict(self.queue))  
class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, key, value):
        self.nodes.append((key, value))
        print(f"Added node ({key}:{value}) to the graph.")

    def display_nodes(self):
        print("Nodes in graph:", dict(self.nodes))  
graph = Graph()
queue = Queue()
num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    key = input("Enter the key: ")
    value = input("Enter the value: ").split()
    graph.add_node(key, value)
    queue.enqueue(key, value)
print("\nGraph after adding nodes:")
graph.display_nodes()
print("\nQueue after enqueueing nodes:")
queue.display()
key1 = input("\nEnter the key for the new node: ")
value1 = input("Enter the value for the new node: ").split()
graph.add_node(key1, value1)
queue.enqueue(key1, value1)
print("\nGraph after adding the new node:")
graph.display_nodes()
print("\nQueue after enqueueing the new node:")
queue.display()
if not queue.is_empty():
    dequeued_node = queue.dequeue()
    print(f"\nDequeued node from the queue: {dequeued_node}")
    queue.display()
else:
    print("\nCannot dequeue from an empty queue.")

