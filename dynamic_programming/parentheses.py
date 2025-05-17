from functools import lru_cache
import operator

"""
Turns a string like "66*23+2*0-4" into a list: 
[66, '*', 23, '+', 2, '*', 0, '-', 4]
"""
#TODO for every '-' count as expression or negative number to put parentheses around
#Ex: 2-4 -> 2-(4) or 2(-4)
def parse_expression(expr):
    tokens = []
    num = ''

    # accumulate digits in num until operator is reached
    for char in expr:
        # if char is operator
        if char in '+-*/':
            # append accumulated digits and operator (current char)
            tokens.append(int(num))
            tokens.append(char)
            num = ''
        # else if char is a digit add digit to num string
        else:
            num += char
    # append final/leftover num
    tokens.append(int(num))
    return tokens
"""
Performs arithmatic based on operator
"""
def apply_op(a, b, op):
    # TODO consider division
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        # integer division with zero check
        # inf can either be included in "divergent" solution or considered invalid answer
        # return division if divisor != 0, else return inf (Not a number?)
        '/': lambda x, y: x // y if y != 0 else float('inf')
    }
    # calls respective operator based on dictionary mapping, returns result as number
    return ops[op](a, b)


"""
Main function for finding max value
"""
def max_expression_value(expr):
    # first create list of tokens by parsing original string
    tokens = parse_expression(expr)

    """
    Recursive function with memoization
    Returns (min_val, min_expr, max_val, max_expr)
    i and j are parameters for indices within tokens list
    """
    """decorator to automatically cache results of previous calls, 
    so repeated calls during recursive process are processed faster
    Ex: if compute(0,4) is called, result will be remembered if compute(0,4)
    is called again
    None argument for unbounded cache size"""
    @lru_cache(None)
    def compute(i, j):
        #  if theres only one index in equation return that index's value
        if i == j:
            val = tokens[i]
            return val, str(val), val, str(val)

        # initialize min and max values to "highest" and "lowest" possible values
        min_val = float('inf')
        max_val = float('-inf')
        min_expr = max_expr = ""

        # loop through operator tokens through looping through odd indices of tokens list
        #TODO implement splitting of multi-digit numbers with parentheses
        for k in range(i + 1, j, 2):  # k is operator index

            # for each operator recursively call compute for left and right sides of operator
            op = tokens[k]
            l_min, l_expr_min, l_max, l_expr_max = compute(i, k - 1)
            r_min, r_expr_min, r_max, r_expr_max = compute(k + 1, j)

            # try all permutations: min-left w/ min right, min-left w/ max right...
            for a_val, a_expr in [(l_min, l_expr_min), (l_max, l_expr_max)]:
                for b_val, b_expr in [(r_min, r_expr_min), (r_max, r_expr_max)]:
                    # determine result of basic 2 num, 1 op expression
                    result = apply_op(a_val, b_val, op)
                    expr_str = f"({a_expr}{op}{b_expr})"
                    # track the best min and max results and expressions seen so far
                    if result < min_val:
                        min_val = result
                        min_expr = expr_str
                    if result > max_val:
                        max_val = result
                        max_expr = expr_str
        # return best result and expression for this recursive call
        return min_val, min_expr, max_val, max_expr

    return compute(0, len(tokens) - 1)

# Example usage
test_expressions = [
    "6+2*0-4",
    "3+8*2",
    "5-3+2*4",
    "10+2*3-4",
    "8*3/2+1",
    "9+5*2-6/3",
    "12/3+4*2-5",
    "7*2-3*4",
    "4+6*2/3-1",
    "66*23+2*0-4"
]

for expr in test_expressions:
    min_val, min_expr, max_val, max_expr = max_expression_value(expr)
    print(f"Expression: {expr}")
    print(f"  Min Value: {min_val} from {min_expr}")
    print(f"  Max Value: {max_val} from {max_expr}")
    print("-" * 50)
