from home import Home

h0 = Home('Andrew', 'SW 12th St')
print(h0._firstName)
print(h0._address)
print(h0.get_alarm_pin())
h0.set_alarm_pin(1234)
print(h0.get_alarm_pin())

h1 = Home('Brian', 'Fayetteville St')
print(h1._firstName)
print(h1._address)