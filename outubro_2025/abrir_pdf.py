import os 
def abrir_pdf(caminho): 
    try: 
        os.startfile(caminho) 
    except Exception as e: 
        print(f"Erro ao abrir o arquivo {caminho}: {e}")

# Exemplo: abrir um PDF chamado "documento.pdf" na pasta Documentos 
abrir_pdf("C:\Users\Jeferson\Documents\documento.pdf") 