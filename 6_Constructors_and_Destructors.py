class Logger:
    def __init__(self):
        print(f"Logger object created!")
     
    def __del__(self):
        print("Logger object destroyed!")
     
if __name__ in "__main__" :
    log1 : Logger = Logger()
    log2 : Logger = Logger()

    del log1
    del log2