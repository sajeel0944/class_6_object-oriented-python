def log_function_call(func):
    def wrapper() -> None:
        print("Function is being called")
        return func()

    return wrapper

@log_function_call
def say_hello() -> None:
    print("Hello")
 
if __name__ in "__main__":
    say_hello()