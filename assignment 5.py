number1 = [1,2,3,4,5,6,7,8,9,10]
number2 = [1,2,5,5,6,7,10,9,3,3,4,4]
number = [1,2,5,11,8,93,4,3]

#print element of the list 1 per line
def func1 (numbers):
    for i in numbers:
        print (i)

# print in reverse order

def func2 (numbers):
    numbers.reverse()
    for i in numbers:
        print (i)
        
        
#print in reverse same line
def func3 (numbers):
    numbers.reverse()
    for i in numbers:
        print (i,end = ',')

#return the inverse list 
def func4 (numbers):
    numbers.reverse()
    print (numbers)

#function that computes the average of a list of numbers given as a list.
def func5 (numbers):
    average = sum(numbers) / len(numbers)
    print ('This is the average:', average)


#function that takes a list of integers as input parameter and returns
#the number of times the most-frequently occurring element appears in the list.
def func6a(numb):
    maximum = 0
    for i in numb:
        if numb.count(i) > maximum:
            maximum = numb.count(i)
    print (maximum)
    return maximum


#function that orders a list of integers in ascending order.
def func7 (numbers):
    final =[]
    numbers.sort()
    for i in range (0,len(numbers)):
        final.append(numbers[(len(numbers)-1)-i])
    print (final)

#function that removes any duplicates from a list.

def func8 (numb):
    noduplicate= []
    for n in numb:
        if n in noduplicate:
            noduplicate = noduplicate
        else:
            noduplicate.append(n)
    print (noduplicate)


#function that finds the minimum or maximum element of a list of integers.
def func9 (numb):
    maximum= 0
    minimum= 0
    for i in numb:
        if i >= maximum:
            maximum = i
    minimum = maximum 
    for i in numb:
        if i <= minimum:
           minimum = i
    print ('the maximum number is :', maximum, 'and the minimum number is:', minimum)          


#function that opens a textfile and returns its 10th line as a string.

def func10 (text):
    te= open (text, mode ='r')
    listtext= te.readlines()
    
    print(listtext[9])

#function that reads a textile and prints any adjacent lines that are identical.

def func11 (text ):
    te= open (text, mode ='r')
    listtext= te.readlines()
    
    adjacent= []
    line1 = ''
    for line in listtext:
        if line == line1:
            adjacent.append(line)
        else:
            line1 = line

    print (adjacent)

#while loop to print numbers from 0 to 10.
def func12():
    i = 0 ;
    while( i <= 10 ):
        print (i, end= ',')
        i+= 1

#while loop to print numbers from 0 to 10.
def func13():
    i = 10 ;
    while( i >= 0 ):
        print (i, end= ',')
        i-= 1

        
func6a(['a','b','b','a','c', 'c'])

