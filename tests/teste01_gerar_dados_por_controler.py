import models.gen_dice_model
import controllers.gen_dice_controller

gdm = models.gen_dice_model.gen_dice_model()
crdc = controllers.gen_dice_controller.ran_dice_controller(gdm)



a=0
while True:
    crdc.gen_dice(2,4,0)
    a+=1
    if a == 10:
        break

print(crdc.get_historical)
print()
crdc.clear_historical
print(crdc.get_historical)