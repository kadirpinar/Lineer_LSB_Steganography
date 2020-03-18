import cv2
import numpy as np
import binascii
"""strr="a"
for i in range(0,1024):
    strr=strr+"a"
"""
strr=input()
bitstr=' '.join(format(ord(x), 'b') for x in strr)
print(bitstr)
bitstr=bitstr.replace(" ","")
print(bitstr)
print(len(bitstr))
lengt=str(len(bitstr))+"*"
print(lengt)
length=' '.join(format(ord(x), 'b') for x in lengt)
print(length)
length=length.replace(" ","")
print(length)
image = cv2.imread('IRONMANbmp.bmp',cv2.IMREAD_COLOR)
size=image.shape
print(size[0])
print(size[1])
y=0
yy=0


done = False



for i in range (0,size[0]):
    for j in range (0,size[1]):
        for k in range(0,3):
            if y==len(length):
                if yy==len(bitstr):
                    done=True
                    cv2.imwrite("lineerlsb.bmp",image)
                    break
                else:
                    x = "{0:b}".format(image[i, j][k])
                    x = x[:-1]
                    x = x+""+bitstr[yy]
                    x = int(x, 2)
                    image[i, j][k] = x
                    yy = yy + 1

            else:
                x = "{0:b}".format(image[i, j][k])
                x = x[:-1]
                x=x+""+length[y]
                x = int(x, 2)
                image[i, j][k] = x
                y=y+1
        if done==True:
            break
    if done == True:
        break
output=[]
list1=[]
list2=[]
done = False
header=0
dee=0
for i in range(0,size[0]):
    for j in range(0,size[1]):
        for k in range(0,3):
            header=header+1
            x = "{0:b}".format(image[i, j][k])
            x=x[len(x)-1]
            output.append(x)
            str1 = ''.join(output[-6:])
            if str1=="101010":
                done = True
                print(output)
                str2 = ''.join(output[:-6])
                list = [x for x in str2]
                print(list)
                list.insert(6,',')
                for de in range(0,len(list)):
                    if dee==len(list)-1:
                        break
                    str3= ''.join(output[dee:dee+6])
                    list1.append(str3)
                    dee=dee+6

                for z in range(0,len(list1)):
                    n = int(list1[z], 2)
                    try:
                        n=binascii.unhexlify('%x' % n)
                        n=int(n)
                        n=str(n)
                    except:
                        n = binascii.unhexlify('0%x' % n)
                        n = int(n)
                        n = str(n)
                    list2.append(n)
                ch="".join(list2)
                ch=int(ch)
                ch=ch+header
                print(ch)
                break

        if done == True:
            break
    if done == True:
        break
counter=0
output1=[]
done = False

for i in range(0,size[0]):
    for j in range(0,size[1]):
        for k in range(0,3):
            counter=counter+1
            if(counter>header):
                if(counter>ch):
                    done = True
                    break
                else:
                    x = "{0:b}".format(image[i, j][k])
                    x = x[len(x) - 1]
                    output1.append(x)
        if done == True:
            break
    if done == True:
        break
print("KAdirr")
print(output1)
output2=[]
x=0


for i in range(0,len(output1)):
    print(x)

    if x == len(output1) - 1:
        break
    try:
        str6 = ''.join(output1[x:x + 7])
        print(str6)
        if "100000" in str6:
            output2.append(" ")
            x=x+6
        else:
            n = int(str6, 2)
            n = binascii.unhexlify('%x' % n)
            output2.append(n.decode('utf-8'))
            x = x + 7

    except ValueError:
        print()
        break

    except:
        str6 = ''.join(output1[x:x + 7])
        print(str6)
        if "100000" in str6 :
            output2.append(" ")
            x=x+6
        else:
            n = int(str6, 2)
            n = binascii.unhexlify('0%x' % n)
            output2.append(n.decode('utf-8'))

print(output2)
out=''.join(output2)
print(out)
image = cv2.imread('IRONMANbmp.bmp')
cv2.imshow("before",image)
lineer= cv2.imread('lineerlsb.bmp')
cv2.imshow("after",lineer)
cv2.waitKey()
