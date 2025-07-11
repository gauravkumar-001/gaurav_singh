def create(num_product):
    inventary={}
    for i in range(1,num_product+1):
        id1=int(input(f"enter the product id {i} =>"))
        name=input(f"enter the name for id {id1} =>")         # product details     
        inventary[id1]=name
    return inventary

num_product=int(input("enter the number of product"))
dictionary=create(num_product)
print(dictionary)