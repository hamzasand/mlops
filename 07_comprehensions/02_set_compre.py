# favourite_chais = [
#     "Masala Chai", "Green Tea", "Masala Chai",
#     "Lemon Tea", "Green Tea", "Elaichi Chai"
# ]

# unique_chai = {chai for chai in favourite_chais }
# print(unique_chai)


# recipes = {
#     "Masala Chai": ["ginger", "cardamom", "clove"],
#     "Elaichi Chai": ["cardamom", "milk"],
#     "Spicy Chai": ["ginger", "black pepper", "clove"],
# }

# unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

# print(unique_spices)

# favourite_chais = [
#      "Masala Chai", "Green Tea", "Masala Chai",
#      "Lemon Tea", "Green Tea", "Elaichi Chai"
#  ]

# unique_chai = {my_chai for my_chai in favourite_chais}
# print(unique_chai)

recipes = {
     "Masala Chai": ["ginger", "cardamom", "clove"],
     "Elaichi Chai": ["cardamom", "milk"],
     "Spicy Chai": ["ginger", "black pepper", "clove"],
 }

unique_spice = {spice for ingridents in recipes.values() for spice in ingridents}

print(unique_spice)