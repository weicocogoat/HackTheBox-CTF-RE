'''
Count starting from 0

1 cell is made of 16 bytes
8th element shows the x_pos
4th element shows the y_pos
0th element shows the z_pos

12th element dictates whethere the space is valid or not
0x2 means that the space is invalid
0x0 or 0x1 means that the space is possibly valid
'''
# open the sample file used 
file = open('cleaned.txt') 

# read the content of the file opened 
content = file.readlines()

f = open("path.txt", "a")
for i in range(8000):
    if content[i][48:50] == "01" or content[i][48:50] == "03":
        print(content[i])
        f.write(content[i])



#print(content[1][48:50])

