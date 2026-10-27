from models import gen_dice_model, export_import_historical_model
from controllers import gen_dice_controller
from views import custom_tkinter
from excepts import excepts

def main():
    obj_excepts = excepts
    obj_dice_model = gen_dice_model.gen_dice_model()
    obj_historical_IO = export_import_historical_model.historical_IO(obj_dice_model, excepts)
    obj_dice_model.set_obj_historical_IO(obj_historical_IO)
    obj_dice_controller = gen_dice_controller.ran_dice_controller(obj_dice_model)
    view_custom_tkinter = custom_tkinter.Ctk_UI_Main(obj_dice_controller, excepts)

    
    #Inicializa a interface grafica em custom tkinter
    view_custom_tkinter.mainloop()

if __name__ == "__main__":
    main()