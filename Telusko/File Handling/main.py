

# # if u want to read file then it should be opened in read mode before u read the file
# # if u want to write something in file then file should be opened in write mode 
# # if u want to append some data to existing file then file should be opened to append mode
# # otherwise it will throw an error
# # in write mode if file does not exist then python will create file automatically

# # Modes
# # r = read
# # w = write
# # a = append


# file = open('data.txt','w')
# # this is used to print data line by line
# # print(file.readline(),end="")
# # # this is used to print all the data from the file
# # print(file.read())


# file.write("I am Abhishek.\nWorking as python developer in TCS,Mumbai\n")

# file = open('data.txt','r')

# for i in file:
#     print(i,end="")

mypic = open('pp.jfif','rb')


newpic = open("Newpic.jfif","wb")

for i in mypic:
    newpic.write(i)