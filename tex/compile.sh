 #!/bin/bash

echo "Compiling LaTeX document..."

# Define TeX Live paths
TEXLIVE_BIN="/c/texlive/2025/bin/win32"

# Run pdflatex first time
"$TEXLIVE_BIN/pdflatex.exe" 00_PRJ_main.tex

# Run bibtex for bibliography
"$TEXLIVE_BIN/bibtex.exe" 00_PRJ_main

# Run pdflatex twice more to resolve references
"$TEXLIVE_BIN/pdflatex.exe" 00_PRJ_main.tex
"$TEXLIVE_BIN/pdflatex.exe" 00_PRJ_main.tex

echo "Compilation complete!"