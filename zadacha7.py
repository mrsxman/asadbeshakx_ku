# 1

n = int(input("n natural soni: "))
summa = 0

for _ in range(n):
    son = int(input("Sonni kiriting: "))
    summa += son

eng_kichik = eng_katta = son  # Boshlangich qiymatlar uchun

for _ in range(n - 1):
    son = int(input("Sonni kiriting: "))
    summa += son

    if son > eng_katta:
        eng_katta = son
    elif son < eng_kichik:
        eng_kichik = son

print(f"Toplam: {summa}")
print(f"Eng katta son: {eng_katta}")
print(f"Eng kichik son: {eng_kichik}")

# 2

def kichik_yuzali_tortburchak(n):
    min_area = float('inf')
    min_a, min_b = 0, 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i * j <= n:
                area = i * j
                if area < min_area:
                    min_area = area
                    min_a, min_b = i, j
    
    return min_a, min_b

# Test uchun misol
n = 20
result = kichik_yuzali_tortburchak(n)
print(f"Eng kichik yuzali to'rtburchak: {result}")

# 3

def kritilgan_tortburchak(n, a, b):
    max_perimeter = 0
    max_a, max_b = 0, 0
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i * j <= n:
                perimeter = 2 * (i + j)
                if perimeter > max_perimeter and i <= a and j <= b:
                    max_perimeter = perimeter
                    max_a, max_b = i, j
    
    return max_a, max_b

# Test uchun misol

n = 20
a = 5
b = 6
result = kritilgan_tortburchak(n, a, b)
print(f"Eng katta perimetrga ega bolgan tortburchak: {result}")

# 4

# Funksiya tuzish
def eng_kichik_element_topish(toplam):
    eng_kichik = float('inf')  # Hozirgi eng katta qiymatni o'rnatamiz
    for son in toplam:
        if son < eng_kichik:
            eng_kichik = son
    return eng_kichik

# Foydalanuvchi to'plamni kiritadi
toplam = list(map(float, input("Iltimos, sonlarni vergul orqali kiriting: ").split(',')))

# Natijani chiqaramiz
natija = eng_kichik_element_topish(toplam)
print(f"To'plamdagi eng kichik element: {natija}")


# 5

# Funksiya tuzish
def eng_katta_zichik_topish(toplam):
    eng_katta_zichik = float('-inf')  # Hozirgi eng katta qiymatni o'rnatamiz
    for m, v in toplam:
        zichik = m / v  # Zichikni hisoblaymiz
        if zichik > eng_katta_zichik:
            eng_katta_zichik = zichik
    return eng_katta_zichik

# Foydalanuvchi to'plamni kiritadi
toplam = []
n = int(input("Iltimos, to'plamda nechta element bo'lishini kiriting: "))
for _ in range(n):
    m, v = map(float, input("Iltimos, og'irlik va hajmni vergul orqali kiriting: ").split(','))
    toplam.append((m, v))

# Natijani chiqaramiz
natija = eng_katta_zichik_topish(toplam)
print(f"To'plamdagi eng katta zichik: {natija}")

# 6

# Funksiya tuzish
def tartib_raqami_aniqlovchi(toplam):
    n = len(toplam)
    
    if n == 0:
        return None, None

    # Birinchi uchragan eng kichik element tartib raqami
    birinchi_uchragan_kichik = min(toplam[0])

    # Oxirgi uchragan eng katta element tartib raqami
    oxirgi_uchragan_katta = max(toplam[-1])

    return birinchi_uchragan_kichik, oxirgi_uchragan_katta

# Foydalanuvchi toplamni kiritadi
toplam = list(map(int, input("Iltimos, toplamni kiriting: ").split()))

# Natijani chiqaramiz
birinchi_uchragan_kichik, oxirgi_uchragan_katta = tartib_raqami_aniqlovchi(toplam)

