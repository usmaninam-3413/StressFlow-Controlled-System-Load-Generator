# Prime number calculation (CPU heavy)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

while True:
    for num in range(10**5):
        is_prime(num)