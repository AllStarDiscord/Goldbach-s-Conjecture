import sys
import time

print('Generating full prime List up to 10000000')
start_time=time.time()
primeList=[]
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p+= 1
    

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            primeList.append(p)
    return primeList
primeList=SieveOfEratosthenes(10000000)
end_time=time.time()
time_lapsed=end_time - start_time
#print(primeList)
print('Done in '+str(int(time_lapsed))+' seconds.')
#exit=input('a.')
start=input('Do you want to check one number or a range of numbers? (1 for one number, 2 for a range of numbers.)')

if start==('1'):
    x=input('What even number to check?')
    x=int(x)
    if (x<=2 or x%2!=0):
        print('You either inputted an odd number or a number less than 3, please try again.')
        stop=input('Enter Anything to exit.')
        sys.exit()
    i=0
    while (primeList[i]<= x//2):
        d = x - primeList[i]
        if d in primeList:
            print(str(x)+' is the sum of '+str(d)+' and '+str(primeList[i]))
            stop=input('Enter Anything to exit.')
            sys.exit()
        i+=1
    print('Either something went wrong, or you discovered an exception to Goldbachs Conjecture.')
    stop=input('Enter Anything to exit.')
    sys.exit()

if start==('2'):
    x=int(input('What number to start at?'))
    y=int(input('What number to end at?'))
    for z in range(x,(y+1)):
        skip=0
        if (z<=2):
            print(str(z)+' is an invalid input.')
            skip=1
        if (z%2!=0 and skip==0):
            print(str(z)+' is an odd number.')
            skip=1
        if skip==0:
            i=0
            while (primeList[i]<= z//2):
                d = z - primeList[i]
                if d in primeList:
                    print(str(z)+' is the sum of '+str(d)+' and '+str(primeList[i]))
                    skip=1
                    break
                i+=1
            if skip==0:
                print(str(z)+' may be an exception to Goldbachs Conjecture, or something went wrong with the code.')
    stop=input('Done. Enter Anything to exit.')
    sys.exit()
else:
    print('Please try again and enter a 1 or a 2.')
    stop=input('Enter Anything to exit.')
    sys.exit()
