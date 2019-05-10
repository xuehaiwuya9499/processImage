from PIL import Image
import numpy as np
count=39
column=7
edgex,edgey=50,50
gapx,gapy=31,31
x0,x1,y0,y1=250,880,80,620
blackPhoto=np.full((((count+column-1)//column)*(y1-y0+gapy)-gapy+edgey*2, \
                    gapx*(column-1)+(x1-x0)*column+edgex*2, 3),0)
for i in range(count):
    catchp=np.array(Image.open('./456/'+str(i+1)+'.jpg'))
    x2=edgex+i%column*(x1-x0+gapx)
    y2=edgey+i//column*(y1-y0+gapy)
    blackPhoto[y2:y2+y1-y0,x2:x2+x1-x0]=catchp
im=Image.fromarray(blackPhoto.astype('uint8'))
im.save('blackPhoto123.jpg','jpeg')
