banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
print(type(banks_list))
i=0
while i<len(banks_list):
    print((banks_list[i]))
    with open("bank.txt","a") as b:
        b.write(banks_list[i])
        b.write("\n")
    i=i+1