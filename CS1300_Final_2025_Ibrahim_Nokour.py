# Problem 1:

def count_positive(numbers):
    positiveNumbers = 0
    for number in numbers:
        if number > 0:
            positiveNumbers += 1
    return positiveNumbers
print(count_positive([5, -2, 0, 3, -1, 8]))
print(count_positive([-1, -2, -3]))
print(count_positive([10, 20, 30]))
print(count_positive([10, 20, 30]))
print(count_positive([]))

# Problem 2:
def get_age_group(age):
    if age >= 60:
        return "Senior"
    elif 20 <= age < 60:
        return "Adult"
    elif 13 <= age < 20:
        return "Teen"
    else:
        return "Child"
    
def count_age_groups(ages):
    groups = {"Child": 0, "Teen": 0, "Adult": 0, "Senior": 0}
    for age in ages:
        groups[get_age_group(age)] += 1
    return groups
    
print(get_age_group(60))
ages_list = [5, 15, 25, 35, 65, 8, 18, 70]
print(count_age_groups(ages_list))

# Problem 5:

def reverse_list(items):
    revlist = []
    for i in range(len(items)):
        revlist.append(items.pop())
    return revlist

print(reverse_list([1,2,3,4,5]))
print(reverse_list(["a", "b", "c"]))
print(reverse_list([10]))
print(reverse_list([]))

        