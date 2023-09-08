'''
Number to LCD kata app
'''

from lcd.lcd import LCD

def main():
    '''
    Thin layer to exercise LCD class
    '''
    cut = LCD()
    lcd_number = cut.gen_lcd_number(1234567890)
    print(lcd_number)

if __name__ == "__main__":
    main()
