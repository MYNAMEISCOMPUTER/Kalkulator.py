print ('='*25)
print ('OPERASI MATEMATIKA :')
print ('    1.Penjumlahan \t [+]')
print ('    2.Pengurangan \t [-]')
print ('    3.Perkalian \t [*]')
print ('    4.Pembagian \t [/]')
print ('='*25)

operasi=input('Pilih operasi 1/2/3/4 :')
bilangan1=eval(input('Masukan bilangan 1 :'))
bilangan2=eval(input('Masukan bilangan 2 :'))

if operasi == '1':
  hasil = bilangan1 + bilangan2
  print(f'Hasil operasi dari {bilangan1} + {bilangan2} = {hasil}')
elif operasi == '2':
  hasil = bilangan1 - bilangan2
  print(f'Hasil operasi dari {bilangan1} - {bilangan2} = {hasil}')
elif operasi == '3':
  hasil = bilangan1 * bilangan2
  print(f'Hasil operasi dari {bilangan1} * {bilangan2} = {hasil}')
elif operasi == '4':
  hasil = bilangan1 / bilangan2
  print(f'Hasil operasi dari {bilangan1} / {bilangan2} = {hasil}')
else:
  print('Tidak valid')

print(f'{bilangan1} adalah:', type(bilangan1))
print(f'{bilangan2} adalah:', type(bilangan2))
print(f'{hasil} adalah:', type(hasil))