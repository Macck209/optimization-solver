from sympy import symbols, sympify
import random, copy

def solve(maximize, target_func_string, conditions_strings, positive_condition, integer_condition, generations_num, mutation_factor):
    variables_set = set(char.lower() for char in target_func_string if char.isalpha())
    x_variables = symbols(variables_set)
    x_values = {var: 1 for var in x_variables}
    new_x_values = copy.copy(x_values)
    
    conditions = []
    for cond_string in conditions_strings:
        conditions.append(sympify(cond_string))
    print(conditions_strings) #test
    target_func_equasion = sympify(target_func_string)
    target_func = calc_target_func(target_func_equasion, x_values, conditions, maximize)
    new_target_func = target_func
    
    repeating_output_counter = 0
    
    for i in range(generations_num):
        for j in range(50):
            new_x_values = copy.copy(x_values)
            for var in new_x_values:
                if integer_condition:
                    mutation = random.randint(-mutation_factor, mutation_factor)
                else:
                    mutation = random.uniform(-mutation_factor, mutation_factor)
                    
                new_x_values[var] += mutation
                
                if positive_condition:
                    new_x_values[var] = abs(new_x_values[var])
                    
            new_target_func = calc_target_func(target_func_equasion, new_x_values, conditions, maximize)
            
            if (maximize and new_target_func>target_func) or (not maximize and new_target_func<target_func):
                x_values = copy.copy(new_x_values)
                target_func = new_target_func
                repeating_output_counter = 0
                
                #print(f"{x_values} \nz={target_func}")
                break
            elif new_target_func == target_func:
                repeating_output_counter += 1
                
                #print("aaa")
                break
            else:
                break
            
        # TODO introduce config option for this
        if repeating_output_counter >= 20:
            break
            
    return f"{x_values} \nz={target_func}"

def init_variables():
    pass

def mutate():
    pass

def calc_target_func(equasion, values, conditions, maximize):
    penalty = 0
    
    for cond in conditions:
        penalty += (-1000000 if maximize else 1000000) if not bool(cond.subs(values)) else 0
        if bool(cond.subs(values)):
            print("a") 
        else:
            print("b")
    
    return equasion.subs(values) + penalty