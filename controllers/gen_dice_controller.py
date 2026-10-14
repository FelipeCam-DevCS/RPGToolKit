import random

class ran_dice_controller:
    def __init__(self, obj_dice_model):
        self._obj_dice_model = obj_dice_model

#Validação de parametros e geração de dados no obj_dice_model
    def gen_dice(self, sides, amount, modfier):
        if isinstance(amount, int) and isinstance(sides, int) and (isinstance(modfier, float) or isinstance(modfier, int)):
            self._obj_dice_model.generate_dice_save_historical(sides, amount, modfier)
        else:
            raise TypeError

    @property
    def get_historical(self):
        return self._obj_dice_model.get_dices_generated

    def clear_historical(self):
        self._obj_dice_model.clear_dice_historical()