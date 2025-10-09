
for i in range(10):
    print("Into the future of Earth")


x = 5
while x < 10:
    print("10 years have passed")
    x += 1


a = 10
b = 12
for i in range(20):
    if b < a and b / a != 0:
        print("True")
    else:
        print("False")


content = ["earth is our home", "10 years have passed"]
content.append("earth is our home")
content.insert(1, "Nazi Germany")
content.insert(3, "World War 2")
content.pop()

print("Content list:", content)


sorted_content = sorted(content, reverse=True)
print("Sorted content:", sorted_content)

numbers = [1, 11, 3, 3, 3, 4, 5, 9, 7, 48, 9, 10]
numbers.pop(3)        
numbers.remove(1)     
numbers.sort()        
numbers.insert(2, 35) 

print("Count of 3:", numbers.count(3))
print("Numbers list:", numbers)


numbers.clear()
print("After clearing:", numbers)
