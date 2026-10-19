import models.gen_dice_model
import controllers.gen_dice_controller
import models.export_import_historical_model
import excepts.excepts

gdm = models.gen_dice_model.gen_dice_model()
crdc = controllers.gen_dice_controller.ran_dice_controller(gdm)
exp = excepts.excepts
ioh = models.export_import_historical_model.historical_IO(gdm,exp)



a=0
while True:
    crdc.generate_dice(2,4,0)
    a+=1
    if a == 5:
        break

print(crdc.get_dices_historical_first_to_last)
print(ioh.program_user_data_dir)
ioh.save_txt_historical()