# Natijalarni ekranga chiqaramiz
print(f"Birinchi uchragan eng kichik element tartib raqami: {birinchi_uchragan_kichik}")
print(f"Oxirgi uchragan eng katta element tartib raqami: {oxirgi_uchragan_katta}")

# 7

# Funksiya tuzish
def tartib_raqami_aniqlovchi(toplam):
    n = len(toplam)
    
    if n == 0:
        return None

    # Birinchi uchragan eng kichik element tartib raqami
    birinchi_uchragan_kichik = min(toplam[0])

    # Oxirgi uchragan eng kichik element tartib raqami
    oxirgi_uchragan_kichik = min(toplam[-1])

    return birinchi_uchragan_kichik, oxirgi_uchragan_kichik

# Foydalanuvchi toplamni kiritadi
toplam = list(map(int, input("Iltimos, toplamni kiriting: ").split()))

# Natijani chiqaramiz
birinchi_uchragan_kichik, oxirgi_uchragan_kichik = tartib_raqami_aniqlovchi(toplam)

# Natijalarni ekranga chiqaramiz
print(f"Birinchi uchragan eng kichik element tartib raqami: {birinchi_uchragan_kichik}")
print(f"Oxirgi uchragan eng kichik element tartib raqami: {oxirgi_uchragan_kichik}")

# 8

# Funksiya tuzish
def tartib_raqami_aniqlovchi(toplam):
    n = len(toplam)
    
    if n == 0:
        return None

    # Birinchi uchragan eng kichik element tartib raqami
    birinchi_uchragan_kichik = min(toplam[0])

    # Oxirgi uchragan eng kichik element tartib raqami
    oxirgi_uchragan_kichik = min(toplam[-1])

    return birinchi_uchragan_kichik, oxirgi_uchragan_kichik

# Foydalanuvchi toplamni kiritadi
toplam = list(map(int, input("Iltimos, toplamni kiriting: ").split()))

# Natijani chiqaramiz
birinchi_uchragan_kichik, oxirgi_uchragan_kichik = tartib_raqami_aniqlovchi(toplam)

# Natijalarni ekranga chiqaramiz
print(f"Birinchi uchragan eng kichik element tartib raqami: {birinchi_uchragan_kichik}")
print(f"Oxirgi uchragan eng kichik element tartib raqami: {oxirgi_uchragan_kichik}")

# 9

# Funksiya tuzish
def tartib_raqamlarini_anish(toplam):
    n = len(toplam)

    if n == 0:
        return None, None

    # Birinchi uchragan eng katta element tartib raqami
    birinchi_uchragan_katta = max(toplam[0])

    # Oxirgi uchragan eng katta element tartib raqami
    oxirgi_uchragan_katta = max(toplam[-1])

    return birinchi_uchragan_katta, oxirgi_uchragan_katta

# Foydalanuvchi toplamni kiritadi
toplam = list(map(int, input("Iltimos, toplamni kiriting: ").split()))

# Natijani chiqaramiz
birinchi_uchragan_katta, oxirgi_uchragan_katta = tartib_raqamlarini_anish(toplam)

# Natijalarni ekranga chiqaramiz
print(f"Birinchi uchragan eng katta element tartib raqami: {birinchi_uchragan_katta}")
print(f"Oxirgi uchragan eng katta element tartib raqami: {oxirgi_uchragan_katta}")

# 10

# Funksiya tuzish
def ekstremal_element_tartib_raqami(toplam, katta=True):
    n = len(toplam)

    if n == 0:
        return None

    # Birinchi uchragan ekstremal element tartib raqami
    if katta:
        ekstremal_element_tartib = max(toplam[0])
    else:
        ekstremal_element_tartib = min(toplam[0])

    return ekstremal_element_tartib

# Foydalanuvchi to'plamni kiritadi
toplam = list(map(int, input("Iltimos, to'plamni kiriting: ").split()))

