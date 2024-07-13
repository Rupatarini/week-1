graph={ }
enterie=int(input("enter the number of enterie:"))
for i in range(enterie):
    key=input("enter the key:")
    value=input("enter the value:").split()
    graph[key]=value
print("the user Nodes are :",graph)
key=input("enter the user specified node:")
print("display the adjucent node for user specified node:",graph[key])
