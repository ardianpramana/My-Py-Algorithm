class ShortInputException(Exception):
    ''' a user defined exception class. '''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Why do you do an EOF on me?')

except KeyboardInterrupt:
    print('Sorry, another key pressed')

except ShortInputException as ex:
    print(('ShortInputException: the input was ' + '{0} long, expected at least {1}').format(ex.length, ex.atleast))

else:
    print('No exception was raised.')