# Ekstremal elementni topish
katta_element_tartib = ekstremal_element_tartib_raqami(toplam, katta=True)
kichik_element_tartib = ekstremal_element_tartib_raqami(toplam, katta=False)

# Natijalarni ekranga chiqaramiz
print(f"Birinchi uchragan eng katta element tartib raqami: {katta_element_tartib}")
print(f"Birinchi uchragan eng kichik element tartib raqami: {kichik_element_tartib}")

# 11

# Funksiya tuzish
def oxirgi_uchragan_ekstremal_element_tartib_raqami(toplam, katta=True):
    n = len(toplam)

    if n == 0:
        return None

    # Oxirgi uchragan ekstremal element tartib raqami
    if katta:
        ekstremal_element_tartib = max(toplam[-1])
    else:
        ekstremal_element_tartib = min(toplam[-1])

    return ekstremal_element_tartib

# Foydalanuvchi toplamni kiritadi
toplam = list(map(int, input("Iltimos, toplamni kiriting: ").split()))

# Oxirgi uchragan ekstremal elementni topish
katta_element_tartib = oxirgi_uchragan_ekstremal_element_tartib_raqami(toplam, katta=True)
kichik_element_tartib = oxirgi_uchragan_ekstremal_element_tartib_raqami(toplam, katta=False)

# Natijalarni ekranga chiqaramiz
print(f"Oxirgi uchragan eng katta element tartib raqami: {katta_element_tartib}")
print(f"Oxirgi uchragan eng kichik element tartib raqami: {kichik_element_tartib}")


# 12 


# Funksiya tuzish
def eng_kichik_musbat_topish(toplam):
    eng_kichik_musbat = float('inf')  # Hozirgi eng katta qiymatni o'rnatamiz
    
    for son in toplam:
        if son > 0 and son < eng_kichik_musbat:
            eng_kichik_musbat = son
    
    if eng_kichik_musbat == float('inf'):
        return 0
    
    return eng_kichik_musbat

# Foydalanuvchi to'plamni kiritadi
toplam = list(map(int, input("Iltimos, to'plamni kiriting: ").split()))

# Natijani chiqaramiz
eng_kichik_musbat = eng_kichik_musbat_topish(toplam)
print(f"To'plamdagi eng kichik musbat son: {eng_kichik_musbat}")


# 13


def eng_katta_toq_element_tartib(sonlar):
    toq_sonlar = [x for x in sonlar if x % 2 != 0]

    if not toq_sonlar:
        print("Soni to'q sonlardan iborat emas.")
        return 0

    eng_katta_toq = max(toq_sonlar)
    tartib_raqami = toq_sonlar.index(eng_katta_toq) + 1

    print(f"Eng katta to'q son: {eng_katta_toq}")
    print(f"Eng katta to'q sonning tartib raqami: {tartib_raqami}")

# Massivni tanlang
sonlar = [5, 10, 3, 7, 15, 9, 2, 8]

# Dasturni chaqirish
eng_katta_toq_element_tartib(sonlar)


# 14

def ikkita_nol_chiqar(b, sonlar):
    musbat_sonlar = [x for x in sonlar if x > 0]

    if not musbat_sonlar or all(x <= b for x in musbat_sonlar):
        print("Ikkita 0.")
    else:
        print("Ikkita 0 chiqmasa.")

# B ni tanlang
B = 8

# Musbat sonlar to'plamini tanlang
sonlar = [4, 10, -3, 7, 15, 9, 2, -8, 6, 1]

# Dasturni chaqirish
ikkita_nol_chiqar(B, sonlar)


# 15

def eng_katta_element_tartib_raqami(B, C, sonlar):
    if B >= C:
        print("Xato! B katta yoki teng C ga bo'lishi kerak.")
        return

    b_c_oraliq_sonlar = [x for x in sonlar if B < x < C]

    if not b_c_oraliq_sonlar:
        print("Ikkita 0.")
    else:
        eng_katta = max(b_c_oraliq_sonlar)
        tartib_raqami = b_c_oraliq_sonlar.index(eng_katta) + 1
        print(f"Eng katta element: {eng_katta}")
        print(f"Eng katta elementning tartib raqami: {tartib_raqami}")

