class ValidarMenu:       
    def validar_opcao(self,op):
        URL_BASE = None
        if op == "1":
            URL_BASE= "https://atacadobarato.com/"
            return  URL_BASE
        elif op == "2":
            URL_BASE= "https://www.meufornecedor.com/produtos/"
            return  URL_BASE
        elif op == "3":
            URL_BASE= "https://www.meufornecedor.com/original/"
            return  URL_BASE
        else: 
            print("Opção inválida. Saindo.")
            exit()
            
        
        
