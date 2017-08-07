print 'let\'s play'
print 'so, this is what it is all about'
print 'i choosed a no between 1 to 10 and you have to guess it'
print 'but u just have two turns'
user=[1,2]
for a in user:
    a=int(raw_input('Enter the no or type exit for quitting ='))
    if(a>7 or a<3):
        print 'you are going away'
    if(a == 6 or a == 7 or a == 4 or a == 3):
        print  'you are near'
    if(a == 5):
        print 'you guessed it correct'
    if(a == 'exit'):
        exit()