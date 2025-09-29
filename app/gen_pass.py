import pyperclip  # noqa: E402
import string  # noqa: E402
import secrets  # noqa: E402

#                                          ДЛЯ ГЕНЕРАЦИИ 1 ПАРОЛЯ
def gen_pass(length: int = 16):
    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    punctuation = string.punctuation


    # обязательный минимум
    password_chars = [
        secrets.choice(digits),
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(punctuation),
    ]

    # добор символов до length
    all_chars = digits + lowercase + uppercase + punctuation
    password_chars += [secrets.choice(all_chars) for _ in range(length - len(password_chars))]
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


pwd = gen_pass() #Один пароль на все функции


def copy_to_clipboard(): # КОПИРОВАНИЕ В БУФЕР ОБМЕНА
    pyperclip.copy(pwd)
    print(f"Пароль сгенерированый в буфер обмена: {pwd}")


def write_in_file(file_path = "Gen_pas.txt"): #ЗАПИСАТЬ В ФАЙЛ
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(pwd + "\n")
    print(f"Пароль записанный в файл: {pwd}")

if __name__ == "__main__":
    copy_to_clipboard()
    write_in_file()
