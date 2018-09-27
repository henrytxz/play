import pendulum
now = pendulum.now()
print now
print now.minute
print now.minute / 15
print now.date()
print type(now.date())

def mod_15_mins(t):
    if not isinstance(t, pendulum.Pendulum):
        raise TypeError('function mod_15_mins expects a pendulum.Pendulum object')
    quarter_in_hour = t.minute / 15
    return pendulum.Pendulum()