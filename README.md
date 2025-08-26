# Projeto Lista de Chamada

Este projeto é um sistema de lista de chamada escolar com interface gráfica desenvolvida em Python utilizando a biblioteca Tkinter.
Ele permite registrar presenças e faltas dos alunos, salvar os dados em um banco SQLite e até simular o envio de notificações para os pais dos alunos faltosos via WhatsApp (simulação por console).

### Funcionalidades
- Criar uma lista de chamada para os alunos.
- Marcar presença ou falta em diferentes dias da semana.
- Salvar os registros no banco de dados SQLite.
- Consultar os alunos que faltaram em cada dia.
- Simular envio de notificações de falta para os pais via WhatsApp (console).
- Interface gráfica simples e intuitiva.

### Estrutura do Projeto
- `main.py` → Funções de banco de dados (criar banco, salvar presenças, consultar faltas).
- `app.py` → Classe ListaChamadaApp, responsável pela interface gráfica em Tkinter.
- `notificacao.py` → Função para enviar notificações simuladas no console.

### Tecnologias Utilizadas
- **Python 3**
- **Tkinter (GUI)**
- **SQLite3 (banco de dados)**
- **MessageBox para exibir mensagens**
