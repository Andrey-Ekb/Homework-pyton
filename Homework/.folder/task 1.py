# Задача 2. найти сумму трех чисел

i = int (input ('Введите трехзначное число '))

sum = i//100 + i//10 %10 + i%10

print(f'Сумма трех чисел равна - ',sum)
print()



# Задача 4. Наити сколько сделали журавликов каждый.
#
i = int(input('Введите общее количество сделанных журавликов '))
if i%6 != 0: print('нет решения')

else: 
    Serg=i//6
    Ket=Serg*4
    print('Катя сделала',Ket,'журавлика(ов). Петя и Сергей сделали по ',Serg,'журавлику(ов).')
print()


# Задача Найти счастливый билет, если найден YES, иначи NO.
#
number=(input('Введите шестизначный номер билета '))
if len(number)==6:
    num1=int(number[:3])
    num2=int(number[3:])
    num1=(num1//100)+(num1//10 %10)+num1%10
    num2=(num2//100)+(num2//10 %10)+num2%10
    if num1==num2: print('Билет',number,'счастливый - YES')
    else: print('Билет не счастливый - NO')
else: print('длина номера не соответствует заданной, попробуйте еще раз')
print()

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
#

n=int(input('Введите кол-во долек для значения n - '))
m=int(input('Введите кол-во долек для значения m - '))
k=int(input('Введите кол-во отломленных долек  m - '))

if k<(n*m): 
    print(n,m,k)
    if (k%n == 0 or k%m ==0): print('Можно отломить - Yes')
    
else: print('столько долек отломить нельзя - NO')
print()