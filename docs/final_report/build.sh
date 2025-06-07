# Save with LF line endings
rm build -rf
mkdir -p build

cp XBib.bib build/
cp apalikeMy.bst build/

pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex

makeglossaries -d build 00_PRJ_main
bibtex build/00_PRJ_main

pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex
pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex


mv build/00_PRJ_main.pdf build/final_report.pdf

# rm final_report.pdf
# mv build/00_PRJ_main.pdf final_report.pdf
