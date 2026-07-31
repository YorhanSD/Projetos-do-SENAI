aluno = ["bruno", "marcos", "stefany"]
if "bruno" in aluno:
   print("O aluno está na lista!")
else:
   print("O alunio não está na lista!")

print("="*20)

aluno = {
   "nome": "Bruno",
   "idade": 18,
   "curso": "Python"
}

if "curso" in aluno:
   print(aluno["curso"])
else:
   print("O aluno não está matriculado")

if "profissão" in aluno:
   print(aluno["profissão'"])
else:
   print("Não existe")

print("="*20)

for chave in aluno:
   print(chave)

for valor in aluno.values():
   print(valor)

for chave, valor in aluno.items():
   print(chave, valor)

print(aluno)