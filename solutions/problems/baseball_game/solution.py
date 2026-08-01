class Solution:
    def calPoints(self, operations):
        stack = []
        total = 0

        for op in operations:
            if op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
                total += val

            elif op == "D":
                val = stack[-1] * 2
                stack.append(val)
                total += val

            elif op == "C":
                total -= stack.pop()

            else:
                val = int(op)
                stack.append(val)
                total += val

        return total