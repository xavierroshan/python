#reverse a string using a stack

string = "roshanxavier"
stack = []
for i in string:
    stack.append(i)
print(stack)
string = ""
for j in range(0, len(stack)):
    string += stack.pop()
print(string)





    