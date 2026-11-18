# """ Practical 1 : a first look at python dta types. """
scores =[62, 75, 48, 90, 71]#list of int 
course = "WSU-COS 207" #Str
mean = sum(scores) / len(scores) #float
passed = mean >= 50 #bool

for values in  (scores,course,mean,passed):
 print(f"{type(values).__name__:>10} : {values}")
print(f"{course}: n={len(scores)}, mean = {mean:.2f}")
