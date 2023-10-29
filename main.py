import CTR

def options():
  print('------------- AES -------------')
  print('1 - Cifrar arquivo com ECB')
  print('2 - Decifrar arquivo com ECB')
  print('3 - Sair')
  print('-------------------------------')
  return input("> ")

# B7msLxzo

def main():
  while True:
    option = options()
    if option == '1':
      file = input("Arquivo da imagem (ex. foto.png): ")
      rounds = int(input("Numero de rodadas: "))
      key = input("Chave: ")
      key = key[:16].ljust(16, '\x00')
      CTR.Encrypt(file, rounds, bytes(key, 'ascii'))
    elif option == '2':
      file = input("Arquivo da imagem (ex. foto.png): ")
      rounds = int(input("Numero de rodadas: "))
      key = input("Chave: ")
      key = key[:16].ljust(16, '\x00')
      CTR.Decrypt(file, rounds, bytes(key, 'ascii'))
    else:
      break

main()
