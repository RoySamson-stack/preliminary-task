def check_divsum(number):
  remainder = 0
  digit_sum = 0
  check = False
  n = number
  while(n > 0):
    remainder = n % 10
    digit_sum = digit_sum + remainder
    n = n//10
  if number % digit_sum == 0:
    check = True
  return check

print( )
for i in range(1,100):
  if check_divsum(i):
    print(i)
    # break
print('')
print('')