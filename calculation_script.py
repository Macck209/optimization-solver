from sympy import symbols, sympify

def solve(maximize, target_func_string, condition_1_string):
    variables_set = set(char.lower() for char in target_func_string if char.isalpha())
    x_variables = symbols(variables_set)
    x_values = {var: 1 for var in x_variables}
    
    target_func = sympify(target_func_string)
    
    return f"a=1, z={target_func.subs(x_values)}"

def calc_target_func(target_func, x_values):
    
    return