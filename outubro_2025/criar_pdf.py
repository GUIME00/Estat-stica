from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import os
import platform
 
# Nome do arquivo PDF
nome_pdf = "arquivo.pdf"
 
# Criação do PDF
pdf = canvas.Canvas(nome_pdf, pagesize=A4)
 
# ========================
# 🎓 Cabeçalho
# ========================
pdf.setFont("Helvetica-Bold", 18)
pdf.drawString(3*cm, 27*cm, "O Uso da Inteligência Artificial no Ensino Personalizado")
 
# Linha decorativa
pdf.line(3*cm, 26.8*cm, 17*cm, 26.8*cm)
 
# Subtítulo
pdf.setFont("Helvetica-Oblique", 12)
pdf.drawString(3*cm, 25.5*cm, "Como a tecnologia está transformando a forma de aprender e ensinar")
 
# ========================
# 🧠 Corpo do texto
# ========================
pdf.setFont("Helvetica", 12)
 
texto = [
    "",
    "A Inteligência Artificial (IA) tem se tornado uma aliada poderosa na educação moderna, permitindo que o ensino",
    "seja adaptado às necessidades específicas de cada estudante. Em vez de um modelo único para todos, a IA analisa",
    "o desempenho, o ritmo e as preferências individuais, criando experiências de aprendizado personalizadas.",
    "",
    "Por exemplo, plataformas de ensino online utilizam algoritmos que identificam as dificuldades de um aluno e",
    "sugerem conteúdos complementares ou exercícios direcionados. Isso torna o aprendizado mais eficiente e evita que",
    "estudantes fiquem desmotivados por não acompanhar o ritmo da turma.",
    "",
    "Além disso, professores podem contar com relatórios inteligentes que indicam quais alunos precisam de mais apoio,",
    "permitindo intervenções pedagógicas mais precisas e humanizadas. A IA não substitui o educador, mas o auxilia,",
    "tornando o processo de ensino-aprendizagem mais inclusivo e adaptativo.",
    "",
    "Em ambientes corporativos e universitários, a IA também é usada para criar trilhas de aprendizado personalizadas,",
    "de acordo com as metas e interesses de cada indivíduo, promovendo o desenvolvimento contínuo.",
    "",
    "Reflexão Final:",
    "O ensino personalizado impulsionado pela Inteligência Artificial representa um avanço significativo na educação.",
    "No entanto, é essencial garantir o uso ético desses sistemas, respeitando a privacidade e promovendo a equidade no",
    "acesso à tecnologia, para que todos possam se beneficiar desse novo modelo de aprendizagem."
]
 
# Escrevendo o texto no PDF
x = 3*cm
y = 24*cm
for linha in texto:
    pdf.drawString(x, y, linha)
    y -= 0.7*cm  # espaçamento entre linhas
 
# ========================
# 💬 Rodapé
# ========================
pdf.setFont("Helvetica-Oblique", 10)
pdf.drawString(3*cm, 2*cm, "")
 
# Salvar o PDF
pdf.save()
 
# ========================
# 📂 Abrir o PDF automaticamente
# ========================
if platform.system() == "Windows":
    os.startfile(nome_pdf)
elif platform.system() == "Darwin":  # macOS
    os.system(f"open '{nome_pdf}'")
else:  # Linux
    os.system(f"xdg-open '{nome_pdf}'")