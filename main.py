"""
TODO: A very useful temperature-conversion app.
"""

TEMPERATURE_THRESHOLD : float = 68

def is_cold_f(temp_f: float) -> bool:
    '''
    Determines if supplied temperature in F is below agreed temp
    
    Parameters
    ==========
    temp_f : float
        supplied temperature in F
    
    Returns
    =========
    bool
        True means below the agreed threshold
    '''

    if temp_f < TEMPERATURE_THRESHOLD:
        return True
    else:
        return False

def greet_person() -> None:
    '''Obtains the name of a person from keyboard and greets them'''

    your_name: str = input("What's your name? :>: ")
    print(f"Howdy, {your_name} !" )

def main() -> None:

    print("Hello world!!")

    greet_person()
    

if __name__ == "__main__":
    main() #Runs main function