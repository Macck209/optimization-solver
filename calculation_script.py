from sympy import symbols, sympify
import random, copy

def solve(maximize, target_func_string, conditions_strings, positive_condition, integer_condition, generations_num, mutation_factor):
    result=""
    
    # Points for graph generation
    progress_data = []
    
    variables_set = set(char.lower() for char in target_func_string if char.isalpha())
    x_variables = symbols(variables_set)
    x_values = {var: 1 for var in x_variables}
    
    generations_num = int(abs(generations_num)) if generations_num>=100 else 100
    
    conditions = []
    for cond_string in conditions_strings:
        try:
            conditions.append(sympify(cond_string))
        except Exception:
            result += f"Wrong formatting in condition: {cond_string}\n"
    
    try:
        target_func_equasion = sympify(target_func_string)
    except Exception:
        result += f"Wrong formatting of target function. Showing -2*a^2 instead\n"
        target_func_equasion = sympify("-2*a^2")
    
    target_func = calc_target_func(target_func_equasion, x_values, conditions, maximize)
    
    repeating_output_counter = 0
    
    for i in range(1, generations_num+1):
        # TODO introduce config option for j
        for j in range(50):
            new_x_values = copy.copy(x_values)
            mutate(new_x_values, mutation_factor, integer_condition, positive_condition)
                    
            new_target_func = calc_target_func(target_func_equasion, new_x_values, conditions, maximize)
            
            if (maximize and new_target_func>target_func) or (not maximize and new_target_func<target_func):
                x_values = copy.copy(new_x_values)
                target_func = new_target_func
                repeating_output_counter = 0
                break
            
            elif new_target_func == target_func:
                repeating_output_counter += 1
        
        # data entries for the graph
        progress_data.append((i, target_func))
        
        # TODO introduce config option for this
        if repeating_output_counter >= 20:
            break
            
    return f"{x_values} \nz={target_func}", progress_data

def mutate(values, mutation_factor, integer_condition, positive_condition):
    for var in values:
        if integer_condition:
            mutation = random.randint(-mutation_factor, mutation_factor)
        else:
            mutation = random.uniform(-mutation_factor, mutation_factor)
            
        values[var] += mutation
        
        if positive_condition:
            values[var] = abs(values[var])

def calc_target_func(equasion, values, conditions, maximize):
    penalty = 0
    
    # TODO catch substitution of sqrt(-a) and other exceptions
    for cond in conditions:
        penalty += (-10**10 if maximize else 10**10) if not cond.subs(values) else 0
    
    return equasion.subs(values) + penalty