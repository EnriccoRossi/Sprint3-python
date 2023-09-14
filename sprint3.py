# Função para verificar a resposta do usuário
def checa_resp(msg, opcoes):
    resp = input(msg)
    while resp not in opcoes:
        print("Por favor, escreva uma das opções.")
        resp = input(msg)
    return resp

# Função para verificar a situação de uma rua com base nas informações de altura e RPM
def checa_rua(infos, num_rua):
    altura = infos[num_rua][1][0]
    rpm = infos[num_rua][1][1]
    if altura <= 50 and rpm <= 1000:
        print("Nenhum risco de enchente!\n")
    elif altura >= 50 and altura <= 99 and rpm >= 1000 and rpm <= 2999:
        print("Baixo risco de enchente!\n")
    elif altura >= 100 and rpm >= 3000:
        print("Alto risco de enchente!\n")
    return

# Dados de informações das ruas em um dicionário
infos = {
    # "num_rua": ("nome da rua", [altura em cm, rpm])
    "1": ("Avenida Nove de Julho", [30, 800]),
    "2": ("Marginal Pinheiros", [48, 1000]),
    "3": ("Avenida Sumaré", [70, 1500]),
    "4": ("Avenida Antonio Munhoz Bonilha", [150, 3500]),
    "5": ("Rua Ricardo Cavatton", [60, 2000]),
    "6": ("Rua Maria Antonia", [80, 1700]),
    "7": ("Rua Caio Prado", [90, 2300]),
    "8": ("Avenida do Estado", [25, 600]),
    "9": ("Radial Leste-Oeste", [48, 1000]),
    "10": ("Rua São Francisco", [120, 4000])
}
num_rua = infos.keys()
# Mensagens de boas-vindas
print("Seja bem vindo a Alerta Enchentes!")
print("Aqui você vai encontrar informações relacionadas à enchentes sobre a situação de alguns lugares.\n")

# Verifica se o usuário deseja conhecer o serviço
entra = checa_resp("Você deseja conhecer nosso serviço? (s/n)", ["s", "n"])

if entra == "s":
    while True:
        print("Essas são as unidades com as quais trabalhamos: ")
        for key in infos.keys():
            print(f"{key} : {infos[key][0]}")
        escolha = checa_resp("De qual unidade você gostaria de saber a situação atual? (Caso deseje sair escreva 'sair')",
                             ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "sair"])

        if escolha == "sair":
            print("Agradecemos a sua participação, volte sempre!")
            break
        else:
            checa_rua(infos, escolha)
            continue
