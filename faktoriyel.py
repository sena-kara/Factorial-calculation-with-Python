
sayi = int(input("Say� : "))

faktoriyel = 1
if sayi<0:
    print("Negatif say�lar�n faktoriyeli hesaplanamaz")
    
elif sayi==0:
    print("Sonu� = 1 faktoriyel")
    
else:
    for i in range(1, sayi + 1):
        faktoriyel = faktoriyel * i
    print("sonu� = ", faktoriyel)
    
    
    
    # di�er ��z�m
    
def FirstFactorial(num):

  if num == 1:
    return num

  else:
    return num * (FirstFactorial(num - 1))


# keep this function call here 
print(FirstFactorial(input()))