#Erro generico na escrita/leitura
class IO_Generic_Error(Exception): pass
#Erro de acesso negado geralmente ocorre por ocupação ao manipular escrita/leitura ou acesso negado
class IO_Deny_Access_Error(Exception): pass

#Erro de arquivo ou qualquer coisa a ser manipulada não existir no momento
class IO_Dont_Exist_Error(Exception): pass