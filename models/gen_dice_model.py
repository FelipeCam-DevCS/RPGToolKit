import random

class gen_dice_model():
    def __init__(self):
        self._dices_generated = []

    #Retorna uma lista com o resultado e os parametros utilizados
    def generate_dice(self, sides, amount, modfier):
        dice_amount = 0
        if sides >= 2 or amount <= 1:
                for i in range(amount):
                    dice_value = random.randint(0,sides)
                    dice_mod = dice_value + modfier
                    dice_amount += dice_mod
                return [dice_amount, amount, sides, modfier]
        else:
            raise ValueError
            

    #Gera e salva os dados aleatorios e seus parametros a uma lista (self.dices_generated)
    def generate_dice_save_historical(self,sides,amount,modfier):
        self._dices_generated.append(self.generate_dice(sides, amount, modfier))

    def clear_dice_historical(self):
        self._dices_generated.clear()

    @property
    def get_dices_generated(self):
        return self._dices_generated
    

