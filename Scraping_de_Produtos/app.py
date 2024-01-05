
from validar_menu import *
import sys
from produtos import *

validar = ValidarMenu()

opcao = sys.argv[1] if len(sys.argv) > 1 else None
categoria = validar.validar_opcao(opcao)

produtos = Produtos(categoria)
  
produtos.gerar_planilha_xlsx()