# B va C ni tanlang
B = 3
C = 8

# Sonlar to'plamini tanlang
sonlar = [4, 10, 5, 7, 15, 9, 2, 6, 1, 12]

# Dasturni chaqirish
eng_katta_element_tartib_raqami(B, C, sonlar)


# 16

def eng_kichik_element(sonlar):
    if not sonlar:
        print("Soni bo'sh.")
        return

    eng_kichik = min(sonlar)
    tartib_raqami = sonlar.index(eng_kichik) + 1

    print(f"Eng kichik element: {eng_kichik}")
    print(f"Eng kichik elementning tartib raqami: {tartib_raqami}")

# Sonlar to'plamini tanlang
sonlar = [5, 10, 3, 7, 15, 9, 2, 8]

# Dasturni chaqirish
eng_kichik_element(sonlar)


# 17

def turuvchi_element_tartib_raqami(N, sonlar):
    if N <= 0 or len(sonlar) != N:
        print("N noto'g'ri kiritilgan yoki sonlar to'plami uzunligi N ga teng emas.")
        return

    eng_katta = max(sonlar)

    # Eng katta sonning indeksini topish
    eng_katta_indeksi = sonlar.index(eng_katta)

    # Oxirgi eng katta sonning keyingi indeksini topish
    if eng_katta_indeksi < N - 1:
        turuvchi_indeksi = eng_katta_indeksi + 1
        turuvchi = sonlar[turuvchi_indeksi]
        tartib_raqami = turuvchi_indeksi + 1
        print(f"Oxirgi eng katta element: {eng_katta}")
        print(f"Turuvchi element: {turuvchi}")
        print(f"Turuvchi elementning tartib raqami: {tartib_raqami}")
    else:
        print("Oxirgi eng katta element oxirgi element hisoblanadi, boshqa element yo'q.")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [5, 10, 3, 7, 15]

# Dasturni chaqirish
turuvchi_element_tartib_raqami(N, sonlar)


# 18

def turgan_element_tartib_raqami(N, sonlar):
    if N <= 0 or len(sonlar) != N:
        print("N noto'g'ri kiritilgan yoki sonlar to'plami uzunligi N ga teng emas.")
        return

    eng_katta = max(sonlar)

    # Eng katta sonning indeksini topish
    eng_katta_indeksi = sonlar.index(eng_katta)

    if eng_katta_indeksi > 0 and eng_katta_indeksi < N - 1:
        turgan_indeksi = eng_katta_indeksi
        turgan = sonlar[turgan_indeksi]
        tartib_raqami = turgan_indeksi + 1
        print(f"Oxirgi uchragan eng katta element: {eng_katta}")
        print(f"Turgan element: {turgan}")
        print(f"Turgan elementning tartib raqami: {tartib_raqami}")
    else:
        print("To'plamda faqat bitta eng katta element bor, nol chiqariladi.")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [5, 10, 3, 7, 15]

# Dasturni chaqirish
turgan_element_tartib_raqami(N, sonlar)


# 19

def eng_kichik_element(sonlar):
    if not sonlar:
        print("Soni bo'sh.")
        return

    eng_kichik = min(sonlar)
    tartib_raqami = sonlar.index(eng_kichik) + 1

    print(f"Eng kichik element: {eng_kichik}")
    print(f"Eng kichik elementning tartib raqami: {tartib_raqami}")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [5, 10, 3, 7, 15]

# Dasturni chaqirish
eng_kichik_element(sonlar)

# 20

