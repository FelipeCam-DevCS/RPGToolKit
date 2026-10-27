import customtkinter as ctk
from tkinter import messagebox

'''
ATENÇÃO ESSE CODIGO É PROVISORIO TUDO QUE ESTA AQUI VAI PASSAR POR REFATORAÇÕES DE CODIGO MELHORIAS DE LEGIBILIDADE, ORGANIZAÇÃO E CORREÇÃO
PROVAVELMENTE A EXTRUTURA IRA MUDAR DAS PARTES MAIS IMPROVISADAS.
'''


class Ctk_UI_Main(ctk.CTk):
    def __init__(self, obj_dice_controller, excepts):
        super().__init__()
        self.excepts = excepts
        self.obj_dice_controller = obj_dice_controller
        self.title("RPGToolKit by FelipeDevCS")
        self.geometry("800x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

        self.dices_rolled_frame_list = [""]
        self.rowconfigure(0, weight=0)
        self.dices_rolled_frame = ctk.CTkScrollableFrame (self, fg_color="#013220" )
        self.dices_rolled_frame.pack( fill="both", expand=True, padx=25, pady=20)
        self.btn_roll = ctk.CTkButton(self, text="Roll!", corner_radius= 10 ,command=self.roll_button_event, height=50, width=50, border_width=2, border_color="green", fg_color="darkgreen")
        self.btn_roll.pack(padx=20, pady=20, side="right")
        self.label_dice_list_title = ctk.CTkLabel(self.dices_rolled_frame, text="Dice historical", bg_color="gray")
        self.label_dice_list_title.pack(side="top", fill="x", pady=0, padx=0)
        self.btn_delete = ctk.CTkButton(self, text="Delete historical", corner_radius= 10, width=90, height=50, command=self.delete_dice, border_width=2, border_color="tomato", fg_color="darkred")
        self.btn_delete.pack(side="left", pady=10, padx=10)
        
        self.label_entry_modifier = ctk.CTkLabel(self,text="Modfier")
        self.label_entry_modifier.pack(side="right")
        self.entry_modfier = ctk.CTkEntry(self, placeholder_text="0", width=50)
        self.entry_modfier.pack(pady=10, padx=10, side="right")
        
        self.label_entry_sides = ctk.CTkLabel(self,text="Sides")
        self.entry_sides = ctk.CTkEntry(self, placeholder_text="20", width=50)
        self.label_entry_sides.pack(side="right")
        self.entry_sides.pack(pady=10, padx=10, anchor="center", side="right")

        self.label_entry_amount = ctk.CTkLabel(self,text="Amount")
        self.label_entry_amount.pack(side="right")
        self.entry_amount = ctk.CTkEntry(self, placeholder_text="1", width=50)
        self.entry_amount.pack(pady=10, padx=10, side="right")


        self.dice_rolled_frame_list = []
        try:
            self.obj_dice_controller.import_dices_saved()
            self.load_dices()
        except self.excepts.IO_Dont_Exist_Error:
            messagebox.showinfo("Historico anterior inexistente", "Nenhum arquivo de historico foi encontrado caso seja sua primeira isso é normal e os arquivos vão ser gerados.")
        except self.excepts.IO_Invalid_integrity:
            messagebox.showerror(f"Integridade invalida",f"ATENÇÃO não foi possivel importar dados anteriormente gerados caso mais algum dado.\n\nCaso algum dado for gerado o seu conteudo sera substituido pelos dados dessa sessão e o prgrama volta a funcionar normalmente.")

        try:
            self.obj_dice_controller.import_dices_saved()
            self.load_dices()
        except self.excepts.IO_Dont_Exist_Error:
            messagebox.showinfo("Historico anterior inexistente", "Nenhum arquivo de historico foi encontrado caso seja sua primeira isso é normal e os arquivos vão ser gerados.")
        except self.excepts.IO_Invalid_integrity:
            messagebox.showerror(f"Integridade invalida",f"ATENÇÃO não foi possivel importar dados anteriormente gerados caso mais algum dado.\n\nCaso algum dado for gerado o seu conteudo sera substituido pelos dados dessa sessão e o prgrama volta a funcionar normalmente.")

    def create_dice_frame(self,value ,sides, amount, modfier):
        dice_rolled_frame_width = self.dices_rolled_frame.winfo_width()#Tamanho do frame principal
        
        #Instancia um novo frame de dado
        self.dice_rolled_frame = ctk.CTkFrame(self.dices_rolled_frame, height=100, width=dice_rolled_frame_width, fg_color="olive", border_color="green", border_width=5)
        self.dice_rolled_frame_list.append(self.dice_rolled_frame)
        #Cria o frame na janela
        self.dice_rolled_frame.pack(pady=10, padx= 25, fill="x")
        
        #Desabilita o tamanho automatico do frame do dado gerado
        self.dice_rolled_frame.pack_propagate(False)
        self.update_idletasks() #Atualiza a renderização para definir os valores de tamanho
        dice_rolled_frame_height = self.dice_rolled_frame.winfo_height()

        self.label_value = ctk.CTkLabel(self.dice_rolled_frame, text=f"Value: {value}")
        self.label_dice = ctk.CTkLabel(self.dice_rolled_frame, text=f"{amount}d{sides} + {modfier}")

        self.label_valor_modfier = ctk.CTkLabel(self.dice_rolled_frame, text=f"Modfier: {modfier}")
        self.label_value.pack(side="left", padx=10)
        self.label_dice.pack(side="right", padx=10)
        
    def roll_button_event(self):
        try:
            sides = int(self.entry_sides.get()) 
            amount = int(self.entry_amount.get())
            modfier = int(self.entry_modfier.get())
        except ValueError:
            messagebox.showinfo("Atenção","Os valores inseridos não é valido")

        self.obj_dice_controller.generate_dice(sides,amount,modfier)
        self.load_dices()
        
    def load_dices(self):
        self.obj_dice_controller.import_dices_saved() 

        try:
            for itens in self.dice_rolled_frame_list:
                itens.destroy()
        except AttributeError: pass
        
        for i in range(len(self.obj_dice_controller.get_dice_historical_last_to_first)):
            value = self.obj_dice_controller.get_dice_historical_last_to_first[i][0]
            sides = self.obj_dice_controller.get_dice_historical_last_to_first[i][1]
            amount = self.obj_dice_controller.get_dice_historical_last_to_first[i][2]
            modfier = self.obj_dice_controller.get_dice_historical_last_to_first[i][3]
            self.create_dice_frame(value, sides, amount, modfier)
        

        
    def delete_dice(self):
        self.obj_dice_controller.clear_historical()
        self.obj_dice_controller.clear_file_historical()
        self.load_dices()