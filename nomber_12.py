S = int(input("Введите сумму: "))
P = int(input("Введите произведение: "))

x, y = 0, 0
for i in range(1, S+1):
    if P % i == 0:   
        j = P // i  
    if i + j == S:   
        x, y = i, j   
        break

print(f"X = {x}, Y = {y}")  