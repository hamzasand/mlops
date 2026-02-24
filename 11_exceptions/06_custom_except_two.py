# class OutOfIngredientsError(Exception):
#     pass

# def make_chai(milk, sugar):
#     if milk == 0 or sugar == 0:
#         raise OutOfIngredientsError("Missing milk or sugar")
#     print("chai is ready...")


# make_chai(0, 1)


class Outofingredienterror(Exception):
    pass

def make_chai(milke ,ugar):
    if milke ==0 or ugar == 0:
        raise Outofingredienterror("missing milke or sugar")
    print("chai is ready")

make_chai(0,1)
