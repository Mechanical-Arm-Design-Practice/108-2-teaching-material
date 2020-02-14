def do_nothing():
    pass

def say_something():
    print("Hello~")

def agree():
    return True

def echo(input):
    return str(input) + " " + str(input)

def is_none(thing):
    if thing is None:
        #print("It's None.")
        return None
    elif thing :
        #print("It's True.")
        return True
    else:
        #print("It's False.")
        return False

def menu(wine, entree, dessert):
    return {"wine":wine, "entree":entree, "dessert":dessert}

def menu_today(wine, entree, dessert="pudding"):
    return {"wine":wine, "entree":entree, "dessert":dessert}

def buggy(arg, result=[]):
    result.append(arg)
    return result

def buggy_2(arg):
    result=[]
    result.append(arg)
    return result

def print_arg(*args):
    print("Positional argument tuple: ", args)

def print_more_arg(input_1, input_2, *args):
    print("Input 1 is: ", input_1)
    print("Input 2 is: ", input_2)
    print("All the rest: ", args)

def printkwargs(**kwargs):
    print("Keyword arguments:", kwargs)

def print_if_true(input, check):
    '''
    Print the first argument if a second argument is true.
    '''
    if check:
        print(input)

def sum_args(*args):
    return(sum(args))

def run_with_positional_args(func, *args):
    return func(*args)

def main():
    '''
    if agree():
        say_something()
    else:
        print(echo(2))
        print(do_nothing())
    '''
    '''
    type_list = [None, True, False, 0, 0.0, (), [], {}, set()]
    for thing in type_list:
        print(str(thing) + ' is ', str(is_none(thing)))
    '''
    '''
    print(menu("chardonnay", "chicken", "cake"))
    print(menu(dessert="cake", wine="chardonnay", entree="chicken"))
    print(menu_today("chardonnay", "beef"))
    print(menu_today("chardonnay", "beef", dessert="cake"))
    '''
    '''
    print(buggy('a'))
    print(buggy('b'))

    print(buggy_2('a'))
    print(buggy_2('b'))
    '''
    '''
    print_more_arg("hello", 1, 2, 3)
    '''
    '''
    dict_a = {"wine":"chardonnay", "entree":"chicken", "dessert":"cake"}
    print(dict_a)
    printkwargs(wine="chardonnay", entree="chicken", dessert="cake")
    '''
    '''
    print(print_if_true.__doc__)
    '''
    print(run_with_positional_args(sum_args, 1, 2, 3, 4))

if __name__ == "__main__":
    main()