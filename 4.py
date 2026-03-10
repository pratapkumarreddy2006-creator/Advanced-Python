def even_odd(n):
        
        for i in range(1,n+1):
          if n%2==0:
            return "no is  even "
          else:
            return "no is oddd"
n=int(input("enter a no "))
print(even_odd(n))
