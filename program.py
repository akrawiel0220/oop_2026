class Zloty(float):
    def zmien_wage_na_euro(self):
        return self / 4.21

    def __add__(self, other): #to jest add dla zlotego
        # super().__add__()  # dwoanie sie  do nadklasy
        return Zloty(super().__add__(other)) #super zwroci mi metode z klasy nadrzd
#chcemy zeby zeby zloty mial metode add jako typ zloty a nie float dlatego tak piszemy

a = Zloty(4)
b = Zloty(7)
print(a + b)
c = a + b
print(a.zmien_wage_na_euro())
print(c.zmien_wage_na_euro())
