stack = {}
def push_element(stack, key, value):
    stack[key] = value
    print(f"Pushed ({key}: {value}) onto the stack.")
def pop_element(stack):
    if not stack:
        print("Stack is empty. Cannot pop.")
        return None
    else:
        key, value = stack.popitem()
        print(f"Popped ({key}: {value}) from stack")
        return key, value
def is_stack_empty(stack):
    return len(stack) == 0
entries = int(input("Enter the number of entries: "))
for i in range(entries):
    key = input("Enter the key: ")
    value = input("Enter the value: ").split()
    push_element(stack, key, value)
print("Nodes in stack:", stack)
key1 = input("Enter the key for new node: ")
value1 = input("Enter the value for new node: ").split()
push_element(stack, key1, value1)
print("Nodes in stack after inserting a new node:", stack)
if not is_stack_empty(stack):
    popped_element = pop_element(stack)
    print(f"Popped element from stack: {popped_element}")
    print("Nodes in stack after popping:", stack)
else:
    print("Cannot delete from an empty stack.")
