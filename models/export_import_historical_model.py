import pathlib
import platformdirs

class historical_IO:
    def __init__(self, obj_dice_model,excepts):
        self.obj_dice_model = obj_dice_model
        #Fazer uma forma disso ser definido em um arquivo a parte (save_directory é a definição do local onde vai ser salvo o hisorico)
        self._program_user_data_path = platformdirs.user_data_path("RPGToolKit", appauthor=False)
        self._program_root = pathlib.Path(__file__).resolve().parent.parent
        self._excepts = excepts

    #Depois adapitar para salvar como json

    def save_txt_historical(self, path_save=None):
        if path_save == None:
            path_save = self._program_user_data_path

        if not isinstance(path_save, pathlib.Path):
            raise self._excepts.IO_Invalid_Path
        
        #Se o diretorio de saves não existir na raiz do programa cria um diretorio
        try:
            if not pathlib.Path(path_save).exists():
                pathlib.Path(f"{path_save}/saves").mkdir(parents=True)

            if not pathlib.Path(f"{path_save}/saves/save_historical_dices.txt").is_file():
                with open(pathlib.Path(f"{path_save}/saves/save_historical_dices.txt") , 'a', encoding='utf-8') as historical_file:
                    for value in self.obj_dice_model._dices_generated_first_to_last:
                        historical_file.write(str(f"{value}\n"))
            else:
                with open(pathlib.Path(f"{path_save}/saves/save_historical_dices.txt") , 'w', encoding='utf-8') as historical_file:
                                    for value in self.obj_dice_model._dices_generated_first_to_last:
                                        historical_file.write(str(f"{value}\n"))
        except PermissionError:
             raise self._excepts.IO_Deny_Access_Error
        except IOError:
             self._excepts.IO_Generic_Error
             


    def clear_txt_historical(self):
        if pathlib.Path(f"{self._program_user_data_path}/saves/save_historical_dices.txt").exists():
            with open(pathlib.Path(f"{self._program_user_data_path}/saves/save_historical_dices.txt"), 'w') as historical_file:
                pass
        else:
            raise self._excepts.IO_Dont_Exist_Error

    #Adicionar uma forma de exportar historico em texto legivel
    def load_txt_historical(self, path_save=None):
        if path_save == None:
            path_save = self._program_user_data_path

        if not isinstance(path_save, pathlib.Path):
                    raise self._excepts.IO_Invalid_Path

        if not pathlib.Path(path_save).exists():
            raise self._excepts.IO_Dont_Exist_Error

        with open(pathlib.Path(f"{path_save}/saves/save_historical_dices.txt") , 'r', encoding='utf-8') as historical_file:
            historical_matrix = []
            dice_list = []
            for line in historical_file.readlines():
               if line == "":
                   return historical_matrix
               line = line.replace("[","").replace("]", "").replace("\n", "")
               values = line.split(",")


               dice_list = []
               for value in values:
                    try:
                        dice_list.append(int(value))
                    except ValueError:
                        raise self._excepts.IO_Invalid_integrity
                    
               historical_matrix.append(dice_list)
                    
                    
                            
            #historical_matrix.append(dice_list)
               #print(dice_list)
            return historical_matrix
               

                


    def export_historical_txt(self):
        pass

    #Adicionar uma forma de exportar historico em Json
    def export_historical_json(self):
        pass

    #Adicionar uma forma de exportar historico em planilha csv
    def export_historical_csv(self):
            pass


    
    