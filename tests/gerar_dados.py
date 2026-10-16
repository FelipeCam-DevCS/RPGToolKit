import models.gen_dice_model
gdm = models.gen_dice_model.gen_dice_model()

a=0
while True:
    gdm.generate_dice_save_historical(2,4,0)
    a+=1
    if a == 5:
        break

print(f"get_dices_first_to_last \n{gdm.get_dices_first_to_last}")
print(f"get_dice_last_to_first \n{gdm.get_dice_last_to_first}")
print(f"dice_largest_to_small \n {gdm.get_dice_largest_to_small}")
print(f"get_dice_small_to_largest \n {gdm.get_dice_small_to_largest}")