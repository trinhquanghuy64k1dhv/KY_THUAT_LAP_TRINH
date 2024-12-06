print("Sinh vien : Trinh Quang Huy")
print("MSSV : 235752021610016")
print("#################")
def sieve_of_eratosthenes(limit):
    # Tao mot danh sach cac so tu 0 đen limit
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            # Đanh dau tat ca cac boi so cua p la khong phai so nguyen to
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1

    # Tao danh sach cac so nguyen to
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)

    return tuple(primes)  # Tra ve tuple chua cac so nguyen to

# Tao tuple P chua cac so nguyen to nho hon 1 trieu
P = sieve_of_eratosthenes(1000000)

# In ra so luong va mot vai so nguyen to
print(f"So luong so nguyen to nho hon 1 trieu: {len(P)}")
print(f"Mot vai so nguyen to: {P[:10]}")  # In 10 so nguyen to đau tien
