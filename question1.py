def number_to_words(n):
    ones={0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
    tens={0:"",2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}
    if n < 20:
        return ones[n]
    elif n<100:
        return tens[n//10]+ones[n%10]
    elif n<1000:
        return ones[n//100]+"hundred"+(("and"+number_to_words(n%100)) if n%100!=0 else "")
    elif n==1000:
        return "onethousand"

def count_letter_to_numbers_words(limit):
    total_letters=0
    for number in range(1,limit+1):
        words=number_to_words(number)
        total_letters+=len(words)
    return total_letters

result = count_letter_to_numbers_words(1000)
print(result)
