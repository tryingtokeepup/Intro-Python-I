# imagine a literal stack of plates
# if excedes some threshold, the stack will break
# implement a data struct that stops increasing once it hits the capacity(?) of said stack and builds another one


class SetOfStacks:
    def __init__(self, threshold, plates):
        self.threshold = threshold
        self.plates = plates

    def popStack(self, stack):
        return stack[-1]

    def pushStack(self, stack, value):
        # if stack.length > stack.threshold
        #   return new stack.append(value)
        # elif:
        #   return stack.append(value)
        return stack.append(value)


stack = SetOfStacks(4, 0)

stack.pushStack(stack, 5)
print()
