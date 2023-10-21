def linear_search_product(product_list, target_product):
    indices = []
    
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    
    return indices


products = ["Apple", "Banana", "Apple", "Orange", "Grapes", "Apple"]
target = "Apple"
result = linear_search_product(products, target)

if result:
    print(f"The product '{target}' is found at indices: {result}")
else:
    print(f"The product '{target}' is not found in the list.")

