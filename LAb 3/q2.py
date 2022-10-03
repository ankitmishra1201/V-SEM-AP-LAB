def get_unique(numbers):
    numbers.sort()
    uniquelist=[]
    unique_number=set(numbers)
   
    return unique_number

numbers=[1,2,3,3,3,3,4,5]
print(get_unique(numbers))
               
