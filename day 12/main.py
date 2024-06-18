# membuat game algoritma hangman menggunakan bahasa pemerograman python
import random 

def get_random_word(word_list):
    return random.choice(word_list)

def display_current_progress(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def  play_hangman():
    word_list = ["python", "java", "kotlin", "javascript"]
    word = get_random_word(word_list)
    guessed_letters = []
    attempts = 6
    guessed = False
    
    print("Selamat datang di permainan Hangman!")
    print("_" * len(word))
    
    while not guessed and attempts > 0:
        guess = input("Masukkan huruf yang ingin diperiksa: ").lower()
        
        if guess in guessed_letters:
            print("Anda telah menekan huruf ini sebelumnya. Silakan coba lagi.")
        elif guess not in word:
            print(f"Maaf, '{guess}' bukan huruf yang diperiksa. Coba lagi.")
            attempts -= 1
            guessed_letters.append(guess)
        else:
            print(f"Selamat, '{guess}' adalah huruf yang diperiksa.")
            guessed_letters.append(guess)
        
        display = display_current_progress(word, guessed_letters)
        print(display)
        
        if display == word:
            guessed = True
    else:
        print("Tebak tidak valid")
    
    print(display_current_progress(word, guessed_letters))
    print("Susa percobaan", attempts)
    
    if guessed:
        print("Selamat anda berhasil menebak kata!", word)
    else :
        print("Maaf, anda gagal menebak kata. Kata yang diperiksa adalah", word)

if __name__ == "__main__":
    play_hangman()    