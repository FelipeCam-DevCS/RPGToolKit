import random

class gen_dice_model():
    def __init__(self):
        self._dices_generated_last_to_first = []
        self._dices_generated_first_to_last = []
        self._dices_generated_largest_to_small = []
        self._dices_generated_small_to_largest = []



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
            for i in range(len(copy_last_to_first_dice)-1):
                for j in range(len(copy_last_to_first_dice)-1-i):
                    if copy_last_to_first_dice[j][0] < copy_last_to_first_dice[j+1][0]:
                        copy_last_to_first_dice[j], copy_last_to_first_dice[j+1] = copy_last_to_first_dice[j+1] , copy_last_to_first_dice[j]

            #Reatribui todos os valores substituido pela ordenação depois ver se tem como otimizar solução provisoria
            self._dices_generated_largest_to_small[:] = copy_last_to_first_dice
        else:
            self._dices_generated_largest_to_small[:] = self._dices_generated_last_to_first


        self._dices_generated_small_to_largest = self._dices_generated_largest_to_small[::-1]

        




    #Gera e salva os dados aleatorios e seus parametros a uma lista (self.dices_generated)
    def generate_dice_save_historical(self,sides,amount,modfier):
        self.save_dice_sorted(dice_reg=self.generate_dice(sides, amount, modfier))
        

    def clear_dice_historical(self):
        #Limpa os registros do historioco
        self._dices_generated_last_to_first[:] = []
        self._dices_generated_first_to_last[:] = []
        self._dices_generated_largest_to_small[:] = []
        self._dices_generated_small_to_largest[:] = []

    @property
    def get_dices_first_to_last(self):
        return self._dices_generated_first_to_last
    
    @property
    def get_dice_last_to_first(self):
        return self._dices_generated_last_to_first

    @property
    def get_dice_largest_to_small(self):
        return self._dices_generated_largest_to_small
    
    @property
    def get_dice_small_to_largest(self):
        return self._dices_generated_small_to_largest