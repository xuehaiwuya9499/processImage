from PIL import ImageGrab
count=1
while True:
    txt=input()
    if txt!='q' and txt!='Q':
        im=ImageGrab.grab()
        im.save(str(count)+'.jpg','jpeg')
    else:
        break
    count+=1
    print(count)
