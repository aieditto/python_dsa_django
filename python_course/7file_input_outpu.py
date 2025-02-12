"""
'r'     open for reading (default)
'w'     open for writing, truncating (remove data) the file first
'a'     open for writing, appneding to the end of the file if it exists
'x'     open for writing, creating a new file if it exists
'b'     binary mode
't'     text mode (default)
'+'     open a disk file for updating (reading and writing)

'r+'    read and write together. If no file exists than it will automatic
        create a new file and open it for reading and writing.
        Also it start removing from the begining of the file.
        
'w+'    read and write together. But it first remove all data than started.
'a+'    append me  

"""
#open a file with the directed name using function open("file name","mode")
#file=open("stude_data","r")
#read() function use for reading data from the file 
# data=file.read()
# print(data)
# print(len(data))
#close() use for closing the file
# file.close()



file=open("stude_data","a+")
file.write("Hello, how are you?\n I've completede my graduation")
data=file.read()
print(data)
file.close()
