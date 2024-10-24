import requests

## URL da API do json-server
url = 'http://localhost:3000/clientes'

class ClientesApiService:

    def buscarClientes(self):
        response = requests.get(url)

        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print('Erro ao acessar a API:', response.status_code)



    ## GET com parametro
    def buscarCliente(self, id=None, nome=None):
        if id is not None and nome is not None:
            response = requests.get(f"{url}?id={id}&nome={nome}")
        elif id is not None:
            response = requests.get(f"{url}/{id}")
        elif nome is not None: 
            response = requests.get(f"{url}?nome={nome}")   
        else:
            self.buscarClientes()
            return 
        
        if response.status_code == 200:
            users = response.json()
            print(users)
            return
        else:
            print('Erro ao acessar a API:', response.status_code)

    # Post sendo enviado o body JSON
    def adicionarCliente(self, nome):
        novo_cliente = {"nome": nome}
        response = requests.post(url, json=novo_cliente)

        if response.status_code == 201:
            print(f"{nome} foi adicionado a lista de clientes")
        else:
            print('Erro ao adicionar cliente:', response.status_code)


        # Put sendo enviado o body JSON
    def alterarCliente(self, id, nome):
        cliente_atualizado = {"nome": nome}
        response = requests.put(f"{url}/{id}", json=cliente_atualizado)

        if response.status_code == 200:
            print(f"{nome} foi atualizado na lista de clientes")
        else:
            print('Erro ao atualizar cliente:', response.status_code)


            # Delete para remover 
    def removerCliente(self, id):
        response = requests.delete(f"{url}/{id}")

        if response.status_code == 200:
            print(f"Cliente de codigo {id} foi removido da lista de clientes")
        else:
            print('Erro ao remover cliente:', response.status_code)

servico = ClientesApiService()
servico.removerCliente("1")

