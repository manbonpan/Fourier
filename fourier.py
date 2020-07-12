'''
import requests
from PIL import Image
import numpy as np
import io
from sklearn.cluster import mean_shift

# get the image
url = 'https://i.stack.imgur.com/qKAk5.png'
res = requests.get(url)
# set the content as a file pointer object
fp = io.BytesIO(res.content)
# load the image to PIL
img = Image.open(fp)

# convert the image to gray-scale and load it to a numpy array
# need to transpose because the X and Y are swapped in PIL
# need [:,::-1] because pngs are indexed from the upper left
arr = np.array(img.convert('L')).T[:,::-1]
# get indices where there line is the pixel values is dark, ie <100
indices = np.argwhere(arr < 100)
for x in np.arange(.5,5.6,.25):
    print('{:.2f}: '.format(x), end='')
    print(len(mean_shift(indices, bandwidth=x)[0]))'''

import random
import math
import turtle
turtle=turtle.Turtle()
import matplotlib.pyplot as plt

xp=[]
yp=[100,100,100,-100,-100,-100,100,100,100,-100,-100,-100,100,100,100,-100,-100,-100,100,100,100,-100,-100,-100]
for t in yp:
    xp.append(0)
    

'''p=[]
for i in range(0,100):
    p.append(random.randint(1,100))'''
turtle.speed(0)
xa=len(xp)
counter=0


compp=[]
comppy=[]
for k in range(0,len(xp)):
    r=0
    i=0
   
    for n in range(0,len(xp)):
        
        counter=counter+1
        phi = (2*math.pi * k * n) /xa
        r=r+(xp[n]*(math.cos(phi)))
        i=i-(yp[n]*(math.sin(phi)))

    r=r/xa
    i=i/xa

    compp.append([k,abs(math.sqrt(((r**2)+(i**2)))),abs(math.atan2(i,r)),r,i])

compp.reverse()
radius=12

tim=0
#for i in compp:
       #print(i[3],i[4])
pi=(2*math.pi)/1000
#turtle.circle(radius)
j=[]
f=0
k=0
x=0
y=0
test=0
while True:
    
    for i in range(len(compp)):
         k=k+1
         radius=compp[i][1]
         tim=(2*math.pi)/len(compp)
         x+=(radius*(math.cos((compp[i][0]*tim)+compp[i][2]+math.pi/2)))
         y+=(radius*(math.sin((compp[i][0]*tim)+compp[i][2]+(math.pi/2))))
         print(abs(x),abs(y))
         
    #turtle.goto(x,0)
    gg=str(y)[0:5]
    turtle.goto(0,float(gg))
    k=k+0.2
    #plt.plot([x],[y])
    #plt.ylabel('some numbers')

    #turtle.goto(x,y)
    #f=f+1
    #if f== len(compp)-1:
      #  f=0
#plt.show()     
'''for i in range(100):
    for j in range(len(compp)):
         radius=compp[j][1]
         tim=((2*math.pi)/len(compp))+tim
         x+=(radius*(math.cos((compp[j][0]*tim)+compp[j][2])))
         y+=(radius*(math.sin((compp[j][0]*tim)+compp[j][2])))
    print(x,abs(y))
    k=k+1
    
    turtle.goto(x,y)
    f=f+1'''
    


