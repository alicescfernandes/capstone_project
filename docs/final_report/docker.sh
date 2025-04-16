# Run this with powershell
docker build -t compiler_image .
docker run --rm -v "$(pwd):/data" -w /data compiler_image

# docker run --rm -it -v "${PWD}:/data" -w /data compiler_image sh