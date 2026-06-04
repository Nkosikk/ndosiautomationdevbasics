#def greet(name, age, message):  ->Defining a function
#greet → Function name
#name, age, message → Parameters

def greet(name , age , message ):
# anything indented under the function is called the function body:
#These are the instructions that run when the function is called.
    print(f'Hello!{name}')
    print(f'You are {age} years old')
    print(f'{message}')

#Argument must match the 3 called functions(name,age,message)
#The argument "Thabo,20,I love you" is passed into the parameters "name,age, message"

greet('Thabo', 20,'I love you' )
greet('Seemah',17, 'Take care')
greet('Sammy',34, 'See you later')
greet('Munky',12, 'See you later')
greet('Kim',12,'Stay strong')

#Parameter = empty placeholder
#Argument = actual value given to the placeholder ✅