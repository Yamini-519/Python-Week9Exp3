import random
file=open("rannum","w+")
print("random 20 numbers from 1 to 100:")
for i in range(20):
    num=random.randint(1,100)
    file.write(str(num)+"  ")
file=open("rannum","r")
list=[file.read()]
print(list)
file.close()