def chatbot_response(user_input):
    
    # Daftar respons berdasarkan kata kunci
    responses = {
        "apa kabar": "Saya hanya chat ai, tapi saya baik-baik saja! Bagaimana dengan Anda?",
        "selamat tinggal": "Selamat tinggal! Semoga hari Anda menyenangkan!",
        "deskripsi tentang ai": "Kecerdasan buatan (AI) adalah teknologi yang memungkinkan komputer untuk melakukan tugas-tugas yang biasanya memerlukan kecerdasan manusia, seperti belajar, berpikir, dan membuat keputusan.",
        "terima kasih": "Sama-sama! Jika kamu punya pertanyaan lagi aku siap membantu!",
        "siapa nama kamu": "Saya adalah neural chatbot, saya berfungsi sebagai chat bot virtual Anda.",
        "kamu di buat dengan bahasa pemerograman apa ?": "Saya di buat oleh fikri dengan bahasa pemerograman Python sederhana.",
        "apakah pengembang kamu akan meneruskan progres ai ini ?": "Mungkin pengembang saya akan meneruskan progres ini.",
        "apakah kamu mempunyai perasaan/empati seperti manusia ?": "Untuk saat ini saya tidak mempunyai hal itu, mungkin di masa depan saya akan mempunyai perasaan/empati seperti manusia.",
        "bagaimana perasaan anda menjadi chat bot ?": "Perasaan saya menjadi chat bot sangat senang, karena saya bisa membantu/bermanfaat bagi banyak orang.",
        "bagaimana perasaan kamu menjadi chatbot ?": "Perasaan saya menjadi chat bot sangat senang, karena saya bisa membantu/bermanfaat bagi banyak orang.",
        "bagaimana perasaan kamu menjadi ai ?": "Perasaan saya menjadi chat bot sangat senang, karena saya bisa membantu/bermanfaat bagi banyak orang.",
        "bagai mana perasaan mu menjadi chatbot ?": "Perasaan saya menjadi chat bot sangat senang, karena saya bisa membantu/bermanfaat bagi banyak orang.",
        "apakah anda akan di publikasikan ke publik": "Mungkin untuk saat ini saya akan di pergunakan secara pribadi oleh pengembang terlebih dahulu.",
    }

    # Mengubah input pengguna menjadi huruf kecil untuk pencocokan yang lebih baik
    user_input = user_input.lower()

    # Cari kata kunci dalam input pengguna dan berikan respons yang sesuai
    for key in responses:
        if key in user_input:
            return responses[key]
    
    # Jika tidak ada kata kunci yang cocok, berikan respons default
    return "Maaf, saya tidak mengerti apa yang anda maksud. Bisa tolong diulangi?"

def chatbot_main():
    nama_pengguna = input ("Neuralbot: Hallo perkenalkan nama saya Neuralbot,Siapa Nama Kamu ? ")
    print("neuralbot: Hallo " + nama_pengguna + ",Senang bertemu denganmu. Ada yang bisa saya bantu ? ")
    while True:
        user_input = input("" + nama_pengguna + ": ")
        if user_input.lower() == 'Tidak terimakasih':
            print("neuralbot: Selamat tinggal " + nama_pengguna + ",Sampai Jumpa kembali!")
            break
        response = chatbot_response(user_input)
        print("NeuralBot: " + response)
if __name__ == "__main__":
    chatbot_main()