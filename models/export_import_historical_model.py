import pathlib
import os

class historical_IO:
    def __init__(self, obj_dice_model,excepts):
        self.obj_dice_model = obj_dice_model
        #Fazer uma forma disso ser definido em um arquivo a parte (save_directory é a definição do local onde vai ser salvo o hisorico)
        print()
        self.program_root = pathlib.Path(__file__).resolve().parent.parent
        self.excepts = excepts

    #Depois adapitar para salvar como json
    #ATENÇÃO isso é uma implementação provisoria na raiz depois adicionar salvamento com platformdirs para salvar com multiplataforma fora do diretorio da aplicação (algo por exemplo appdata do windows) ATENÇÃO isso´é uma implementação provisoria na raiz
    def save_txt_historical(self):
        #Se o diretorio de saves não existir na raiz do programa cria um diretorio
        try:
            if not pathlib.Path(f"{self.program_root}/saves/").exists():
                os.mkdir(os.path.join(self.program_root, "saves"))
            with open(pathlib.Path(f"{self.program_root}/saves/save_historical_dices.txt") , 'a', encoding='utf-8') as historical_file:
                for value in self.obj_dice_model.get_dices_first_to_last:
                    historical_file.write(str(f"{value}\n"))
        except PermissionError:
             raise self.excepts.IO_Deny_Access_Error
        except IOError:
             self.excepts.IO_Generic_Error
             


    def clean_txt_historical(self):
        if pathlib.Path(f"{self.program_root}/saves/save_historical_dices.txt").exists():
            with open(pathlib.Path(f"{self.program_root}/saves/save_historical_dices.txt"), 'w') as historical_file:
                pass
        else:
            raise self.excepts.IO_Dont_Exist_Error

    #Adicionar uma forma de exportar historico em texto legivel
    def export_historical_txt(self):
            pass

    #Adicionar uma forma de exportar historico em Json
    def export_historical_json(self):
        pass

    #Adicionar uma forma de exportar historico em planilha csv
        def export_historical_csv(self):
                pass


    
    