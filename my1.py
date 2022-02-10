import math
import random
import datetime
import string
from unicodedata import name
print(abs(-11))
print(round(5.6543,2))
print(pow(3,3))
print(max(1,4,2,444,5),min(3,1,55,6,666))
x=[55,4,4]
print(sum(x))
print(math.sqrt(49))
print(math.remainder(5,2))
print(random.randint(0,100))
print(datetime.date(2022,2,9).day)
print(datetime.time(2,55,21).hour)
print(datetime.datetime.today().second)
today=datetime.datetime.today()
print("{} ** {}  *  {}".format(today.month,today.year,today.day))
#strftime


alphabet="abcdefjhissjklmnopqrstuvwxyz"
print(alphabet[-6:])
print(alphabet[6:0:-1])
s = slice(0,5)
print(alphabet[s])
print(alphabet.index("c"))
print(len(alphabet))
print(alphabet.count("s"))
print("ss" in alphabet)



#---------------------

ser="what Can i do"
print(ser.find("do"))
print(ser.rfind("do"))
str_to_lst=ser.split()
print(str_to_lst)
a=' $'.join(str_to_lst)
print(a)

values= '1\n2\n3\n4\n5\n'
print(values.replace("\n",","))

text= '      Python Course      '
print(text.strip())
print(text.lstrip())
print(text.rstrip())


text= 'this is python course'
print(text.upper())
print(text.lower())
print(text.title())
print(text.swapcase())


str= r'\t Python'
file_path  = r"gf\\gf\\fg\\eee\\"
print(file_path)
print(string)



fir="qusai"
sec="ahmed"
print('my name is {1} {0}'.format(fir,sec))


#---------------------------------------------------------------------------#


def info(name,age):
    print('my name is ',name,'and I am ',age,'years old')
print(info('Qusia',17))

def info(name,age):
    print('my name is ',name,'and I am ',age,'years old')
print(info(age=17,name='ah'))

def info(name = 'Ghada',age = 16 ,course = 'python'):
    print('my name is '+name+'and I am ',age,'years old and I am taking '+course+'course')
info()

def avg(*args):
    total= sum(args)
    leng= len(args)
    average = total / leng
    print(average)
    pass
avg(7,6,4,6,8,8,8)

def info(name_1,name_2):
    print("first student : ",name_1 )
    print("second student name : ",name_2)
names='ahmed','qusai'
info(*names)

def my_func(*items):
    print(items)
items = ['a','b','c']
my_func(*items)

def info(**kwargs):
    print('my name is',kwargs["name"])    
info(name = "ali",age =17)

def info(name,age):
    print('my name is ',name,'and I am ',age,'years old')
d={'name':'Ali','age':17}
info(**d)








