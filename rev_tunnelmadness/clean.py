# open the sample file used 
file = open('Maze.txt') 

# read the content of the file opened 
content = file.readlines() 

res = ''
arr = []
arr_2d = []
temp_arr = []
a = 0

for j in range(128000):
    for i in range(len(content[j])):
        # Extract relevant data from file
        if 8 < i < 11:
            res += content[j][i]
        '''
        if i > 39:
            res += content[j][i]
        '''
    arr.append(res.replace(" ","").replace("\n", ""))

    # Store data in a 2d array, with each subarray detailing the content of the 16 byte cell
    if a < 16:
        temp_arr.append(res.replace(" ","").replace("\n", ""))
        a = a + 1
    else:
        arr_2d.append(temp_arr)
        a = 1
        temp_arr = []
        temp_arr.append(res.replace(" ","").replace("\n", ""))

    res = ''


#print(arr_2d[0:3])

'''
# Write cleaned contents to a file
f = open("cleaned.txt", "a")
for i in range(len(arr_2d)):
    for j in range(len(arr_2d[i])):
        f.write(arr_2d[i][j])
        f.write(", ")
    f.write("\n")
f.close()
'''

for i in range(len(arr_2d)):
    if "03" in arr_2d[i]:
        print(arr_2d[i])
        print(i)
    '''
    if (arr_2d[i][13]) == "03":
        print(arr_2d[i])
        print(i)
    '''