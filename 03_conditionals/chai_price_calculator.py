# cup = input("Choose your cup size (small/medium/large): ").lower()

# if cup == "small":
#     print("Price is 10 rupees")
# elif cup == "medium":
#     print("Price is 15 rupees")
# elif cup == "large":
#     print("price is 20 rupees")
# else:
#     print("Unknown cup size")


cup_size = input("please chose your cup size as(small/medium/large)").lower()

if cup_size == "small":
    print(f"your bill is for {cup_size} 10")
elif cup_size == "medium":
    print(f"your bill is for {cup_size} 15")
elif cup_size == "large":
    print(f"your bill is for {cup_size} 20")
else:
    ("we dont have this cup size")