import sqlite3

#cria o banco de dados e a tabela se n existirem
def criar_banco():
    conn = sqlite3.connect("chamada.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chamada (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dia_semana TEXT NOT NULL, 
            aluno TEXT NOT NULL,
            presente INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

#salvar presença no banco de dados
def salvar_presenca(presencas):
    conn = sqlite3.connect("chamada.db")
    cursor = conn.cursor()
    for aluno, dias in presencas.items():
        for dia, presente in dias.items():
            cursor.execute("INSERT INTO chamada (aluno, dia_semana, presente) VALUES (?, ?, ?)",
                          (aluno, dia, presente))
    conn.comit()
    conn.close()