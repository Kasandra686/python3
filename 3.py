def my_func(nums):
   nums.remove(min(nums))
   return (int(nums[0])+int(nums[1]))

while True:
    nums = input("Введите три числа через пробел: ").split()
    if (len(nums)==3and(nums[0].isdigit())and(nums[1].isdigit())and(nums[2].isdigit())):
        break
    else: print("Ошибка ввода!")

print (my_func(nums))