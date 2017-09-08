import logging

def calculate(first_, second_, third_):
    return ((first_**2)+(second_**3))**(1./third_)

print ((3**2)+(6**3))**(1/2.)
print ((3**2)+(6**3))**(1/2)
print ((3**2)+(6**3))**(0.5)
print 0.5
print 1.0/2.0 #Returns float
print 1/2 #Returns int

while(True):
    try:
        t = str(input("Enter number: "))
        break
    except:
        logging.warning("Please enter a number!!!")
    
print t

my_first_number = input('Please enter a number: ')
my_second_number = input('Please enter a number: ')
my_third_number = input('Please enter a number: ')
my_answer = ((my_first_number**2)+(my_second_number**3))**(1./my_third_number)
print 'Answer = ' + str(my_answer)

#do a calculation

