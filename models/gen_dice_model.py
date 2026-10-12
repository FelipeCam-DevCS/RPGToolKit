import random

class gen_dice_model():
    def __init__(self):
        self.dices_generated = []

    #Retorna uma lista com o resultado e os parametros utilizados
    def generate_dice(self, sides, amount, modfier):
        if isinstance(amount, int) and isinstance(sides, int) and (isinstance(modfier, float) or isinstance(modfier, int)):
            dice_amount = 0
            for i in range(amount):
                dice_value = random.randint(0,sides)
                dice_mod = dice_value + modfier
                dice_amount += dice_mod
            return [dice_amount, amount, sides, modfier]
        else:
            raise ValueError

    #Gera e salva os dados aleatorios e seus parametros a uma lista (self.dices_generated)
    def generate_dice_save_historical(self,sides,amount,modfier):
        self.dices_generated.append(self.generate_dice(sides, amount, modfier))

    def clear_dice_historical(self):
        self.dices_generated.clear

    

gdm = gen_dice_model()
a = 0
while True:
    gdm.generate_dice_save_historical(2,3,5)
    a +=1
    if a == 80:
        break
for i in gdm.dices_generated:
    print(i)