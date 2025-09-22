"""Para a atividade desta semana, você deverá criar um interator que irá iterar os dados da API (Application Interface) da tabela FIPE e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe que fará o papel de interator no momento da instanciação, neste caso use o ID de uma marca).

Para trazer esses dados, será necessário interagir com a API da FIPE disponível nesse endereço: https://deividfortuna.github.io/fipe/. Dicas:

Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas dessa forma serão listadas todas as marcas que a API possui. Escolha uma para ser usada na próxima etapa, grave o ID dela para ser usado no seu código.
Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando a URL: https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, com os modelos dos veículos que ela possui.
Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do veículo da marca selecionada.
OBS: Ao usar a biblioteca de requests é necessário criar um header com o User-agent setado com algum valor. É um pré-requisito da API que será usada. Exemplo de headers: headers = {‘user-agent’: ‘MyStudyApp’}."""

# Resposta 
import requests

# -------------------------------
# Função auxiliar para listar marcas
# -------------------------------
def listar_marcas():
    url = "https://parallelum.com.br/fipe/api/v1/carros/marcas"
    headers = {"user-agent": "MyStudyApp"}  # requisito da API
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        marcas = response.json()
        print("\n=== LISTA DE MARCAS DISPONÍVEIS ===")
        for marca in marcas:
            print(f"ID: {marca['codigo']} | Nome: {marca['nome']}")
    else:
        print("❌ Erro ao acessar a API:", response.status_code)


# -------------------------------
# Classe Iteradora para modelos de uma marca
# -------------------------------
class FipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca_id}/modelos"
        self.headers = {"user-agent": "MyStudyApp"}
        self.modelos = self._get_modelos()
        self.index = 0

    def _get_modelos(self):
        """Busca os modelos da marca na API"""
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 200:
            data = response.json()
            return data["modelos"]  # a API retorna {"modelos": [...], "anos": [...]}
        else:
            print("❌ Erro ao acessar a API:", response.status_code)
            return []

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.modelos):
            modelo = self.modelos[self.index]
            self.index += 1
            return modelo["codigo"], modelo["nome"]
        else:
            raise StopIteration


# -------------------------------
# Programa principal (CLI)
# -------------------------------
if __name__ == "__main__":
    print("=== CONSULTA FIPE ===")
    print("1. Listar marcas")
    print("2. Listar modelos de uma marca")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        listar_marcas()

    elif opcao == "2":
        marca_id = input("Digite o ID da marca: ").strip()
        fipe_iter = FipeIterator(marca_id)
        print(f"\n=== MODELOS DA MARCA {marca_id} ===")
        for codigo, nome in fipe_iter:
            print(f"ID: {codigo} | Nome: {nome}")

    else:
        print("⚠️ Opção inválida!")
