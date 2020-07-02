l_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=0;allnumber=0
with open("hw5.txt","a") as f:
    f.writelines("abc\ndef\nOPQ\nOPQ\n\ndahugde\nHAGGFYU\nhjgyd")
with open("hw5.txt","r") as f:
    lines=f.readlines()
    for i in range(len(lines)-1):
        allnumber+=len(lines[i])
    for i in range(25):
        number=0
        for j in range(len(lines)-1):
            line=lines[j];line=line.upper()
            number+=line.count(l_list[i])
        if i%5==0 and i>=5:
            print("\n",end="")
        if (number/allnumber)<0.01:
            print(l_list[i],end="")
            print("<1.0%",end="  ")
        elif (number/allnumber)>=0.1:
            print(l_list[i],end=" ")
            print(round(number/allnumber*100,1),end="")
            print("%",end=" ")
        elif (number/allnumber)<0.1 and (number/allnumber)>=0.01:
            print(l_list[i],end=" ")
            print(round(number/allnumber*100,1),end="")
            print("%",end="  ")