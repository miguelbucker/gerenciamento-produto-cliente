import http.client
import json
import pandas as pd

class EnderecoApiService:
    
    def consultarEnderecoIbge(self):

        # Conectar ao servidor de API da Via Cep
        apiViaCep = http.client.HTTPSConnection("viacep.com.br")

        while True:
            #Solicitar o CEP ao usuário
            cep = input("Digite o CEP para consultar o endereço: ")
            
            #Enviar requisição GET
            apiViaCep.request("GET", f"/ws/{cep}/json/")

            #Obter a resposta
            response = apiViaCep.getresponse()

            #Variável padrão que contem todos os dados
            data = response.read().decode("utf-8")
            endereco = json.loads(data)

            endereco_simples = [
            
            {
                "logradouro" : endereco.get("logradouro"),
                "bairro"  : endereco.get("bairro"),
                "localidade"  : endereco.get("localidade"),
                "uf": endereco.get("uf")
            }
            ]

            tabela = pd.DataFrame(endereco_simples)
            print(tabela)
            break

servico = EnderecoApiService()
servico.consultarEnderecoIbge()