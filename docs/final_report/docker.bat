:: Run this with powershell
docker build -t alicescfernandes/compiler_image:latest .
docker push alicescfernandes/compiler_image:latest
docker run --rm -v "$(pwd):/data" -w /data alicescfernandes/compiler_image:latest