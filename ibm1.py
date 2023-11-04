s = input("Enter String : ") #79611511011372113721110141108
s = s[::-1] # 801141011127311011511697
print(s)
i=0
res = ""
while(i<len(s)-1):
      x=s[i]+s[i+1]
      if x == "32":
         res = res + " "
      elif int(x) in range(65,91) or int(x) in range(97,100):
           res = res + chr(int(x))
      elif i+2<len(s):
           x = x+s[i+2]
           res = res + chr(int(x))
           i +=1
      i+=2
print(res)      