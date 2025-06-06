# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

class InvalidTempError(Exception):
    """Raised when the oven is set to an invalid temperature"""
    def __init__(self, temp):
        super().__init__(f"Invalid temperature setting: {temp}")

class DigitalOven:
    def __init__(self):
        self.temp = 0

    def set_temp(self, temp):
        if temp == 0:
            self.temp = 0
        elif temp < 100 or temp > 500:
            raise InvalidTempError(temp)
        self.temp = temp

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print(f"Error: {e}")
    else:
        print(f"New temp: {oven.get_temp()}")
    finally:
        print(f"Current temp setting is {oven.get_temp()}")

oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)
