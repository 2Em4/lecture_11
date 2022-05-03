def recursive_nth_fibo(cislo):
    if cislo == 0:
        return 0
    elif cislo == 1:
        return 1
    else:
        return recursive_nth_fibo(cislo-1)+recursive_nth_fibo(cislo-2)

def main():
    pass
    print()


if __name__ == "__main__":
    main()