def extremal_element(sonlar):
    if not sonlar:
        print("Soni bo'sh.")
        return

    eng_katta = max(sonlar)
    eng_kichik = min(sonlar)

    eng_katta_indeksi = sonlar.index(eng_katta) + 1
    eng_kichik_indeksi = sonlar.index(eng_kichik) + 1

    print(f"Eng katta element: {eng_katta}")
    print(f"Eng katta elementning tartib raqami: {eng_katta_indeksi}")

    print(f"Eng kichik element: {eng_kichik}")
    print(f"Eng kichik elementning tartib raqami: {eng_kichik_indeksi}")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [5, 10, 3, 7, 15]

# Dasturni chaqirish
extremal_element(sonlar)

# 21

def ortacha_qiymat(sonlar):
    if len(sonlar) <= 2:
        print("N kichik yoki teng 2 bo'lishi kerak.")
        return

    eng_katta = max(sonlar)
    eng_kichik = min(sonlar)

    sonlar.remove(eng_katta)
    sonlar.remove(eng_kichik)

    ortacha_qiymat = sum(sonlar) / len(sonlar)

    print(f"Eng katta qiymat: {eng_katta}")
    print(f"Eng kichik qiymat: {eng_kichik}")
    print(f"Ortacha qiymat: {ortacha_qiymat}")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [5, 10, 3, 7, 15]

# Dasturni chaqirish
ortacha_qiymat(sonlar)

# 22


def eng_kichik_2_qiymat(sonlar):
    if len(sonlar) <= 2:
        print("N kichik yoki teng 2 bo'lishi kerak.")
        return

    eng_kichik_1 = min(sonlar)
    sonlar.remove(eng_kichik_1)

    eng_kichik_2 = min(sonlar)

    print(f"Eng kichik 2 ta qiymat: {eng_kichik_1} {eng_kichik_2}")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [1, 2, 3, 4, 5]

# Dasturni chaqirish
eng_kichik_2_qiymat(sonlar)


# 23

def eng_katta_3_qiymat(sonlar):
    if len(sonlar) <= 3:
        print("N kichik yoki teng 3 bo'lishi kerak.")
        return

    eng_katta_1 = max(sonlar)
    sonlar.remove(eng_katta_1)

    eng_katta_2 = max(sonlar)
    sonlar.remove(eng_katta_2)

    eng_katta_3 = max(sonlar)

    print(f"Eng katta 3 ta qiymat: {eng_katta_1} {eng_katta_2} {eng_katta_3}")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [1, 2, 3, 4, 5]

# Dasturni chaqirish
eng_katta_3_qiymat(sonlar)


# 24


def eng_katta_yigindi(N, sonlar):
    if N <= 1 or len(sonlar) != N:
        print("N noto'g'ri kiritilgan yoki sonlar to'plami uzunligi N ga teng emas.")
        return

    eng_katta_yigindi = float('-inf')
    
    for i in range(N - 1):
        for j in range(i + 1, N):
            current_yigindi = sonlar[i] + sonlar[j]
            eng_katta_yigindi = max(eng_katta_yigindi, current_yigindi)

    print(f"Ikkita qo'shni son yig'indisi eng katta qiymati: {eng_katta_yigindi}")

# N va sonlar to'plamini tanlang
N = 5
sonlar = [1, 2, 3, 4, 5]

# Dasturni chaqirish
eng_katta_yigindi(N, sonlar)


# 25

def ikkita_qoshni_indekslar(N, array):
    if N <= 1:
        print("N > 1 shartini qanoatlantiring.")
        return

    if len(array) != N:
        print("Massiv uzunligi N ga teng emas.")
        return

    min_product = float('inf')  # Eng kichik ko'paytma uchun boshlang'ich qiymat
    index1, index2 = -1, -1

    for i in range(N):
        for j in range(i + 1, N):
            current_product = array[i] * array[j]
            if current_product < min_product:
                min_product = current_product
                index1, index2 = i, j

    print(f"Ikkita qo'shni indekslari: {index1} va {index2}")

# Masalan, N=5 va massiv sifatida [3, 2, 5, 1, 4] berilgan bo'lsin
N = 5
massiv = [3, 2, 5, 1, 4]

