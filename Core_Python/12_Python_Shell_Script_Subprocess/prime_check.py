
def prime_checker(num = None):

    prime_flag = True

    for i in range(2, num):
        if num % i == 0:
            prime_flag = False
            break

    return prime_flag

def main():
    n = int(input("Enter Number : "))
    prime_status = prime_checker(n)

    if prime_status:
        print("%d Number is Prime !" %(n))
    else:
        print("%d Number is not Prime !" %(n))

main()
