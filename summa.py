def recursive_sum(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += recursive_sum(item)
        else:
            total += item
    return total


chisla = [1, [2, 3], [4, [5, 6]], [-1, -5], 0]
result = recursive_sum(chisla)
print(f"Сумма элементов списка: {result}")
