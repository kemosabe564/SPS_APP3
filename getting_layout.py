from PIL import Image
import numpy as np


I = Image.open('./layout_test.png') 
I.show()    
I_array = np.array(I)
print (I_array.shape)
I_length = I_array.shape[0]
I_width  = I_array.shape[1]
# print (I_array[0][I_width-50] == [0, 0, 0])
# print(I_width)

# reset txt file
with open("layout_map.txt","a") as f:
    f.truncate(0)

# write txt file
for i in range(I_length):
    for j in range(I_width):
        if (I_array[i][j] == [0, 0, 0]).all():
            x = round(0.01*(i),2)
            y = round(0.01*(j),2)
            data1 = str(x) + ", " + str(y) + ", " + "0"
            with open("layout_map.txt","a") as f:
                f.writelines(data1)
                if not(i == I_length-1 and j == I_width-1):
                    f.writelines("\n")
                
    print("OK")
