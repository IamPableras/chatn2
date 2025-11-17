nome = input("Qual é o seu nome? ")
idade = int(input("Quantos anos você tem? "))

print(f"Olá, {nome}! Você tem {idade} anos.")

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")