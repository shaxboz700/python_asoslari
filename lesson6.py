# avtolar = ['audi' , 'bmw' , 'mersedes' , 'volvo0' , 'kia']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
        

# ism ='Ali'
# print(ism.lower() == 'ali')


# a=5
# print(a == 5)
# print(a != 6)

# ism = input('ismingiz nima:\n>>> ')
# if ism.lower() != 'ali':
#     print(f"Uzr , {ism.title()}  biz Alini kutayapmiz")
# else:
#     print("Salom, Ali")


# javob = float(input("12*6 nechaga teng:"))
# if javob != 72:
#     print("Javob xato")

# yosh = int(input("Yoshingiz nechada: "))
# if yosh >= 18:
#     print("Xush kelibsiz")
# else:
#     print("Kirish Mumkin Emas")

# login = input("Yangi Login kiriting: ")
# if len(login) <=5:
#     print("Login 5 ta harfdan koproq bolish kerak")


# yil = int(input("Tug`ilgan yilingizni kiriting: "))
# if 2025-yil<18:
#     print(f"Yoshingiz {2025-yil} da ekan!")
#     print("Kirish mumkin emas")
# else: 
#     print("Xush kelibsiz")


# yosh = int(input("Yoshingizni kiriting: "))
# if yosh>65: print("siz COVID-19 RISK gurhuida ekansiz")

# x , y = 75 , 50 
# print("x>y")  if x<y  else print("x<y")

# son = -72
# if son<0:
#     print('manfiy son')
# else:
#     print('musbat son')


# yosh = int(input("Yoshingiz nechada: "))
# if yosh <=4:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# elif yosh<= 18:
#     narx = 8000
# else:
#     narx = 10000
# print(f"Sizga Kirish {narx} So`m")

# kun = input("Bugun Kun nima: ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun Dam olish kuni")
# else:
#     print("Bugun ish kuni")


# kun = input("Bugun kun nima? ")
# harorat = float(input("Havo harorati qanday? "))
# if kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat>=30:
#     print("Cho`milgani ketdik")
# elif kun.lower() == 'yakshanba' or kun.lower() == 'shanba' and harorat<30:
#     print("Uyda dam olamiz")

# narh = 15000
# choy = True
# salat = False
# if choy and salat:
#     narh = narh+10000
# elif choy or salat:
#     narh = narh +5000
# print(f"Jami summaa {narh} so`m")

# narh = 15000
# choy =True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi")
#     narh = narh+ 3000
# if salat:
#     print("Mijoz salat oldi")
#     narh = narh+ 5000
# if non:
#     print("Mijoz non oldi")
#     narh = narh+ 5000
# if kompot:
#     print("Mijoz kompot oldi")
#     narh = narh+ 2000
# if assorti:
#     print("Mijoz assorti oldi")
#     narh = narh+ 15000
# print(narh)

# menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
# print('somsa' in menu)

# ovqat = input(" Nima Ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi')
# else:
#     print('Afsuski bizda bunday ovqat yo`q')

# menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
# print('manti' not in menu)
# ovqat = input(" Nima Ovqat yeysiz? ")
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo`q')
# else:
#     print('Buyurtma qabul qilindi')

# menu = ['osh' , 'qozonkabob' , 'shashlik' , 'norin' , 'somsa']
# buyurtmalar = ["osh", 'somsa' , 'manti' , 'shashlik']
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz , menuda {taom} yoq")
# else:
#     print('Savatchangiz bo`sh!')

# dostlar = []
# print("3 ta eng yaqin do'stlaringizni kiriting!")
# for n in range(3):
#     dostlar.append(input(f"{n+1}-do'stingizni ismini yozing. \n>>>>>").title())
# print(dostlar)




#    =    teng
#    ==   tengmi
#    !=   teng emasmi
#    or = yoki
#    and = va
#    
#     >>>Barcha bo`limlar if bilan yozilsa har bir shartni tekshirib chiqadi
#    if , elif ,else dan foydalansak mos kelgan bittasini tekshiradi 
#    qolganlarini esa yoq`


#    True = 1
#    False = 0

#    in - bu funksiya list ichidgi malumotlarni tekshirishda ishlatiladi
#    not in  -bu funksiya in funksiyasini teskarisi