import string
import random
import cv2

import AES

def JoinBlocks(blocks, image):
  cnt = 0
  aux = image
  for i in range(image.shape[0]):
    for j in range(image.shape[1]):
      for k in range(image.shape[2]):
        aux[i][j][k] = blocks[cnt]
        cnt += 1
  return aux

def CreateBlock(image):
  block = [image[i][j][k] for i in range(image.shape[0]) for j in range(image.shape[1]) for k in range(image.shape[2])]
  block.extend([0] * (16 - len(block) % 16))
  return block

def SplitBlock(block):
  return [[block[i+j] for i in range(16)] for j in range(0, len(block), 16)]

def GetPlainText(nonce, count):
  s = nonce + str(count).zfill(8)
  b = bytes(s, 'ascii')
  return [b[i] for i in range(16)]

def RandomNonce():
  return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = 8))

def Encrypt(file, rounds, key):
  key = key[:16]

  image = cv2.imread(file)
  cv2.imshow("Imagem original", image)
  cv2.waitKey(0)

  print("Cifrando imagem utilizado método CTR...")

  nonce = RandomNonce()
  print("Nonce utilizado:", nonce)

  block = SplitBlock(CreateBlock(image))
  res = []
  for i in range(len(block)):
    text = GetPlainText(nonce, i)
    aux = AES.Encrypt(rounds, text, key)
    res.extend(AES.MakeXor(aux, block[i]))
  res = JoinBlocks(res, image)

  print("Imagem cifrada salva como 'cifrada.png'")
  cv2.imwrite("cifrada.png", res)
  cv2.imshow("Imagem cifrada", res)
  cv2.waitKey(0)

  cv2.destroyAllWindows()

def Decrypt(file, rounds, key):
  key = key[:16]

  nonce = input("Nonce: ")

  image = cv2.imread(file)
  cv2.imshow("Imagem original cifrada", image)
  cv2.waitKey(0)

  print("Decifrando imagem utilizado método CTR...")
  block = SplitBlock(CreateBlock(image))

  res = []
  for i in range(len(block)):
    aux = GetPlainText(nonce, i)
    aux = AES.Encrypt(rounds, aux, key)
    res.extend(AES.MakeXor(aux, block[i]))
  res = JoinBlocks(res, image)

  print("Imagem decifrada salva como 'decifrada.png'")
  cv2.imwrite("decifrada.png", res)
  cv2.imshow("Imagem decifrada", res)
  cv2.waitKey(0)

  cv2.destroyAllWindows() 
