import sqlite3

def alunos_faltaram():
    conn = sqlite3.connect("chamada.db")
    cursor = conn.cursor()

    cursor.execute("SELECT aluno, dia_semana FROM chamada WHERE presente = 0")
    faltas = cursor.fetchall()

    conn.close()
    return faltas

def enviar_notificacao_whatsapp():
    faltas = alunos_faltaram()

    if not faltas:
        print("✅ Todos os alunos vieram para a escola hoje.")
    else:
        for aluno, dia in faltas:
            # Aqui simulamos o envio via WhatsApp
            print(f"[WhatsApp] Enviando mensagem para os pais de {aluno}:")
            print(f" - Seu filho(a) {aluno} faltou na {dia}.")
            print("--------------------------------------------")


if __name__ == "__main__":
    enviar_notificacao_whatsapp()
