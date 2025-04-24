from typing import Union

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c: Union[int, float]) -> float:
        return (c * 9/5) + 32
    
if __name__ in "__main__" :
    temperature : TemperatureConverter = TemperatureConverter()
    print(temperature.celsius_to_fahrenheit(7))
    print(temperature.celsius_to_fahrenheit(0)) 