#开发者：罗地观生
#开发时间：2021/5/5 13:12
import random
import string
class RandomChar:
    def __init__(self):
        self.all_uppercase=string.ascii_uppercase
        self.all_lowercase=string.ascii_lowercase
        self.all_digits=string.digits
        self.all_specials='~!@#$%^&*'
    def pick_random_item(self,sequence):
        random_int=random.randint(0,len(sequence)-1)
        return sequence[random_int]
    def uppercase(self):
        return self.pick_random_item(self.all_uppercase)
    def lowercase(self):
        return self.pick_random_item(self.all_lowercase)
    def digit(self):
        return self.pick_random_item(self.all_digits)
    def special(self):
        return self.pick_random_item(self.all_specials)
    def anyone(self):
        return self.pick_random_item(self.all_uppercase+self.all_lowercase+self.all_digits+self.all_specials)