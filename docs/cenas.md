Quando um utilizador é criado, gerada uma pasta com um UUID automaticamente gerado, por exemplo: 
  uploads/123e4567-e89b-12d3-a456-426614174000

Quando um utilizador carrega um ficheiro, o ficheiro é guardado na pasta do utilizador, por exemplo:
  uploads/123e4567-e89b-12d3-a456-426614174000/ficheiro.csv

O utilizador pode então criar um quarter, que é uma pasta com um nome, por exemplo:
  uploads/123e4567-e89b-12d3-a456-426614174000/quarter1

O utilizador pode então adicionar ficheiros ao quarter, que são guardados na pasta do quarter, por exemplo:
  uploads/123e4567-e89b-12d3-a456-426614174000/quarter1/ficheiro.csv


Cada quarter é local ao utilizador, e só o utilizador pode ver o seu quarter.
Esta gestão é feita no UI, e é feita através de uma API.
