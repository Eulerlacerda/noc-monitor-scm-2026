import datetime

# ==============================
# SISTEMA NOC - MONITORAMENTO NOC
# Autor: Euler Lacerda
# Disciplina: Projeto de Software Avançado
# Professor(a) Mestre: Marco Ikuro Hisatomi
# ==============================

ARQUIVO_DISPOSITIVOS = "dispositivos.txt"
ARQUIVO_LOG = "log.txt"


def carregar_dispositivos():
    """Carrega lista de dispositivos do arquivo"""
    try:
        with open(ARQUIVO_DISPOSITIVOS, "r") as file:
            dispositivos = file.readlines()
        return [d.strip() for d in dispositivos]
    except FileNotFoundError:
        print("Arquivo de dispositivos não encontrado.")
        return []


def verificar_status(dispositivo):
    """
    Simulação de verificação de status.
    (Para aula prática, status é alternado manualmente)
    """
    import random
    return random.choice(["ONLINE", "OFFLINE"])


def registrar_log(mensagem):
    """Registra eventos no arquivo de log"""
    with open(ARQUIVO_LOG, "a") as log:
        log.write(f"{datetime.datetime.now()} - {mensagem}\n")


def monitorar():
    print("====================================")
    print(" SISTEMA DE MONITORAMENTO NOC ")
    print("====================================\n")

    dispositivos = carregar_dispositivos()

    if not dispositivos:
        print("Nenhum dispositivo cadastrado.")
        return

    for dispositivo in dispositivos:
        status = verificar_status(dispositivo)
        print(f"{dispositivo} -> {status}")

        if status == "OFFLINE":
            alerta = f"ALERTA: {dispositivo} está OFFLINE!"
            print(alerta)
            registrar_log(alerta)


if __name__ == "__main__":
    monitorar()