people_list = input().split()
k = int(input())
people_list = [int(person) for person in people_list]
execution_order = []
index = 0
while people_list:
    index = (index + k - 1) % len(people_list)
    executed_person = people_list.pop(index)
    execution_order.append(executed_person)
result = ','.join(map(str, execution_order))
print(f"[{result}]")