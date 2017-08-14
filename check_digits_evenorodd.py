N=int(raw_input("Enter your no="))
a,b,c,d=N%2,N/10%2,N/100%2,N/1000%2
if(a^b)or(a^c)or(a^d):
    print 'the no contain both even and odd digits'
elif a:
    print 'the no contains all odd digits'
else:
    print 'the no conatains all even digits'