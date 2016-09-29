def getFloat():
    print('please enter a float value')
    while True:
        try:
            num = float( input() )
        except ValueError:
            print( "That is not a number -- please try again" )
            continue
        return num

def getInteger():
    print('please enter a integer value')
    while True:
        try:
            num = int( input() )
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num

def getString():
    print('please enter a string')
    line = input()
    return line.strip()

def getLetter():
    print('please enter a letter')
    while True:
        line = input()
        line = line.strip()
        line = line.upper()
        if len( line ) != 1:
            print( "Please enter exactly one character" )
            continue
        if line < 'A' or line > 'Z':
            print( "Please enter a letter from the alphabet" )
            continue
        return line
