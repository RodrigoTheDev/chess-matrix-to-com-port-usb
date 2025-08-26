import os
import time
import serial
import sys
from dotenv import load_dotenv
from moveParser import parse_move
from matrix import matrix

load_dotenv()

move = None
if len(sys.argv) > 1:
    move = sys.argv[1]  

parsed = parse_move(move)
print(parsed)

baud = int(os.getenv("BAUD_RATE", 9600))

COM_A = os.getenv("COM_A")
COM_B = os.getenv("COM_B")

try:
    serial_A = serial.Serial(COM_A, baud, timeout=1); time.sleep(2)
    serial_B = serial.Serial(COM_B, baud, timeout=1); time.sleep(2)
except:
    print("Portas seriais não conectadas... prosseguindo sem enviar dados.")


serial_A_text = f"{matrix[parsed[0]-1][parsed[1]-1][0]}, {matrix[parsed[0]-1][parsed[1]-1][2]}".encode()
print(serial_A_text)

serial_B_text = f"{matrix[parsed[2]-1][parsed[3]-1][1]}, {matrix[parsed[2]-1][parsed[3]-1][3]}".encode()
print(serial_B_text)

try:
    serial_A.write(serial_A_text) # type: ignore
    serial_B.write(serial_B_text) # type: ignore
except:
    print("os dados não foram enviados")

print("Mensagens enviadas.")

# Fechar
try:
    serial_A.close() # type: ignore
    serial_B.close() # type: ignore
except:
    print("as portas não foram fechadas")
