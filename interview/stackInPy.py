class stack:
    def StackUsingList(self):
        lst = []

        lst.append(5)
        lst.append(10)
        lst.append(15)

        lst.pop()

        # here last 15 appended also popped 15 so it's stack LIFO(last in first out)

        print(lst)


newStack = stack()
newStack.StackUsingList()
