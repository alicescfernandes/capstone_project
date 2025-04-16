FROM texlive/texlive:latest

RUN tlmgr update --self && \
    tlmgr install \
        latexmk \
        glossaries \
        xfor \
        mfirstuc \
        datatool \
        tracklang

# Define o ponto de montagem

WORKDIR /data

CMD ["pdflatex", "data/00_PRJ_main.tex"]
