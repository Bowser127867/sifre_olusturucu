karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
import random






while True:
    hesap = input("Which username do you want?\n")
    sayi = int(input("Kaç karakterli bir şifre istersin?\n"))
    sifre = ""
    for i in range(sayi):
        sifre += random.choice(karakterler)
    with open("sifreler.txt", "a") as file:
        file.write(f"{hesap} : {sifre}\n")

print(file.write(f"{hesap} : {sifre}"))