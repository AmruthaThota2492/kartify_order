# method 1
#myfile=open('myfile.txt') 
#print(myfile.readlines())
#print("next print file************8")
#myfile.close()


#method2:  # here no noeed to use close() to close file
with open('myfile.txt') as myfile:
    print(myfile.readlines())

# write fie

with open("newfile.txt","w") as newfile:
    newfile.write("this is my first line")

with open('newfile.txt','a') as newfile:
    newfile.write("\nthis appended line")