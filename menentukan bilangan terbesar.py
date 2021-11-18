print("Program Bilangan Terbesar Dari 3 Bilangan Yang Diinputkan")
A=int(input("Masukkan bilangan pertama : "))
B=int(input("Masukkan bilangan kedua : "))
C=int(input("Masukkan bilangan ketiga : "))

if A > B and A > C:
    print(A, "Terbesar dari 3 bilangan yang diinputkan")
elif B > A and B > C:
    print(B, "Terbesar dari 3 bilangan yang diinputkan")
else:
    print(C, "Terbesar dari 3 bilangan yang diinputkan")