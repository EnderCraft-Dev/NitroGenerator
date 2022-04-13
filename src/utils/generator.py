import string 
import random 

def generate_code(links):
    char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    code_len = 16
    base_url = "https://discord.gift/"
    final_code = ""

    code_list = []

    for link in range(links):
        final_code = base_url+"".join(random.choice(char_list) for char in range(code_len))
        code_list.append(final_code)
    
    return(code_list)

if __name__=="__main__":
    generate_code()