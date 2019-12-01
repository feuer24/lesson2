""" num = [1,2,3,4,5,6,7,8,9,10]
for number in num:
    number = number + 1
    print(f"{number}")

word = input()
for letter in word:
    print(f"{letter}")
"""
total = 0
count = 0

evaluation = [{'school_class': '4a', 'scores': [3,4,4,5,2]},{'school_class': '4b', 'scores': [5,3,2,2,2,7,10]}]

for clas in evaluation:
    total = total + sum(clas["scores"])
    count = count + len(clas["scores"])
    print("Средний балл по классу: " + clas['school_class'] + " " + str(sum(clas["scores"])/len(clas["scores"])))

print("Средний балл по школе: " + str(total/count))