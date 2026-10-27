class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        current_string = ""
        def dfs(number_of_open_parenthesis, number_of_closed_parenthesis):
            nonlocal current_string
            if number_of_closed_parenthesis == n:
                output.append(current_string)
                return
            
            # open parenthesis
            if number_of_open_parenthesis < n:
                current_string = current_string + "("
                dfs(number_of_open_parenthesis + 1, number_of_closed_parenthesis)
                current_string = current_string[:-1]

            # closed parenthesis
            if number_of_closed_parenthesis < number_of_open_parenthesis:
                current_string = current_string + ")"
                dfs(number_of_open_parenthesis, number_of_closed_parenthesis + 1)
                current_string = current_string[:-1]
        
        dfs(0, 0)
        return output