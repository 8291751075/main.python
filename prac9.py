t = (1, 2, 3, 4, 5)
print("The values in tuple are:,t")
t=t+(7,)
print("Tuple after adding element :",t)
print("Tuple after slice : ", t[2:4])
print(" Multiplication :",(t*2))
print("The length of tuple is: ", len(t))
print("The maximum value of tuple is: ",max(t))
print("The maximum value of tuple is: ",min(t))
del t
print("Tuple deleted")
