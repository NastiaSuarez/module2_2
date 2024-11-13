numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

not_primes = []
primes = []
for i in range(1, 16):
      for j in range(2, 10):
          is_prime = True
          if i % j == 0 and i != 2:
              not_primes.append(i)
              break
          elif i == 9 or i == 15:
              not_primes.append(i)
          elif i != is_prime:
              primes.append(i)
              break
print(not_primes)
print(primes)
