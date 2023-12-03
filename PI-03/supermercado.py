def insert_product(products):
    code = input("Digite o código do produto: ")
    name = input("Digite o nome do produto: ").capitalize()
    price = input("Digite o preço do produto: ")
    
    product = {"code": code, "name": name, "price": price}
    products.append(product)
    print("Produto cadastrado com sucesso!")

def delete_product(products):
    code_to_delete = input("Digite o código do produto a ser excluído: ")
    for product in products:
        if product["code"] == code_to_delete:
            products.remove(product)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def list_products(products):
    for product in products:
        print(f"Código: {product['code']}, Nome: {product['name']}, Preço: R${product['price']}")

def search_price(products):
    code_to_search = input("Digite o código do produto para consultar o preço: ")
    for product in products:
        if product["code"] == code_to_search:
            print(f"O preço do produto {product['name']} é R${product['price']}")
            return
    print("Produto não encontrado.")

def main():
    products = []
    while True:
        print("\n===== Menu Supermercado =====")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            insert_product(products)
        elif choice == "2":
            delete_product(products)
        elif choice == "3":
            list_products(products)
        elif choice == "4":
            search_price(products)
        elif choice == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
