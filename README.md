# 📑 PDF Splitter (PyMuPDF)

Este projeto utiliza a biblioteca [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/) para **dividir arquivos PDF grandes** em várias partes menores, facilitando o manuseio e compartilhamento.

## 🚀 Funcionalidade
- Aceita qualquer PDF (em qualquer pasta).
- Permite definir:
  - 📂 pasta de saída
  - 📄 quantidade de páginas por parte
- Cria automaticamente a pasta de saída se não existir.
- Gera arquivos `part_1.pdf`, `part_2.pdf`, etc.

## 📦 Requisitos
- Python 3.8 ou superior
- Biblioteca [PyMuPDF](https://pypi.org/project/PyMuPDF/)

## 🔧 Instalação

Clone este repositório:

```bash
git https://github.com/felipestroff/pdf-splitter.git
cd pdf-splitter
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instale a dependência:

```bash
pip install PyMuPDF
```

## #️ Uso

Execute o script passando 3 argumentos:

```bash
python split_pdf.py <arquivo_pdf> <pasta_saida> <paginas_por_parte>
```

### Exemplos:

PDF na mesma pasta:

```bash
python split_pdf.py meu_arquivo.pdf saida 1000
```
➡️ Divide meu_arquivo.pdf em partes de 1000 páginas, salva em ./saida/.

PDF em subpasta:

```bash
python split_pdf.py docs/meu_arquivo.pdf partes 500
```
➡️ Divide docs/meu_arquivo.pdf em partes de 500 páginas, salva em ./partes/.

PDF em outro diretório:

```bash
python split_pdf.py "C:/Users/Usuario/Documents/livro.pdf" pdf_split 200
```
➡️ Divide livro.pdf em partes de 200 páginas, salva em ./pdf_split/.

### 📂 Exemplo de saída
```bash
Parte 1 salva: pdf_dividido/part_1.pdf
Parte 2 salva: pdf_dividido/part_2.pdf
Parte 3 salva: pdf_dividido/part_3.pdf
Divisão concluída!
```

## ⚙️ Configurações

- input_pdf → informe o caminho completo ou relativo do PDF.
- output_folder → será criada automaticamente.
- pages_per_part → define o número de páginas em cada parte.