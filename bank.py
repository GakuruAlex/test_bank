#bank function
def value(greeting: str)-> int:
    """_A program that expects  str as input aand outputs an int_

    Args:
        greeting (str): _Input str_

    Returns:
        int: _0 if for str starting with hello, 20 if str starts with h except hello otherwise 100_
    
    Example:
        >>> bank("hello)
            0
        >>> bank("Hello World)
            20
        >>> bank("Morning)
            100
        
    """
    greeting = greeting.strip().lower()



    if greeting.startswith("h"):
        if greeting.split()[0] == "hello" or greeting.split()[0] == "hello,":
            return 0
        else:
            return 20
    else:
        return 100
def main(): #main function
    greeting: str = input("Greeting: ")
    print(f"${value(greeting=greeting)}")



if __name__ == "__main__":
        main()  #invoke main
