import time
import pyupm_i2clcd

RET_ERROR = -1

if __name__ == '__main__':
    lcd = pyupm_i2clcd.Jhd1313m1(1, 0x3E, 0x62)
    lcd.setColor(255, 0, 0) # RED
    lcd.write('RED')
    time.sleep(10)
    lcd = pyupm_i2clcd.Jhd1313m1(1, 0x3E, 0x62)
    lcd.setColor(0, 255, 0) # GREEN
    lcd.write('GREEN')
    time.sleep(10)
    lcd = pyupm_i2clcd.Jhd1313m1(1, 0x3E, 0x62)
    lcd.setColor(0, 0, 255) # BLUE
    lcd.write('BLUE')
    time.sleep(10)
