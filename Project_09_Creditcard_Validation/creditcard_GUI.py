card_no = '5610591081018250'
odd_sum = 0
number = list(card_no)
double_list = []
even_sum = 0
for (idx, val) in enumerate(card_no):
    if idx % 2 != 0:
        odd_sum+=int(val)
    else:  # This is even number
        double_list.append(int(val)*2)
        
# Converting the list into a string

double_string = "" 
for x in double_list:
    double_string += str(x)


# Convering sting back to a list
double_list=list(double_string)
for x in double_list:

    even_sum+=int(x)
    
net_sum = odd_sum+even_sum
if net_sum %10 ==0:
    print("Valid Card...")
else:
    print("Invalid Card")

