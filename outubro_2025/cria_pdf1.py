from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import os
import platform
 
# -------------------------
# Dados das perguntas
# -------------------------
perguntas_estat = [
    {"pergunta": "Qual medida representa a média dos quadrados dos desvios?", "opcoes": ["A) Variância", "B) Desvio padrão", "C) Moda", "D) Mediana"], "correta": "A"},
    {"pergunta": "Distribuição mais usada para modelar eventos raros:", "opcoes": ["A) Normal", "B) Poisson", "C) Binomial", "D) Uniforme"], "correta": "B"},
    {"pergunta": "O valor que divide a amostra ao meio é chamado de:", "opcoes": ["A) Média", "B) Mediana", "C) Moda", "D) Variância"], "correta": "B"},
    {"pergunta": "Se todos os valores têm a mesma probabilidade de ocorrer, temos a distribuição:", "opcoes": ["A) Normal", "B) Uniforme", "C) Binomial", "D) Poisson"], "correta": "B"},
    {"pergunta": "O desvio padrão mede:", "opcoes": ["A) Tendência central", "B) Grau de dispersão", "C) Probabilidade", "D) Frequência"], "correta": "B"},
    {"pergunta": "Qual destas NÃO é uma medida de tendência central?", "opcoes": ["A) Média", "B) Moda", "C) Variância", "D) Mediana"], "correta": "C"},
    {"pergunta": "Em um histograma, a área total representa:", "opcoes": ["A) Média", "B) Frequência total", "C) Probabilidade total", "D) Mediana"], "correta": "C"},
    {"pergunta": "Quando a média é maior que a mediana, a distribuição tende a ser:", "opcoes": ["A) Simétrica", "B) Assimétrica à esquerda", "C) Assimétrica à direita", "D) Normal"], "correta": "C"},
    {"pergunta": "O Teorema Central do Limite afirma que:", "opcoes": ["A) Toda variável é normal", "B) Médias amostrais tendem à normalidade", "C) A variância é sempre constante", "D) A moda é igual à mediana"], "correta": "B"},
    {"pergunta": "Probabilidade de evento impossível é:", "opcoes": ["A) 1", "B) 0", "C) 0,5", "D) Depende da amostra"], "correta": "B"},
]
 
perguntas_ml = [
    {"pergunta": "O que é overfitting?", "opcoes": ["A) Modelo que generaliza bem", "B) Modelo que aprende ruído do treino", "C) Modelo que não aprende nada", "D) Nenhuma das anteriores"], "correta": "B"},
    {"pergunta": "Qual algoritmo é usado em classificação?", "opcoes": ["A) KNN", "B) Regressão Linear", "C) PCA", "D) K-means"], "correta": "A"},
    {"pergunta": "O que significa 'supervisionado' em Machine Learning?", "opcoes": ["A) Sem rótulos", "B) Com rótulos", "C) Autoaprendizado", "D) Nenhuma das anteriores"], "correta": "B"},
    {"pergunta": "Qual técnica reduz dimensionalidade?", "opcoes": ["A) SVM", "B) PCA", "C) Regressão logística", "D) Árvore de decisão"], "correta": "B"},
    {"pergunta": "Na regressão linear, o erro é medido pela:", "opcoes": ["A) Soma dos quadrados dos resíduos", "B) Moda", "C) Desvio padrão", "D) Acurácia"], "correta": "A"},
    {"pergunta": "O que é regularização?", "opcoes": ["A) Técnica para aumentar overfitting", "B) Reduz complexidade do modelo", "C) Melhorar gráficos", "D) Aumentar dimensionalidade"], "correta": "B"},
    {"pergunta": "Qual destes é um algoritmo NÃO supervisionado?", "opcoes": ["A) Regressão logística", "B) SVM", "C) K-means", "D) Random Forest"], "correta": "C"},
    {"pergunta": "O que significa 'feature' em Machine Learning?", "opcoes": ["A) O alvo a ser previsto", "B) Uma variável de entrada", "C) O erro do modelo", "D) O parâmetro de ajuste"], "correta": "B"},
    {"pergunta": "Qual métrica é usada em classificação binária?", "opcoes": ["A) Acurácia", "B) R²", "C) Erro quadrático médio", "D) Nenhuma das anteriores"], "correta": "A"},
    {"pergunta": "Em redes neurais, a função que introduz não-linearidade é chamada de:", "opcoes": ["A) Função de ativação", "B) Função de perda", "C) Função de custo", "D) Função de otimização"], "correta": "A"},
]
 
# -------------------------
# Criação do PDF
# -------------------------
pdf = canvas.Canvas("respostas_IA.pdf", pagesize=A4)
pdf.setTitle("Perguntas e Respostas sobre Estatística e Machine Learning")
 
largura, altura = A4
x = 3*cm
y = altura - 3*cm
 
# Título
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(x, y, "Perguntas e Respostas sobre IA, Estatística e Machine Learning")
pdf.line(x, y-0.2*cm, largura - 3*cm, y-0.2*cm)
y -= 1.2*cm
 
# -------------------------
# Seção 1: Estatística
# -------------------------
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(x, y, "📊 Estatística")
y -= 0.8*cm
 
pdf.setFont("Helvetica", 11)
for i, q in enumerate(perguntas_estat, 1):
    if y < 4*cm:
        pdf.showPage()
        pdf.setFont("Helvetica", 11)
        y = altura - 3*cm
    pdf.drawString(x, y, f"{i}. {q['pergunta']}")
    y -= 0.6*cm
    for opcao in q["opcoes"]:
        pdf.drawString(x + 0.7*cm, y, opcao)
        y -= 0.5*cm
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(x + 0.7*cm, y, f"✔ Resposta correta: {q['correta']}")
    pdf.setFont("Helvetica", 11)
    y -= 1.0*cm
 
# -------------------------
# Seção 2: Machine Learning
# -------------------------
pdf.setFont("Helvetica-Bold", 14)
pdf.drawString(x, y, "🤖 Machine Learning")
y -= 0.8*cm
 
for i, q in enumerate(perguntas_ml, 1):
    if y < 4*cm:
        pdf.showPage()
        pdf.setFont("Helvetica", 11)
        y = altura - 3*cm
    pdf.drawString(x, y, f"{i}. {q['pergunta']}")
    y -= 0.6*cm
    for opcao in q["opcoes"]:
        pdf.drawString(x + 0.7*cm, y, opcao)
        y -= 0.5*cm
    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(x + 0.7*cm, y, f"✔ Resposta correta: {q['correta']}")
    pdf.setFont("Helvetica", 11)
    y -= 1.0*cm
 
# Rodapé
pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(3*cm, 2*cm, "")
 
# Salvar o PDF
pdf.save()
 
# -------------------------
# Abrir o PDF automaticamente
# -------------------------
nome_pdf = "respostas_IA.pdf"
if platform.system() == "Windows":
    os.startfile(nome_pdf)
elif platform.system() == "Darwin":
    os.system(f"open '{nome_pdf}'")
else:
    os.system(f"xdg-open '{nome_pdf}'")