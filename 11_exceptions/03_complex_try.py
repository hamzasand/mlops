# def serve_chai(flavor):
#     try:
#         print(f"Preparing {flavor} chai...")
#         if flavor == "unknown":
#             raise ValueError("We don't know that flavor")
#     except ValueError as e:
#         print("Error: ", e)
#     else:
#         print(f"{flavor} chai is served")
#     finally:
#         print("Next customer please")

# serve_chai("masala")
# serve_chai("unknown")

def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("we dont know the flavor")
    except ValueError as e:
        print("Error", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("next customer please")

serve_chai("masala")
serve_chai("unknown")
