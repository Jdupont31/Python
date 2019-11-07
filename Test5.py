def isprime(number):

	for i in range(2,int(number**0.5)+1):

		if number%i==0:

			return False

	return True

n = int(input('Entrer le nombre premier que vous v: ')) # Demande le nombre premier

primes = []

num = 2

while len(primes) < n:

	if isprime(num):

		primes.append(num)

		num += 1
	else:

		num += 1

print(primes[len(primes) - 1])