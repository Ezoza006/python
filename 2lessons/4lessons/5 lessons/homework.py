# son = int(input("Juft son kiriting: "))

# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Xato yozdingiz, bu juft emas")

# yosh = int(input("Yoshingizni kiriting: "))

# if yosh < 7 or yosh > 55:
#     print("Chipta bepul")
# elif yosh < 18:
#     print("Chipta narxi: 15000 so'm")
# else:
#     print("Chipta narxi: 17000 so'm")

# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))
# if son1 == son2:
#     print(f"{son1} = {son2}")
# elif son1 > son2:
#     print(f"{son1} > {son2}")
# else:
#     print(f"{son1} < {son2}")
#     mahsulotlar = ["un", "yog'", "shakar", "tuz", "non", "choy", "sut", "tuxum", "go'sht", "guruch"]
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower())

# for buyum in savat:
#     if buyum in mahsulotlar:
#         print(f"Do'konimizda {buyum} bor")
#     else:
#         print(f"Do'konimizda {buyum} yo'q")
# mahsulotlar = ["un", "yog'", "shakar", "tuz", "non", "choy", "sut", "tuxum", "go'sht", "guruch"]
# savat = []
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: ").lower())

# bor_mahsulotlar = []
# mavjud_emas = []

# for buyum in savat:
#     if buyum in mahsulotlar:
#         bor_mahsulotlar.append(buyum)
#     else:
#         mavjud_emas.append(buyum)

# if not mavjud_emas:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:")
#     for m in mavjud_emas:
#         print(m)
#         foydalanuvchilar = ["admin", "bekzod", "ali", "valisher", "olim"]
# yangi_login = input("Yangi login tanlang: ").lower()

# if yangi_login in foydalanuvchilar:
#     son = int(input("Butun son kiriting: "))
# for n in range(2, 11):
#     if son % n == 0:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {yangi_login}!")
#     son = int(input("Butun son kiriting: "))
# for n in range(2, 11):
#     if son % n == 0:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
#         son = int(input("Son kiriting: "))
# if son % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")
#     son = float(input("Son kiriting: "))
# if son > 0:
#     print(f"{son} ning ildizi {son**0.5} ga teng")
# else:
#     print("Musbat son kiriting")
#     son = float(input("Istalgan son kiriting: "))
# if son > 0:
#     print("Musbat son")
# elif son < 0:
#     print("Manfiy son")
# else:
#     print("Son 0 ga teng")
#     son1 = input("1-sonni kiriting: ")
# son2 = input("2-sonni kiriting: ")
# if son1 == son2:
#     print("Sonlar teng")
a = 69
c = 94
d = 78
if a>c and a>d:
    print(f"Kattasi: {a}")
elif c>a and c>d:
 print(f"Kattasi : {c}")
else:
 print(f"Kattasi:{d}")
