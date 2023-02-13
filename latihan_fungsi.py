'''Fungsi pada python didefinisikan dengan def'''

'''def nama_fungsi():'''

def salam():
  print("Assalamu'alaikum !! Akhi Ukhty")

salam()
salam()
salam()

'''Buatlah sebuah fungsi versi kalian'''

'''Fungsi dengan parameter'''
'''def nama_fungsi(p1, p2)'''

def say_hi(nama):
  print("Halo perkenalkan nama saya", nama)

say_hi("Jawir")
say_hi("Reog")

'''Buatlah fungsi dengan 3 Parameter'''
def perkenalan(nama, alamat, umur):
  # Metode
  print("Nama saya:", nama)
  print("Alamat saya:", alamat)
  print("Umur saya:", umur, 'tahun')

perkenalan("Ujang", "Jakarta", 25)

print("\n\n=========== BATAS ===========\n\n")

perkenalan("Yusman", "Depok", 19)