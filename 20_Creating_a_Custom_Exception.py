class InvalidAgeError(Exception):
    print("Check User Name")

def check_age(age : int) -> str:
    if age < 18: 
        raise InvalidAgeError("Age must be 18 or older")
    else:
        return(f"Age {age} is valid")

 
if __name__ in "__main__":
    try: 
        print(check_age(23))
        print(check_age(3))
    except InvalidAgeError as e:
        print(f"Error: {e}")