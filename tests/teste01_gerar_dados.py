import models.gen_dice_model
gdm = models.gen_dice_model.gen_dice_model()

a=0
while True:
    gdm.generate_dice_save_historical(2,4,0)
    a+=1
    if a == 10:
        break

print(gdm._dices_generated)