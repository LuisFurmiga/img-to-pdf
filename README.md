
# Conversor de Imagens para PDF

Este é um aplicativo Python com uma interface gráfica (GUI) para converter várias imagens em um único PDF. Os usuários podem organizar, adicionar, remover e redimensionar imagens para se ajustar ao formato A4 antes de exportar.

## Funcionalidades
- Adicionar vários arquivos de imagem (`.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff`).
- Organizar as imagens na ordem desejada (mover para cima/baixo).
= Redimensionar imagens automaticamente para caber em uma página A4.
= Exportar as imagens selecionadas como um único arquivo PDF.

## Requisitos
Todas as dependências estão listadas no arquivo requirements.py. Para instalá-las, utilize:
```sh
python requirements.py
```

## Uso
1. Execute o script: python img-to-pdf.py.
2. Use os botões na interface gráfica para adicionar, organizar ou remover imagens.
3. Exporte para PDF selecionando uma pasta de destino.

## Notas
- O arquivo PDF gerado será nomeado com base na primeira imagem selecionada.
- As imagens são redimensionadas para se ajustarem às dimensões de uma página A4 (300 DPI).
