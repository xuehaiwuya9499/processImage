from PIL import Image
import numpy as np
count=39
x0,x1,y0,y1=250,880,80,620
for i in range(count):
    a=np.array(Image.open('./123/'+str(i+1)+'.jpg'))
    b=a[y0:y1,x0:x1]
    im=Image.fromarray(b.astype('uint8'))
    im.save('./456/'+str(i+1)+'.jpg','jpeg')
    print(i+1)
