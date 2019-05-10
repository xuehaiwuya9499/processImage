import imageio
 
def create_gif(image_list, gif_name):
 
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif 
    imageio.mimsave(gif_name, frames, 'GIF', duration = 0.25)
 
    return
 
def main():
    image_list = []
    for i in range(39):
        image_list.append(str(i+1)+'.jpg')
    gif_name = 'created_gif.gif'
    create_gif(image_list, gif_name)
 
if __name__ == "__main__":
    main()
##来源：CSDN 
##原文：https://blog.csdn.net/guduruyu/article/details/77540445
