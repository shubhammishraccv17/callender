import random
actual_array=list()
user_array=list()
for x in range(5):
    y =random.randint(0,99)
    actual_array.append(y)
print(actual_array)
print("input your 5 guess")
for m in range(5):
    n=int(input(""))
    user_array.append(n)
print (user_array)
result_array=[]
for p in range(5):
    result=user_array[p]-actual_array[p]
    result_array.append(abs(result))
accuracy=sum(result_array)   
accuracy=(500-accuracy)
accuracyper=accuracy/500
accuracyper=(accuracyper)*100
print ("your accuracy rate is")
print (accuracyper)

    
    

