list1=["Tv","Laptop","Mouse","Keyboard","Printer"]
print("Intial Inventory Products")
for i in range(0,len(list1)):
    print(list1[i])
###To add new product
urgent_product=input("Enter the product to be added")
list1.append(urgent_product)
##add new products
new_product=["Tablet","Webcam","Laptop"]
list1.extend(new_product)
##Remove products
list1.remove("Mouse")
list1.remove("Webcam")
print(list1)

print("product position Monitor")
#print(list1.index("Monitor"))

print(sorted(list1))
list1.reverse()
print(list1)
