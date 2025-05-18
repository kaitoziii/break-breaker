from db import init_db
from auth import login, register
import game
import leaderboard

def main():
    init_db()

    print("1. Login\n2. Register")
    choice = input("Pilih: ")

    username = input("Username: ")
    password = input("Password: ")

    if choice == '1':
        user = login(username, password)
        if user:
            print("Login berhasil!")
            user_id = user[0]
            game.start(user_id)
        else:
            print("Login gagal.")
    elif choice == '2':
        if register(username, password):
            print("Registrasi berhasil!")
        else:
            print("Username sudah dipakai.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
