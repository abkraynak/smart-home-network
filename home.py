from alarm import Alarm

class Home(object):
    def __init__(self, firstName: str, address: str):
        self._firstName = firstName
        self._address = address
        self._alarm = Alarm(0)

    def get_alarm_pin(self) -> int:
        return self._alarm.get_pin()

    def set_alarm_pin(self, pin: int):
        self._alarm.set_pin(pin)

    def get_alarm_status(self) -> int:
        return self._alarm.get_status()

    def enable_alarm(self, pin: int):
        self._alarm.enable(pin)

    def disable_alarm(self, pin: int):
        self._alarm.disable(pin)