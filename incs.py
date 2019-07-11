''' ''' 

def is_zero(x: int) -> bool: 
    ''' takes an int, returns true if it's zero, false otherwise'''
    return x == 0

def is_one(x: int) -> bool: 
    ''' takes an int, returns true if it's one, else false''' 
    return x == 1

def inc1(x: int) -> int: 
    ''' takes an int and adds 1 to it''' 
    return x + 1

def inc2(x: int) -> int: 
    ''' takes an int and adds 2 to it ''' 
    return x + 2


def inc3(x: int) -> int: 
    ''' takes an int and adds 3 to it ''' 
    return x + 3

def inc4(x: int) -> int: 
    ''' takes an int and adds 4 to it '''
    return x + 4

def inc5(x: int) -> int: 
    '''  takes an int and adds 5 to it ''' 
    return x + 5

def inc6(x: int) -> str: 
    ''' takes an int, adds 6 to it, and casts it to string''' 
    return str(x + 6)

def inc7(x: int) -> str: 
    ''' takes an int, adds 7 to it, and casts it to string ''' 
    return f"{x+7}"

if __name__=='__main__': 
    print(str(inc1(inc5(0))), inc6(0))
    print(str(inc3(inc4(1000))), inc7(1000))
