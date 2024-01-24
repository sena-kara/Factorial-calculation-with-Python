
sayi = int(input("Sayı : "))

faktoriyel = 1
if sayi<0:
    print("Negatif sayıların faktoriyeli hesaplanamaz")
    
elif sayi==0:
    print("Sonuç = 1 faktoriyel")
    
else:
    for i in range(1, sayi + 1):
        faktoriyel = faktoriyel * i
    print("sonuç = ", faktoriyel)
    
    
    
    # diğer çözüm
    
def FirstFactorial(num):

  if num == 1:
    return num

  else:
    return num * (FirstFactorial(num - 1))


# keep this function call here 
print(FirstFactorial(input()))