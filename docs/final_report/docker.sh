# Run this with powershell
docker build -t pdflatex .
docker run --rm -v "$(pwd):/data" -w /data pdflatex
