# docker run --rm -v $(pwd):/data texlive/texlive pdflatex data/00_PRJ_main.tex


# docker build -t my-latex-image .
# docker run --rm -v $(pwd):/data my-latex-image

# PS
docker build -t pdflatex .
docker run --rm -it -v "${PWD}:/data" -w /data pdflatex sh


# docker build --no-cache -t your-image-name .