import random

class gen_dice_model():
    def __init__(self):
        self._dices_generated_last_to_first = []
        self._dices_generated_small_to_largest = []
        self._dices_generated_largest_to_small = []
        self._dices_generated_first_to_last = []



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
            

    def save_dice_sorted(self, dice_reg):
        self._dices_generated_last_to_first.append(dice_reg)
        self._dices_generated_first_to_last = self._dices_generated_last_to_first[::-1]
        i = 0
        j = 0
        '''
        Parte a baixo faz a ordenação por resultado o maior como primeiro e menor como ultimo
        '''
        copy_last_to_first_dice = self._dices_generated_last_to_first.copy()

        '''
        Bubble sort simples para ordenação depois procurar como otimizar
        '''

        if len(copy_last_to_first_dice) > 1:
            for i in range(len(copy_last_to_first_dice)):
                i = 0
                for j in range(len(copy_last_to_first_dice)):
                    if copy_last_to_first_dice[i][0] > copy_last_to_first_dice[i+1][0]:
                        copy_last_to_first_dice[i][0], copy_last_to_first_dice[i+1][0] = copy_last_to_first_dice[i+1][0] , copy_last_to_first_dice[i][0]
                i+=1
                if i == len(copy_last_to_first_dice)-1:
                    break
            #Reatribui todos os valores substituido pela ordenação depois ver se tem como otimizar solução provisoria
            self._dices_generated_largest_to_small[:] = copy_last_to_first_dice
        else:
            self._dices_generated_largest_to_small[:] = self._dices_generated_last_to_first


        self._dices_generated_small_to_largest = self._dices_generated_largest_to_small[::-1]

        




    #Gera e salva os dados aleatorios e seus parametros a uma lista (self.dices_generated)
    def generate_dice_save_historical(self,sides,amount,modfier):
        self.save_dice_sorted(dice_reg=self.generate_dice(sides, amount, modfier))
        

    def clear_dice_historical(self):
        self._dices_generated.clear()

    @property
    def get_dices_generated(self):
        return self._dices_generated
    

