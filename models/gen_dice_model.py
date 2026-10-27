import random

class gen_dice_model():
    def __init__(self):
        self._dices_generated_last_to_first = []
        self._dices_generated_first_to_last = []
        self._dices_generated_largest_to_small = []
        self._dices_generated_small_to_largest = []

    def set_obj_historical_IO(self, obj_historical_IO):      
        self.obj_historical_IO = obj_historical_IO

    #Retorna uma lista com o resultado e os parametros utilizados
    def generate_dice(self, sides, amount, modfier):
        dice_amount = 0
        if sides >= 2 or amount <= 1:
                for i in range(amount):
                    dice_value = random.randint(0,sides)
                    dice_mod = dice_value + modfier
                    dice_amount += dice_mod
                return [dice_amount, sides, amount, modfier]
        else:
            raise ValueError
            

    def save_sort_dices(self, dices_generated_last_to_first):
        copy_last_to_first_dice = dices_generated_last_to_first.copy()
        self._dices_generated_last_to_first[:] = dices_generated_last_to_first.copy()
        self._dices_generated_first_to_last[:] = dices_generated_last_to_first[::1]

        i = 0
        j = 0
        self._dices_generated_first_to_last = dices_generated_last_to_first[::-1]
        if len(copy_last_to_first_dice) > 1:
            for i in range(len(copy_last_to_first_dice)-1):
                for j in range(len(copy_last_to_first_dice)-1-i):
                    if copy_last_to_first_dice[j][0] < copy_last_to_first_dice[j+1][0]:
                        copy_last_to_first_dice[j], copy_last_to_first_dice[j+1] = copy_last_to_first_dice[j+1] , copy_last_to_first_dice[j]
            #Reatribui todos os valores substituido pela ordenação depois ver se tem como otimizar solução provisoria
            self._dices_generated_largest_to_small[:] = copy_last_to_first_dice

        self._dices_generated_small_to_largest = copy_last_to_first_dice[::-1]



    def save_dices_sort(self, dice_reg):
        self._dices_generated_last_to_first.append(dice_reg)   
        self.save_sort_dices(self._dices_generated_last_to_first)

    def save_user_path_dices(self):
        self.obj_historical_IO.save_txt_historical()

    def import_dice_saved(self):
        self._dices_generated_last_to_first[:] = []
        self._dices_generated_first_to_last[:] = []
        self._dices_generated_largest_to_small[:] = []
        self._dices_generated_small_to_largest[:] = []
        self._dices_generated_last_to_first = self.obj_historical_IO.load_txt_historical()
        

    #Gera e salva os dados aleatorios e seus parametros a uma lista (self.dices_generated)
    def generate_dice_save_historical(self,sides,amount,modfier):
        self.save_dices_sort(dice_reg=self.generate_dice(sides, amount, modfier))
        self.save_user_path_dices()

    def clear_dice_historical(self):
        #Limpa os registros do historioco
        self._dices_generated_last_to_first[:] = []
        self._dices_generated_first_to_last[:] = []
        self._dices_generated_largest_to_small[:] = []
        self._dices_generated_small_to_largest[:] = []

    def clear_file_save(self):
        self.obj_historical_IO.clear_txt_historical()

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