class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values_stack = []
        OPERATORS = ['+', '-', '*', '/']

        for token in tokens:
            if token in OPERATORS:
                second_val = values_stack.pop()
                first_val = values_stack.pop()
                output = 0

                match token:
                    case '+':
                        output = first_val + second_val
                    case '-':
                        output = first_val - second_val
                    case '*':
                        output = first_val * second_val
                    case '/':
                        output = int(first_val / second_val)
                    
                values_stack.append(output)
            else: values_stack.append(int(token))
        
        return values_stack.pop()