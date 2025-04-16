FROM texlive/texlive:latest

RUN tlmgr update --self && \
    tlmgr install \
        latexmk \
        glossaries \
        xfor \
        mfirstuc \
        datatool \
        tracklang \
        biblatex \
        biber

# Define o ponto de montagem

WORKDIR /data

CMD ["sh", "build.sh"]
