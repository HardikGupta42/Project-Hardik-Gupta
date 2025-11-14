print("Hello, World!")
if 5>2:
    print("five is greater than two")
x=5
y="hello"
print("x+y")
x=5
y=3
print(y+x)
print(x-y)
print(x*y)
print(x/y)
#jyyffy
print("this  is  python")
print('hello')
x=7
y="Hardik"
print(type(x))
print(type(y))
x=4.5 
print(type(x))
x=True
x=5
y=4
print(bool(x+y))
print(bool(x))
x=""
print(bool(x))
x="e"
print(bool(x))
my_var=40
print(my_var)
x,y,z="30","40","50"
print(x)
x="30","40","50"
print(x)

x=y=z="apple"
print(z)


fruits=["apple","banana","cherry"]
x=y=z=fruits
print(x)
print(type(x))
fruits=[2,4,7,8,34,50]
print(fruits)
print(type(fruits))

x="python"
y="is"
z="good"
print(x,y,z)
print(x+y+z)


x="good"
# global var

def my_function():
   # function opening

    print("python is "+ x)
    # action
    my_function()
    # function closing

    print("python is " + x)

    
    def my_func():
        global x
        x="good"
    my_func()
    print("python is " + x)

#DataTypes

x=1j
print(type(x))


x=10
y=20


print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)




#list

my_list=["apple","banana"]
print(type(my_list))
print(my_list)

print(len(my_list))

my_list=["apple","banana","cherry"]
print(my_list[1])
print(my_list[-1])


my_list=["apple","banana","cherry","shi", "badsui","vrfaewuh"]
print(my_list[2:5])

my_list=["apple","banana",1,3,5,7]
my_list[2:5]=["abc"]
print(my_list)