import os
import time
import serial
from dotenv import load_dotenv

load_dotenv()

baud = int(os.getenv("BAUD_RATE", 9600))

# Pegar as portas
COM_A = os.getenv("COM_A")
COM_B = os.getenv("COM_B")
COM_C = os.getenv("COM_C")
COM_D = os.getenv("COM_D")

# Conectar em cada porta
s1 = serial.Serial(COM_A, baud, timeout=1); time.sleep(2)
s2 = serial.Serial(COM_B, baud, timeout=1); time.sleep(2)
s3 = serial.Serial(COM_C, baud, timeout=1); time.sleep(2)
s4 = serial.Serial(COM_D, baud, timeout=1); time.sleep(2)

# Enviar "hello world" em cada
msg = "hello world\n".encode("utf-8")
s1.write(msg)
s2.write(msg)
s3.write(msg)
s4.write(msg)

print("Mensagens enviadas.")

# Fechar
s1.close()
s2.close()
s3.close()
s4.close()