ikkita_qoshni_indekslar(N, massiv)

# 26

def maksimal_juft_elementlar(N, array):
    if N <= 1:
        print("N > 1 shartini qanoatlantiring.")
        return

    if len(array) != N:
        print("Massiv uzunligi N ga teng emas.")
        return

    max_even = float('-inf')  # Eng katta juft son uchun boshlang'ich qiymat
    juft_toplam = 0

    for i in range(N):
        if array[i] % 2 == 0:
            juft_toplam += array[i]
            max_even = max(max_even, array[i])

    if juft_toplam == 0:
        print(0)
    else:
        print(f"Maksimal juft element: {max_even}")

# Masalan, N=6 va massiv sifatida [3, 2, 5, 1, 4, 6] berilgan bo'lsin
N = 6
massiv = [3, 2, 5, 1, 4, 6]

maksimal_juft_elementlar(N, massiv)

# 27

def uzun_ketma_ketlik(arr):
    n = len(arr)
    max_length = 1
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, n):
        if arr[i] == arr[i - 1] + 1:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            current_length = 1
            start_index = i

    if current_length > max_length:
        max_start_index = start_index

    return max_start_index, max_length

# Test qilish uchun
arr = [1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13]
start_index, length = uzun_ketma_ketlik(arr)
end_index = start_index + length - 1

print(f"Eng uzun ketma ketlik boshlangan element indeksi: {start_index}")
print(f"Eng uzun ketma ketlikdagi elementlar soni: {length}")
print(f"Eng uzun ketma ketlik: {arr[start_index:end_index + 1]}")


# 28

def uzun_ketma_ketlik(n):
    binary_str = bin(n)[2:]  # Natural sonni ikkilik sistemasiga o'tkazamiz va boshlang'ich "0b" qismini olib tashlaymiz
    max_length = 0
    current_length = 0
    start_index = 0
    max_start_index = 0

    for i in range(len(binary_str)):
        if binary_str[i] in ['0', '1']:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            current_length = 0
            start_index = i + 1

    if current_length > max_length:
        max_start_index = start_index

    return max_start_index, max_length

# Test qilish uchun
n = 1256
start_index, length = uzun_ketma_ketlik(n)
end_index = start_index + length - 1

print(f"Eng uzun ketma ketlik boshlangan element indeksi: {start_index}")
print(f"Eng uzun ketma ketlikdagi elementlar soni: {length}")
print(f"Eng uzun ketma ketlik: {bin(n)[2:][start_index:end_index + 1]}")


# 29

def eng_kichik_ketma_ketlik(n):
    num_str = str(n)
    max_count = 0
    current_count = 0
    last_digit = None

    for digit in num_str:
        if digit in ['0', '1']:
            if last_digit is None or digit == last_digit:
                current_count += 1
            else:
                current_count = 1
        else:
            current_count = 0

        max_count = max(max_count, current_count)
        last_digit = digit

    return max_count

# Test qilish uchun
n = 123405600011110
result = eng_kichik_ketma_ketlik(n)
print(f"To'plamdagi eng kichik ketma ketlikning maksimal soni: {result}")


# 30

def eng_katta_ketma_ketlik_minimal_son(n):
    num_str = str(n)
    max_count = 0
    current_count = 0
    last_digit = None

    for digit in num_str:
        if digit in ['0', '1']:
            if last_digit is None or digit == last_digit:
                current_count += 1
            else:
                current_count = 1
        else:
            current_count = 0

        if current_count == max_count and max_count > 0:
            break  # Tugagan elementlarni qidirishni to'xtatamiz

        if current_count > max_count:
            max_count = current_count

        last_digit = digit

    return max_count

# Test qilish uchun
n = 1234000111101001
result = eng_katta_ketma_ketlik_minimal_son(n)
print(f"To'plamdagi eng katta ketma ketlikning minimal soni: {result}")


