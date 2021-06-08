from PIL import Image
import numpy as np
import cv2

I = Image.open('./layoutPF.png') 
image = cv2.imread('./layoutPF.png')
newsize = (810,1431)

image = cv2.resize(image,newsize,interpolation=cv2.INTER_AREA)
print(image.shape)
# I = I.convert('1')
# I.show()
# I.resize((810,1431))
# print(I.size)
I_array = np.array(image)
print (I_array.shape)
I_length = I_array.shape[0]
I_width  = I_array.shape[1]
# print (I_array[0][I_width-50] == [0, 0, 0])
# print(I_width)



# reset txt file
with open("layout_map.txt","a") as f:
    f.truncate(0)
print(I_length,I_width)
# write txt file
for i in range(I_length):
    for j in range(I_width):
        if (I_array[i][j] == [0, 0, 0]).all():
            x = 0.01*(i)
            y = 0.01*(j)
            data1 = str(round(x,2)) + ", " + str(round(y,2)) + ", " + "0"
            with open("layout_map.txt","a") as f:
                f.writelines(data1)
                f.writelines("\n")
    # print("OK")
