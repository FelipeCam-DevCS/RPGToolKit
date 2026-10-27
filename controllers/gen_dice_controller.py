import random

class ran_dice_controller:
    def __init__(self, obj_dice_model):
        self._obj_dice_model = obj_dice_model

    def import_dices_saved(self):
        self._obj_dice_model.save_sort_dices(self.get_dice_historical_last_to_first)
        self._obj_dice_model.import_dice_saved()

    def save_sort_dices(self):
        self._obj_dice_model.save_sort_dices()

    #Validação de parametros e geração de dados no obj_dice_model
    def generate_dice(self, sides, amount, modfier):
        if isinstance(amount, int) and isinstance(sides, int) and (isinstance(modfier, float) or isinstance(modfier, int)):
            self._obj_dice_model.generate_dice_save_historical(sides, amount, modfier)
        else:
            raise ValueError

    def clear_file_historical(self):
        self._obj_dice_model.clear_file_save()

        
    def clear_historical(self):
        self._obj_dice_model.clear_dice_historical()

    @property
    def get_dices_historical_first_to_last(self):
        return self._obj_dice_model.get_dices_first_to_last
    
    @property
    def get_dice_historical_last_to_first(self):
        return self._obj_dice_model.get_dice_last_to_first

    @property
    def get_dice_historical_largest_to_small(self):
        return self._obj_dice_model.get_dice_largest_to_small
    
    @property
    def get_dice_historical_small_to_largest(self):
        return self._obj_dice_model.get_dice_small_to_largest