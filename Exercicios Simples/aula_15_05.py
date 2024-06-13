N = int(input())

for i in range(N):
    A,B = input().split()
    Aunit = len(A)
    Bunit = len(B)
    ADif=Aunit-Bunit
    if A.count(B, ADif, ) == 1:
       print ("encaixa")
    else:
       print("nao encaixa")