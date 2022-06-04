def caesar_encrypt():
    cipher_txt = ''
    txt = input('Введите текст который надо зашифровать.\n:')
    while True:
        step = input('На какой шаг(вправо) надо смещать буквы?\nПравильный шаг для русского алфавита от 1 до 32 (без буквы ё)\n               для английского от 1 до 26\n:')
        if step.isdigit():
            step = int(step)     
            break
        print("Некорректный ввод")
    for sym in txt:
        if 65 <= ord(sym) <= 90:     
            cipher_txt += chr((ord(sym) - 65 + step%26)%26 + 65)
        elif 97 <= ord(sym) <= 122:
            cipher_txt += chr((ord(sym) - 97 + step%26)%26 + 97)
        elif 1040 <= ord(sym) <= 1071:  
            cipher_txt += chr((ord(sym) - 1040 + step%32)%32 + 1040)
        elif 1072 <= ord(sym) <= 1103: 
            cipher_txt += chr((ord(sym) - 1072 + step%32)%32 + 1072)  
        else:
            cipher_txt += sym
    print(cipher_txt)
    
def caesar_decrypt():
    cipher_txt = ''
    txt = input('Введите текст который надо дешифровать.\n:')
    while True:
        step = input('На какой шаг(влево) надо смещать буквы?\n:')
        if step.isdigit():
            step = int(step)
            break
        print("Некорректный ввод")
    for sym in txt:
        if 65 <= ord(sym) <= 90:
            if ord(sym) - int(step)%26 < 65:
                cipher_txt += chr(ord(sym) - step%26 +26)
            else:
                cipher_txt += chr(ord(sym) - step%26)       
        elif 97 <= ord(sym) <= 122:
            if ord(sym) - int(step)%26 < 97:
                cipher_txt += chr(ord(sym) - step%26 +26)
            else:
                cipher_txt += chr(ord(sym) - step%26)       
        elif 1040<= ord(sym) <= 1071:  
            if ord(sym) - int(step)%32 < 1040:
                cipher_txt += chr(ord(sym) - step%32 +32)
            else:
                cipher_txt += chr(ord(sym) - step%32)              
        elif 1072<= ord(sym) <= 1103: 
            if ord(sym) - int(step)%32 < 1072:
                cipher_txt += chr(ord(sym) - step%32 +32)
            else:
                cipher_txt += chr(ord(sym) - step%32)               
        else:
            cipher_txt += sym
    print(cipher_txt)

def caesar_list():  
    txt = input('Введите текст который надо дешифровать.\n:')
    for step in range(1,33):
        cipher_txt = ""
        for sym in txt:
            if 65 <= ord(sym) <= 90:
                if ord(sym) - int(step)%26 < 65:
                    cipher_txt += chr(ord(sym) - step%26 +26)
                else:
                    cipher_txt += chr(ord(sym) - step%26)       
            elif 97 <= ord(sym) <= 122:
                if ord(sym) - int(step)%26 < 97:
                    cipher_txt += chr(ord(sym) - step%26 +26)
                else:
                    cipher_txt += chr(ord(sym) - step%26)       
            elif 1040<= ord(sym) <= 1071:  
                if ord(sym) - int(step)%32 < 1040:
                    cipher_txt += chr(ord(sym) - step%32 +32)
                else:
                    cipher_txt += chr(ord(sym) - step%32)              
            elif 1072<= ord(sym) <= 1103: 
                if ord(sym) - int(step)%32 < 1072:
                    cipher_txt += chr(ord(sym) - step%32 +32)
                else:
                    cipher_txt += chr(ord(sym) - step%32)               
            else:
                cipher_txt += sym
        print(cipher_txt) 

  


print('      Вас приветствует программа\n    шифрования и дешифрования текста\n         по алгоритму Цезаря\n\nЧем будем сегодня заниматься?')

while True:
    answer = input('введите "e" - если будем зашифровывать текст(сдвиг вправо)\nвведите "d" - если будем дешифровывать текст(сдвиг влево)\nвведите "s" - если будем дешифровывать не зная ключа (выведет 32 строки со двигом на 1)\n:').lower().strip()
    if answer == 'e' or answer == 'е':
        caesar_encrypt()
        exit = input('\nВведите "exit" если хотите выйти из программы\n')
        if exit == 'exit':
            break       
    elif answer == 'd':
        caesar_decrypt()  
        exit = input('\nВведите "exit" если хотите выйти из программы\n')
    elif answer == 's':
        caesar_list()  
        exit = input('\nВведите "exit" если хотите выйти из программы\n')
        if exit == 'exit':
            break       
    else:
        print("Некорректный ввод")
