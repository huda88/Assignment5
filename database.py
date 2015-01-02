
##################################################A read from a file text

def read (text):
    finallist= []
    te= open (text).read().split('\n')

    for row in te:
        middlelist=''
        middlelist = str(row)
        delimiter= ','
        a = middlelist.split(delimiter)
        finallist.append(a)
    return finallist

##################################################B Formatted printing

def show (text):
    header = ['Name' , 'Gender', 'Year of birth ']
    finallist= [header] + read(text)
    
    # found the widhts of each column
    col_width = max(len(word) for row in finallist for word in row) + 2  # padding
    for row in finallist:
        print ("".join(word.ljust(col_width) for word in row))

#show('data.txt')


#################################################C Add    

# check the name
def name ():
    while True:
        name= input('Enter the name:')
        if name[0].isupper()== True:
            return name
        else:
             print ('Error, Try Again')
    return name
# check the name
def gender ():
    while True:
        g = ['Male', 'Female']
        gender= input('Enter the gender Male or Female:')
        if gender in g:
            return gender
        else:
             print ('Error, Try Again')
    return gender

# check date
def date ():
    while True:
        date= input('Enter the Year of birth:')
        if int(date):
            if len(date) == 4:
                return date
            else:
                print ('Error, Try Again, you have to write a date in 4 number')
        else:
             print ('Error, Try Again, you have to write a date in 4 number')
    return date

#####################add function


def add(text):
    finallist= read(text)
    new=[str(name()), str(gender()), str(date())]
    finallist.append(new)
    print (finallist)
    return finallist

    
    
####################################### D delet

 # Copy in the file
def past(function, text):
    new=function(text)
    final= []
    delimiter= ','
    #transform in alist contain string
    for x in new:
        a = delimiter.join(x)+ '\n'
        final.append(a)
    b= ''.join(final)
    #print(final)
    #print(b)
    file = open (text, 'w')
    file.write(b)
    file.close()
    show(text)
    
#command delet 
def delet(text):
    finallist= read(text)
    #print(finallist)
    while True:
        na = name()
        for x in finallist:
            if na in x:
                finallist.remove(x)
                return finallist
        print (finallist)
    else:
        print ('Error. Try Again')
    return finallist


####################################### E Modify
# check the name
def moname ():
    print ('Write a new name')
    name()
    return name
# check the name
def mogender ():
    print ('Write a new gender, empty for no change')
    gender()
    return gender
# check date
def modate ():
    print('Write new Year of birth, empty for no change:')
    date()
    return date

#################################### Modify##############################

def modify (text):
    nametochange= name()
    new=[ moname(), mogender(), modate()]      
    finallist= read(text)
    #print(finallist)
    for x in finallist:
        if nametochange in x:   
            for i in range(len(new)):
                if new[i]== '':
                    x[i]
                else:
                    x[i]=new[i]
            return finallist
    return finallist
               

############################database ################################

def database ():
    finallist=[]
    text= input('Chose you database file:')
    while True:
        x = input ('Chose your function s= show, a= add, m= modify, d= delete, e= end:')
        if x == 'd':
            past(delet,text) 
        elif x == 'a':
            past(add,text)
        elif x == 's':
            show(text)
        elif x == 'm':
            past(modify,text)
        elif x == 'e':
            print('Bye, see you an other time')
            return
        else:
            print('Error, Try Again')

database()

            
         
        
