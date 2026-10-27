import models.gen_dice_model
import controllers.gen_dice_controller
import models.export_import_historical_model
import excepts.excepts

exp = excepts.excepts
gdm = models.gen_dice_model.gen_dice_model()
crdc = controllers.gen_dice_controller.ran_dice_controller(gdm)
ioh = models.export_import_historical_model.historical_IO(gdm, exp)
gdm.set_obj_historical_IO(obj_historical_IO = ioh)



a=0
while True:
    crdc.generate_dice(sides=20,amount=1,modfier=0)
    a+=1
    if a == 5:
        break
print(crdc.get_dices_historical_first_to_last)
