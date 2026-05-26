import pywhatkit as kit
import pyautogui
import time

numero = "+50377297050"
mensaje = "Hola, este es un mensaje automático"

for i in range(3):
    kit.sendwhatmsg_instantly(numero, mensaje, wait_time=20, tab_close=False)
    
    print("Esperando que cargue WhatsApp...")
    time.sleep(10)  # 🔥 más tiempo
    
    pyautogui.press("enter")
    print(f"Mensaje {i+1} enviado")
    
    if i < 2:
        time.sleep(120)

        