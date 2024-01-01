from sympy import symbols, sympify

def solve(maximize, target_func_string, condition_1_string):
    target_func_string = target_func_string.replace(' ', '')
    condition_1_string = condition_1_string.replace(' ', '')
    
    variables_set = set(char.lower() for char in target_func_string if char.isalpha())
    variables = symbols(variables_set)
    values = {var: 1 for var in variables}
    
    target_func = sympify(target_func_string)
    
    return f"a=1, z={target_func.subs(values)}"
    #return f"bla {maximize}"