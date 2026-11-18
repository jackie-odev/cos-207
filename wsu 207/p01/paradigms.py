#practical one :the same (the sum of squares )in three styles 
data =[7, 3, 5 , 8, 9]

#1 imperative style : say how ;step by step; changing a variable
total = 0
for x in data:
    total = total + (x * x)
print(f"Imperative : {total}")

#fuctional style : combines functions ; no variable is changed 
print(f"Functional : {(sum(map(lambda x : x*x , data)))}")

#Declarative style : say what you want 
print(f"Declarative : {(sum(x*x for x in data))}")
