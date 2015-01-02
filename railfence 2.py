def cipher3(message, key):
    big=(key-1)*2
    for i in range(key*2):
        if ((len(message)-key)%big)!=0:
            message=message+' '
    
    small=0
    start=key-1  #fourth position, -1 because it starts at 0
    extra=0
    crypted=''
    x=int((len(message)+key-2)/((2*key)-2))
    
    for c in range(key):
        count=0
        if big==0 or small==0:  #if we're doing the first or last line
            line=x
        else:                   #middle lines
            line=(2*x)-1
        for i in range(len(message)):
            if i<line:
                if big==0 or small==0:
                    count+=big
                    crypted+=message[start+extra]
                    extra+=((key-1)*2)
                else:
                    if i%2==0:
                        if i==0:
                            count=count
                            crypted+=message[start+count]
                        else:
                            count+=big
                            crypted+=message[start+count]
                    else:
                        count+=(small)
                        crypted+=message[start+count]
        count=0
        extra=0
        start-=1
        big-=2
        small+=2
    print(crypted)
    return crypted


def decipher3(message, key):
    lenght=(key-1)*2
    final=''
    x=int((len(message)+key-2)/((2*key)-2))
    start= len(message)-x
    counter=0
    minus=0
    for i in range(len(message)+1//lenght):
        if counter<len(message):
            final+= message[start+(counter//lenght)]
        counter+=1
        minus+=1
        for i in range(key-2):
            if counter<len(message):
                final+= message[start+((counter-minus)//(key-1)) -(i+1)*(2*x-1)]
            counter+=1
            minus+=1
        if counter<len(message):        
            final+= message[start+((counter-minus)//lenght) -(x+(key-2)*(2*x-1))]
        counter+=1
        minus+=1
        for i in range((key-3),-1,-1):
            if counter<len(message):        
                final+= message[start+1+((counter-minus)//(key-1)) -((i+1)*(2*x-1))]
            counter+=1
            minus+=1
        minus=0
    print(final)
    return final
    



s='Send more reinforcements for the monkey-catching operation'
cipher3(s,4)
   
k='d onrm-ienn erfreto  oychnproemrencmsfteneacgoaiSoie hkt t'
decipher3(k,4)
