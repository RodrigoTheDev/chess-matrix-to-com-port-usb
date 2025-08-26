import os
import time
import serial
from dotenv import load_dotenv

load_dotenv()

baud = int(os.getenv("BAUD_RATE", 9600))

# Pegar as portas
com1 = os.getenv("COM1")
com2 = os.getenv("COM2")
com3 = os.getenv("COM3")
com4 = os.getenv("COM4")

# Conectar em cada porta
s1 = serial.Serial(com1, baud, timeout=1); time.sleep(2)
s2 = serial.Serial(com2, baud, timeout=1); time.sleep(2)
s3 = serial.Serial(com3, baud, timeout=1); time.sleep(2)
s4 = serial.Serial(com4, baud, timeout=1); time.sleep(2)

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
