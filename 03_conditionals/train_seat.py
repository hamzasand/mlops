# seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()


# match seat_type:
#     case "sleeper":
#         print("Sleeper - No AC, beds available")
#     case "ac":
#         print("AC - Air conditioned, comfy ride")
#     case "general":
#         print("General - Cheapest option, no reservation")
#     case "luxury":
#         print("Luxury - Premium seats with meals")
#     case _:
#         print("Invalid seat type")

seat_type = input("select a set type (sleeper/ac/genral/luxury)").lower()
match seat_type:
    case "sleeper":
        print("u can enjoy beds")
    case "ac":
        print("u can enjoy ac")
    case "ganral":
        print("no need booking")
    case "luxury":
        print("u can enjoy meal")
    case _:
        print("type is not available")