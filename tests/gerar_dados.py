import models.gen_dice_model
gdm = models.gen_dice_model.gen_dice_model()

a=0
while True:
    gdm.generate_dice_save_historical(2,4,0)
    a+=1
    if a == 5:
        break

print(f"self._dices_generated_last_to_first \n{gdm._dices_generated_last_to_first}")
print(f"self._dices_generated_small_to_largest \n{gdm._dices_generated_small_to_largest}")
print(f"self._dices_generated_largest_to_small \n {gdm._dices_generated_largest_to_small}")
print(f"self._dices_generated_first_to_last \n {gdm._dices_generated_first_to_last}")