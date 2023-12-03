def reajusta_dez_porcento(employees):
    for employee in employees:
        employee["salario"] *= 1.1

def main():
    employees = []
    
    with open("dados_funcionarios.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            employee = {
                "nome": data[0],
                "sobrenome": data[1],
                "ano_nascimento": int(data[2]),
                "RG": data[3],
                "ano_admissao": int(data[4]),
                "salario": float(data[5])
            }
            employees.append(employee)

    reajusta_dez_porcento(employees)

    print("\n===== Lista de Funcionários Reajustada =====")
    for employee in employees:
        print(f"Nome: {employee['nome']} {employee['sobrenome']}, Salário: R${employee['salario']:.2f}")

if __name__ == "__main__":
    main()
