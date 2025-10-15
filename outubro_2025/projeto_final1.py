import os

# --- QUIZ: Estatística em IA ---
quiz_estatistica = [
    {
        "pergunta": "Qual é a distribuição mais usada para modelar erro em regressão linear?",
        "opcoes": ["A) Distribuição Uniforme", "B) Distribuição Normal", "C) Distribuição de Poisson", "D) Distribuição Exponencial"],
        "resposta": "B"
    },
    {
        "pergunta": "O que representa a média de uma distribuição?",
        "opcoes": ["A) O valor mais frequente", "B) O ponto central", "C) A variação", "D) A dispersão"],
        "resposta": "B"
    }
]

# --- QUIZ: Machine Learning ---
quiz_ml = [
    {
        "pergunta": "O que é overfitting?",
        "opcoes": ["A) Quando o modelo generaliza bem", "B) Quando o modelo acerta tudo nos dados de teste", "C) Quando o modelo aprende ruídos dos dados de treino", "D) Quando o modelo é muito simples"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual é a função da regularização?",
        "opcoes": ["A) Aumentar o erro", "B) Reduzir o tempo de treino", "C) Evitar overfitting", "D) Diminuir o número de variáveis"],
        "resposta": "C"
    }
]

# --- Função para abrir PDF ---
def abrir_pdf(nome_arquivo):
    try:
        os.startfile(nome_arquivo)  # Apenas no Windows
    except AttributeError:
        print("\nEste comando funciona apenas no Windows. Abra manualmente:", nome_arquivo)
    except FileNotFoundError:
        print(f"\nArquivo não encontrado: {nome_arquivo}")

# --- Função para executar quiz ---
def executar_quiz(quiz):
    acertos = 0
    for i, q in enumerate(quiz):
        print(f"\nPergunta {i+1}: {q['pergunta']}")
        for opcao in q["opcoes"]:
            print(opcao)
        resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
        if resposta == q["resposta"]:
            print("Certa resposta!")
            acertos += 1
        else:
            print(f"Eeeerrooooouuuu!")
    print(f"\nVocê acertou {acertos} de {len(quiz)} perguntas.")

# --- Menu principal ---
def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Exercícios resolvidos de Estatística (PDF)")
        print("2 - Quiz: Estatística em IA")
        print("3 - Quiz: Machine Learning")
        print("4 - Pesquisa sobre uso de IA (PDF)")
        print("0 - Sair")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == '1':
            abrir_pdf("exercicios_resolvidos.pdf")
        elif escolha == '2':
            executar_quiz(quiz_estatistica)
        elif escolha == '3':
            executar_quiz(quiz_ml)
        elif escolha == '4':
            abrir_pdf("pesquisa_ia.pdf")
        elif escolha == '0':
            print("\nEncerrando o programa. Até a próxima!")
            break
        else:
            print("Opção não é válida. Tente novamente.")

# --- Execução ---
if __name__ == "__main__":
    menu()