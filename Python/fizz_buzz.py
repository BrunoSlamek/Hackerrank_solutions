"""
Solution fizz_buzz hackerrank
"""

n = int(input("Digite um número: "))

for i in range(n + 1):
  if i % 3 == 0 and i % 5 == 0:
    print(f'FizzBuzz')
  elif i % 3 == 0:
    print(f'Fizz')
  elif i % 5 == 0:
    print(f'Buzz')
  else:
    print(i)

"""
input: 10

output:
FizzBuzz
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
"""
