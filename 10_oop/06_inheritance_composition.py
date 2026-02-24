class Basechai:
    def __init__(self,type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing {self.type_} chai...")



class Masalachai(Basechai):
    def add_spices(self):
        print("Adding cardomom , Ginger, Cloves")

class Chaishop:
    chai_cls = Basechai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"serving {self.chai.type_} cahi in the shop")
        self.chai.prepare()

class Fancychaishop(Chaishop):
    chai_cls = Masalachai


shop = Chaishop()
fancy = Fancychaishop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()