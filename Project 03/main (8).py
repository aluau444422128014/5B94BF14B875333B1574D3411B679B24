def linear_search_product(product_list, target_product):
  indices = []
  for index, product in enumerate(product_list):
    if product == target_product:
      indices.append(index)
  return indices


Products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
target1 = "apple"
result = linear_search_product(Products, target)
print(result)
