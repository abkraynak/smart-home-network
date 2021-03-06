# home.py

from .alarm import Alarm
from .light import Light
from .lock import Lock

class Home(object):
    def __init__(self, first_name: str, address: str):
        self._username = 'abkraynak'
        self._password = 'mypassword'
        self._first_name = first_name
        self._address = address
        self._alarm = Alarm(1234)
        self._lights = []
        self._locks = []

    def authenticate(self, user: str, passwd: str) -> bool:
        if user == self._username and passwd == self._password:
            return True
        return False

    def sample_home(self):
        self.add_light('Kitchen')
        self.add_light('Dining Room')
        self.add_light('Living Room')
        self.add_light('Bathroom')
        self.add_light('Bedroom')
        self.add_light('Guest Bedroom')
        self.add_light('Laundry Room')
        self.add_light('Garage')
        self.add_light('Front Porch')

        self.add_lock('Front Door', 2345)
        self.add_lock('Garage Door', 5432)
        self.add_lock('Back Door', 2345)
        self.add_lock('Side Door', 5432)
    
    def add_light(self, name: str):
        new_light = Light(name)
        self._lights.append(new_light)

    def get_light_color(self, name: str):
        for light in self._lights:
            if light._name == name:
                return light.get_color()

    def set_light_color(self, name: str, r: int, g: int, b: int):
        for light in self._lights:
            if light._name == name:
                light.set_color(r, g, b)

    def get_light_brightness(self, name: str):
        for light in self._lights:
            if light._name == name:
                return light.get_brightness()

    def set_light_brightness(self, name: str, level: int):
        for light in self._lights:
            if light._name == name:
                light.set_brightness(level)

    def get_light_status(self, name: str):
        for light in self._lights:
            if light._name == name:
                return light.get_status()  
    
    def enable_light(self, name: str):
        for light in self._lights:
            if light._name == name:
                light.enable()
    
    def disable_light(self, name: str):
        for light in self._lights:
            if light._name == name:
                light.disable()

    def print_lights(self):
        for light in self._lights:
            print(light._name, light._status, light._color, sep = ' - ')

    def add_lock(self, name: str, pin: int):
        new_lock = Lock(name, pin)
        self._locks.append(new_lock)

    def get_lock_status(self, name: str):
        for lock in self._locks:
            if lock._name == name:
                return lock.get_status()

    def enable_lock(self, name: str, pin: int):
        for lock in self._locks:
            if lock._name == name:
                lock.enable(pin)

    def disable_lock(self, name: str, pin: int):
        for lock in self._locks:
            if lock._name == name:
                lock.disable(pin)

    def print_locks(self):
        for lock in self._locks:
            print(lock._name, lock._enable, sep = ' - ')