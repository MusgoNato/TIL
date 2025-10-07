dados = [
    {
        "nome": "João da Silva",
        "cpf": "12345678900",
        "rg": "11223344",
        "orgao_emissor": "SSP",
        "data_expedicao": "10/01/2015",
        "filiacao": "Maria da Silva / José da Silva",
        "dt_nasc": "15/05/1990",
        "naturalidade": "Rio de Janeiro",
        "nacionalidade": "Brasileiro",
        "sexo": "Masculino",
        "estado_civil": "Solteiro",
        "profissao": "Programador",
        "logradouro": "Rua das Flores",
        "numero_logradouro": "100",
        "complemento_logradouro": "Apto 202",
        "bairro": "Centro",
        "cidade": "Rio de Janeiro",
        "estado": "RJ",
        "cep": "20000-000",
        "telefone": "(21) 99999-9999",
        "email": "joao.silva@email.com"
    }
]

dados_convenente = [
    {
        "nome": "Prefeitura Municipal",
        "instituicoes": ["Banco do Brasil", "Caixa Econômica Federal"]
    }
]

dados_instituicao_credora = [
    "Banco do Brasil"
]

dados_contratos = [
    {
        "cpf_cliente": "12345678900",
        "convenente": "Prefeitura Municipal",
        "instituicao": "Banco do Brasil",
        "tipo_contrato": "consignacao",
        "tipo_operacao": "novo",
        "valor_bruto": 10000.0,
        "valor_liquido": 9500.0,
        "taxa_mensal": 1.5,
        "data_concessao": "01/08/2023",
        "data_primeira": "01/09/2023",
        "data_ultima": "01/08/2024",
        "valor_parcela": 950.0,
        "prazo": 12
    }
]



# -------- Cadastro de clientes --------
def get_dados_cliente():
    print("-------Informações pessoais------\n")
    nome = str(input("Nome completo: "))
    cpf = str(input("Numero do CPF: "))
    print("---------Informações do RG-----------\n")
    rg = str(input("Numero do RG: "))
    orgao_emissor = str(input("Orgao emissor: "))
    data_expedicao = str(input("Data de expedição: "))

    print("---------------Informações relevantes---------------\n")
    filiacao = str(input("Filiação: "))
    dt_nasc = str(input("Data de nascimento: "))
    naturalidade = str(input("Naturalidade: "))
    nacionalidade = str(input("Nacionalidade: "))
    sexo = str(input("Sexo: "))
    estado_civil = str(input("Estado civil: "))
    profissao = str(input("Profissao: "))

    print("---------------Endereço---------------\n")
    logradouro = str(input("Logradouro: "))
    numero_logradouro = str(input("Numero do logradouro: "))
    complemento_logradouro = str(input("Complemento: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Estado: "))
    cep = str(input("CEP: "))
    telefone = str(input("Telefone: "))
    email = str(input("Email: "))

    return {
        "nome": nome, "cpf": cpf, "rg": rg, "orgao_emissor": orgao_emissor, "data_expedicao": data_expedicao,
        "filiacao": filiacao, "dt_nasc": dt_nasc, "naturalidade": naturalidade, "nacionalidade": nacionalidade,
        "sexo": sexo, "estado_civil": estado_civil, "profissao": profissao,
        "logradouro": logradouro, "numero_logradouro": numero_logradouro, "complemento_logradouro": complemento_logradouro,
        "bairro": bairro, "cidade": cidade, "estado": estado, "cep": cep, "telefone": telefone, "email": email
    }


def insert_dados_cliente(cliente):
    dados.append(cliente)


# -------- Convenentes --------
def get_dados_convenentes():
    print("------------PREENCHIMENTO DE DADOS CONVENENTES------------\n")
    nome_convenente = str(input("Nome convenente: "))
    instituicoes_fi_conveniadas = []
    while True:
        nome_instituicao = str(input("Nome da instituição financeira: ('q' para sair) "))
        if nome_instituicao == 'q':
            break
        instituicoes_fi_conveniadas.append(nome_instituicao)
    return nome_convenente, instituicoes_fi_conveniadas


def insert_dados_convenentes(nome_convenente, instituicoes_financeiras):
    dados_convenente.append({"nome": nome_convenente, "instituicoes": instituicoes_financeiras})


# -------- Instituição credora --------
def get_nome_instituicao_credora():
    nome_instituicao_credora = str(input("Nome da instituição credora: "))
    return nome_instituicao_credora


def insert_instituicao_credora(nome_instituicao_credora):
    dados_instituicao_credora.append(nome_instituicao_credora)


# -------- Cadastro de contrato (RF_F1) --------
def get_dados_contrato():
    print("------------CADASTRO DE CONTRATO------------\n")
    cpf_cliente = str(input("CPF do cliente: "))
    convenente = str(input("Convenente: "))
    instituicao = str(input("Instituição credora: "))
    tipo_contrato = str(input("Tipo de contrato (consignacao/habitacional/veiculos/cartao/credito_pessoal): "))
    tipo_operacao = str(input("Operacao (novo/divida/refin): "))

    valor_bruto = float(input("Valor concedido bruto: "))
    valor_liquido = float(input("Valor concedido liquido: "))
    taxa_mensal = float(input("Taxa mensal: "))
    data_concessao = str(input("Data concessao (dd/mm/aaaa): "))
    data_primeira = str(input("Data venc. primeira parcela (dd/mm/aaaa): "))
    data_ultima = str(input("Data venc. ultima parcela (dd/mm/aaaa): "))
    valor_parcela = float(input("Valor parcela: "))
    prazo = int(input("Prazo em meses: "))

    contrato = {
        "cpf_cliente": cpf_cliente,
        "convenente": convenente,
        "instituicao": instituicao,
        "tipo_contrato": tipo_contrato,
        "tipo_operacao": tipo_operacao,
        "valor_bruto": valor_bruto,
        "valor_liquido": valor_liquido,
        "taxa_mensal": taxa_mensal,
        "data_concessao": data_concessao,
        "data_primeira": data_primeira,
        "data_ultima": data_ultima,
        "valor_parcela": valor_parcela,
        "prazo": prazo
    }
    return contrato


