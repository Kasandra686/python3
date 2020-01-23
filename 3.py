def my_func(nums):
   sorted(nums)
   print(nums)
   return (int(nums[1])+int(nums[2]))

while True:
    nums = input("Введите три числа через пробел: ").split()
    if (len(nums)==3and(nums[0].isdigit())and(nums[1].isdigit())and(nums[2].isdigit())):
        break
    else: print("Ошибка ввода!")

my_func(nums)