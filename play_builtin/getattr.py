class Hi(object):
    field = 'greeting'

print Hi.__name__
print getattr(Hi, '__name__')
print getattr(Hi, 'field')