def insert_dados_contrato(contrato):
    dados_contratos.append(contrato)


# -------- Consultas (RF_S1, RF_S2) --------
def consulta_cliente(cpf):
    for c in dados:
        if c["cpf"] == cpf:
            print(f"\nCliente encontrado: {c['nome']} - CPF {c['cpf']}")
            print("Contratos do cliente:")
            for contrato in dados_contratos:
                if contrato["cpf_cliente"] == cpf:
                    print(contrato)
            return
    print("Cliente não encontrado.")


def consulta_convenentes():
    print("Convenentes cadastrados:")
    for c in dados_convenente:
        print(f"- {c['nome']} -> Instituições: {c['instituicoes']}")


def consulta_instituicoes():
    print("Instituições credoras cadastradas:")
    for inst in dados_instituicao_credora:
        print(f"- {inst}")


# -------- Relatórios (RF_S3, RF_S4) --------
def relatorio_contratos():
    print("\n--- Relatório de Contratos ---")
    print(f"Total de contratos: {len(dados_contratos)}")
    for contrato in dados_contratos:
        print(contrato)


def relatorio_clientes_sem_operacao():
    print("\n--- Clientes sem contrato ---")
    cpfs_com_contrato = [c["cpf_cliente"] for c in dados_contratos]
    for c in dados:
        if c["cpf"] not in cpfs_com_contrato:
            print(f"{c['nome']} - CPF {c['cpf']}")

# -------- Exclusões --------
def excluir_cliente(cpf):
    global dados, dados_contratos
    for c in dados:
        if c["cpf"] == cpf:
            dados.remove(c)
            # também remover contratos associados
            dados_contratos = [contrato for contrato in dados_contratos if contrato["cpf_cliente"] != cpf]
            print(f"Cliente {cpf} e seus contratos foram excluídos.")
            return
    print("Cliente não encontrado.")


def excluir_convenente(nome):
    for c in dados_convenente:
        if c["nome"] == nome:
            dados_convenente.remove(c)
            print(f"Convenente '{nome}' excluído.")
            return
    print("Convenente não encontrado.")


def excluir_instituicao(nome):
    for inst in dados_instituicao_credora:
        if inst == nome:
            dados_instituicao_credora.remove(inst)
            print(f"Instituição credora '{nome}' excluída.")
            return
    print("Instituição não encontrada.")


def excluir_contrato(cpf_cliente, instituicao):
    for contrato in dados_contratos:
        if contrato["cpf_cliente"] == cpf_cliente and contrato["instituicao"] == instituicao:
            dados_contratos.remove(contrato)
            print(f"Contrato do cliente {cpf_cliente} com a instituição {instituicao} foi excluído.")
            return
    print("Contrato não encontrado.")



def menu():
    while True:
        print("\n===== MENU =====")
        print("[0] Registrar cliente")
        print("[1] Registrar convenente")
        print("[2] Registrar instituição credora")
        print("[3] Registrar contrato")
        print("[4] Consultar cliente + contratos")
        print("[5] Consultar convenentes")
        print("[6] Consultar instituições credoras")
        print("[7] Relatório de contratos")
        print("[8] Relatório clientes sem operação")
        print("[9] Excluir cliente")
        print("[10] Excluir convenente")
        print("[11] Excluir instituição credora")
        print("[12] Excluir contrato")
        print("[13] Sair")

        selecao = int(input("Escolha: "))
        match selecao:
            case 0:
                cliente = get_dados_cliente()
                insert_dados_cliente(cliente)
            case 1:
                nome_convenente, instituicoes_financeiras = get_dados_convenentes()
                insert_dados_convenentes(nome_convenente, instituicoes_financeiras)
            case 2:
                nome_instituicao = get_nome_instituicao_credora()
                insert_instituicao_credora(nome_instituicao)
            case 3:
                contrato = get_dados_contrato()
                insert_dados_contrato(contrato)
            case 4:
                cpf = str(input("Digite o CPF do cliente: "))
                consulta_cliente(cpf)
            case 5:
                consulta_convenentes()
            case 6:
                consulta_instituicoes()
            case 7:
                relatorio_contratos()
            case 8:
                relatorio_clientes_sem_operacao()
            case 9:
                cpf = str(input("CPF do cliente para excluir: "))
                excluir_cliente(cpf)
            case 10:
                nome = str(input("Nome do convenente para excluir: "))
                excluir_convenente(nome)
            case 11:
                nome = str(input("Nome da instituição credora para excluir: "))
                excluir_instituicao(nome)
            case 12:
                cpf_cliente = str(input("CPF do cliente: "))
                instituicao = str(input("Instituição do contrato: "))
                excluir_contrato(cpf_cliente, instituicao)
            case 13:
                print("Saindo...")
                break
            case _:
                print("Opção inválida!")



if __name__ == "__main__":
    menu()
