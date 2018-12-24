def say_hello(x):
    print x

print(say_hello("hello"))
def does_it_change(x):
    x = "hello"
    return x

my_str = "koko"
does_it_change(my_str)

print(my_str)
a = [1, 2, 3]

for x in a:
    x += 1
    print(x)
    
for x in a:
    print(x)
a = [1, 2, 3]
x = id(a)
print x

a += [4]
y = id(a)
print y

if x == y:
    a += [5]
print a
a = [1, 2, 3]
x = id(a)
print x
print a

a = a + [4]
y = id(a)
print y
print a

if x == y:
    a += [5]
print a
class B:
    def __init__(self):
        self.element_1 = 'can you print me'
        
print(B().element_1)