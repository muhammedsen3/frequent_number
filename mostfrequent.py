numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
numbers = sorted(numbers,key=numbers.count,reverse=True)
print(f"{numbers[0]} is most frequent number and {numbers.count(numbers[0])} times repeated. ")