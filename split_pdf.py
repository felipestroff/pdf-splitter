import fitz # PyMuPDF
import os
import sys

def split_pdf(input_pdf, output_folder, pages_per_part):
    """
    Divide um arquivo PDF em várias partes menores.

    :param input_pdf: caminho do arquivo PDF original
    :param output_folder: pasta onde os pedaços serão salvos
    :param pages_per_part: número de páginas por cada parte
    """
    
    # Cria a pasta de saída caso não exista
    os.makedirs(output_folder, exist_ok=True)

    # Abre o PDF original
    doc = fitz.open(input_pdf)
    total_pages = len(doc)
    part = 1

    # Itera em blocos de páginas
    for i in range(0, total_pages, pages_per_part):
        new_doc = fitz.open()
        
        # Copia páginas do PDF original para o novo PDF
        new_doc.insert_pdf(
            doc,
            from_page=i,
            to_page=min(i + pages_per_part - 1, total_pages - 1)
        )
        
        # Define o nome da parte e salva na pasta de saída
        output_file = os.path.join(output_folder, f"part_{part}.pdf")
        new_doc.save(output_file)
        new_doc.close()
        
        print(f"Parte {part} salva: {output_file}")
        part += 1

    # Fecha o PDF original
    doc.close()
    print("✅ Divisão concluída!")


if __name__ == "__main__":
    # Verifica argumentos
    if len(sys.argv) < 4:
        print("Uso: python split_pdf.py <arquivo_pdf> <pasta_saida> <paginas_por_parte>")
        sys.e
