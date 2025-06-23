# Save with LF line endings
mkdir -p build

cp XBib.bib build/
cp apalikeMy.bst build/

pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex

makeglossaries -d build 00_PRJ_main
bibtex build/00_PRJ_main

pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex
pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex
pdflatex --interaction=nonstopmode -output-directory=build 00_PRJ_main.tex

mv build/00_PRJ_main.pdf final_report.pdf
rm -rf build