import pyupm_i2clcd as lcd  # importa biblioteca para i2c 

import time,os # importa biblioteca de tempo e os para sistema operacional

Lcd = lcd.Jhd1313m1(0, 0x3E, 0x62) # Cria uma variavel para usar o display
Lcd.clear() 
Lcd.setColor(255, 255, 0)  # Seta cor verde
Lcd.setCursor(0,0) 

ip = ((os.popen("ifconfig wlan0").read()).split("\n")[1]).split(" ")[11].split("addr:")[1] 
 
Lcd.write(ip) 
time.sleep(10) 
