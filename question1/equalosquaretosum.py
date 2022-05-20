def number(num):  
    rem = sum = 0;  
      
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem*rem);  
        num = num//10;  
    return sum;  

          
print("Equal to the square of sum: ");  
for i in range(1, 101):  
    result = i;  
      
    while(result != 1 and result != 4):  
        result = number(result);  
      
    if(result == 1):  
        print(i) 
