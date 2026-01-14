import mysql.connector

# 🔹 MySQL ulanish
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",      # agar parol bo‘lsa yozing
    database="gozallik_saloni"
)

cursor = db.cursor()

# 🔹 Ishchi qo‘shish
def ishchi_qoshish():
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    jins = input("Jins (Ayol/Erkak): ")
    maosh = float(input("Maosh: "))

    sql = "INSERT INTO ishchilar (ism, familiya, jins, maosh) VALUES (%s, %s, %s, %s)"
    values = (ism, familiya, jins, maosh)

    cursor.execute(sql, values)
    db.commit()
    print("✅ Ishchi muvaffaqiyatli qo‘shildi")

# 🔹 Ishchilarni ko‘rish
def ishchilarni_korish():
    cursor.execute("SELECT * FROM ishchilar")
    natija = cursor.fetchall()

    print("\n--- ISHCHILAR RO‘YXATI ---")
    for row in natija:
        print(row)

# 🔹 Ishchini o‘chirish
def ishchi_ochirish():
    id = int(input("O‘chiriladigan ishchi ID sini kiriting: "))
    cursor.execute("DELETE FROM ishchilar WHERE id = %s", (id,))
    db.commit()
    print("🗑 Ishchi o‘chirildi")

# 🔹 Ishchi maoshini yangilash
def maosh_yangilash():
    id = int(input("Ishchi ID: "))
    yangi_maosh = float(input("Yangi maosh: "))

    cursor.execute(
        "UPDATE ishchilar SET maosh = %s WHERE id = %s",
        (yangi_maosh, id)
    )
    db.commit()
    print("✏️ Maosh yangilandi")

# 🔹 Admin menyu
def admin_panel():
    while True:
        print("""
========= ADMIN PANEL =========
1. Ishchi qo‘shish
2. Ishchilarni ko‘rish
3. Ishchini o‘chirish
4. Maoshni yangilash
0. Chiqish
===============================
""")
        tanlov = input("Tanlang: ")

        if tanlov == "1":
            ishchi_qoshish()
        elif tanlov == "2":
            ishchilarni_korish()
        elif tanlov == "3":
            ishchi_ochirish()
        elif tanlov == "4":
            maosh_yangilash()
        elif tanlov == "0":
            print("👋 Dastur yopildi")
            break
        else:
            print("❌ Noto‘g‘ri tanlov")

# 🔹 Dasturni ishga tushirish
admin_panel()
