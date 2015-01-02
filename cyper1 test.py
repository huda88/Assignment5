
# Ceasar cipher
def cipher1():
    var ='abcdefghijklmnopqrstuvwxyz'
           
    n= int(input('number of shift:')) #input data
    mess= input(('Write a message for your friend:'))
    message= ''
    for i in mess:
        var=0
        if i.isupper():
            var=1
            i.lower()
        if i in var(len):
            x =int(var.index(i))
            x = x + n                 
            if x > len(var):                  
                x -= len(var) 
                message+= var[x]
            elif x < 0:
                x += len(var)
                message += var[x]       
            else:
                message += var[x]
        else:
            message+= i
        if var==1:
            x.upper()
    return message

def decipher1():
    al ='abcdefghijklmnopqrstuvwxyz'
    var2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n= int(input('number of shift:'))
    mess= input(('Write a message for your friend:'))
    mess= mess.lower()
    message= ''
    for i in mess:
        if i in al:
            x =int(al.index(i)) 
            x = x - n                #only change the shift in the reverse way
            if x > 26:
                x -= 26
                message += al[x]
            elif x < 0:
                x += 26
                message += al[x]
            else:
                message += al[x]
        elif i in var2:
            x =int(var2.index(i))
            x = x -n
            n                 
            if x > len(var2):                  
                x -= len(var2) 
                message+= var2[x]
            elif x < 0:
                x += len(var2)
                message += var2[x]
            else:
                message += var2[x]
        else:
            message+= " "
    return message

## take a 
def cipher2():
    n= int(input('number of line:'))
    s= input(('Write a message for your friend:'))
    message=''
    if len(s)%n == 0:
        return
    else:
        div= int(len(s)//n)+1
        b= (div*n - (len(s)))*' '
        s= s+b
    for i in range (0, len(s), n):
        print (s[i:i+n])
    for i in range(n):
        a=0+i
        for i in range(a,len(s),n):
            message += s[i]
    print ('The encrypte message is:',message)
    return message 

def decipher2():
    n= int(input('number of line:'))
    s= input(('Write a message for your friend:'))
    message=''
    div= int(len(s)//n)
    for i in range (div):
        a=0+i
        for i in range(a,len(s), div):
            message += s[i]
    print('The decrypt message is:',message)
    return message


def cipher3(message, key):
    big=(key-1)*2   #number of position to do "the piramide"
    for i in range(key*2):
        if ((len(message)-key)%big)!=0:  # add space if we need to string become divisible by the key
            message+=' '
    
    s=0
    start=key-1  #-1 because it starts at 0
    extra=0
    crypted=''
    x=int((len(message)+key-2)//((2*key)-2)) # range to found the letter (different if we are in the middle or it the bottom or top)
    
    for c in range(key):
        count=0
        if big==0 or s==0:  #if we're doing the first or last line
            line=x
        else:                   #middle lines
            line=(2*x)-1
        for i in range(len(message)):
            if i<line:
                if big==0 or s==0: # if we are in the bottom or in the top of the piramide
                    count+=big
                    crypted+=message[start+extra]
                    extra+=((key-1)*2)
                else:
                    if i%2==0: # if the range of the letter is in even range 
                        if i==0: # if 0 
                            count=count
                            crypted+=message[start+count]
                        else:
                            count+=big # in the other even 
                            crypted+=message[start+count]
                    else:  # if odd range
                        count+=s 
                        crypted+=message[start+count]
        extra=0         # be right the value before the next loop
        start-=1
        big-=2
        s+=2
    print(crypted)
    return crypted


def decipher3(message, key):
    lenght=(key-1)*2
    final=''
    x=int((len(message)+key-2)/((2*key)-2))
    start= len(message)-x
    counter=0
    for i in range(len(message)+1//lenght): # do to the line divide by the lenght of the piramide
        minus=0
        if counter<len(message):  # DO ONLY IF THE CONTER IS LOWEST THAN THE LENGHT OF STR
            final+= message[start+(counter//lenght)]
            counter+=1
            minus+=1
            for i in range(key-2):
                if counter<len(message):
                    final+= message[start+((counter-minus)//(key-1)) -(i+1)*(2*x-1)]
                    counter+=1
                    minus+=1
            final+= message[start+((counter-minus)//lenght) -(x+(key-2)*(2*x-1))]
            counter+=1
            minus+=1
            for i in range((key-3),-1,-1):
                if counter<len(message):        
                    final+= message[start+1+((counter-minus)//(key-1)) -((i+1)*(2*x-1))]
                counter+=1
                minus+=1
    print(final)
    return final
    

cipher1()
