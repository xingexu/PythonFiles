import csv
file = open("asking_number", "w")
for i in range(10):
    def ask_number():
        num = int(input("Enter a number: "))
        return num
    def counting(num):
        n = 1
        while n <= num:
            print(n)
            file.write(str(n))
            n = n + 1
    def main():
        num = ask_number()
        counting(num)
    main()
file.close()360

