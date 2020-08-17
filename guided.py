#Big O notation


#! linear time 

my_list = [1,2,3,4,5]

def print_list(arr):
    for things in arr:
        print(things)

print_list(my_list)

longer_list = [1,2,3,4,5,6,7,9,10]

print_list(longer_list)

#linear time
#O(n)


#! quadratic time 

def nested_loop(arr):
    for thing in arr:
        for other_thing in arr:
            print(thing, other_thing)

nested_loop(my_list)



#
# nested_loop(list_100_long)
#? 10x the input 
#? 100 steps 


#? count all the steps
#? count big O

#! what is the following 

def my_func(arr):
    a = 1
    b = 2
    c = a + b

    for x in range(1000):
        print(x)

    for thing in arr:
        print(thing)

my_func(my_list)

#? 3 +1000 + 5
#? 3 +1000 + 10
#? 3 +1000 + len(arr) = len(arr)
#? disregard the constants


#! BIG O = O(n)
def two_loops (arr):
    for x in range(1000000000000000):
        z = x * x
        print(z)

    for thing in arr:
        print(thing)

    for thing_again in arr:
        print(thing_again)

