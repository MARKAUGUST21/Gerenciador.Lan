from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def gerar_relatorio_pdf(tabela, dados):
    # Nome e caminho do arquivo PDF
    nome_arquivo = f"relatorio_{tabela}.pdf"
    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)

    # Cria o objeto canvas com tamanho A4
    c = canvas.Canvas(caminho, pagesize=A4)
    largura, altura = A4

    # Título
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, altura - 50, f"Relatório de Ativos - {tabela}")

    # Cabeçalho das colunas
    c.setFont("Helvetica-Bold", 10)
    y = altura - 80
    colunas = ("ID", "Tipo", "Nome", "Especificações", "Valor", "Estado", "Data de Aquisição", "Vida Útil", "Status")
    linha_colunas = " | ".join(colunas)
    c.drawString(50, y, linha_colunas)
    y -= 15

    # Dados das linhas
    c.setFont("Helvetica", 9)
    for ativo in dados:
        linha = " | ".join(str(campo) for campo in ativo)

        # Garante que não ultrapasse a margem inferior
        if y < 50:
            c.showPage()
            c.setFont("Helvetica", 9)
            y = altura - 50

        c.drawString(50, y, linha)
        y -= 15

    # Salva o PDF
    c.save()
    print(f"Relatório gerado: {caminho}")