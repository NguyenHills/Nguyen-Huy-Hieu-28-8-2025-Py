import random

def bai1():
    bai_1 = set()
    for k in range(10):
        x = random.randint(1,100)
        bai_1.add(x)
    print(f"Danh sach: {bai_1}")
    lon_nhat = nho_nhat = list(bai_1)[0]
    for i in bai_1:
        if i > lon_nhat:
            lon_nhat = i
        elif i < nho_nhat:
            nho_nhat = i
    print(f"Lon nhat la {lon_nhat}")
    print(f"Nho nhat la {nho_nhat}")
    x = int(input("Nhap so bat ki: "))
    if x in bai_1:
        print("Co")
    else:
        print("Khong")
def bai3():
    a = set()
    b = set()
    for i in range(10):
        x = random.randint(1,100)
        y = random.randint(1,100)
        a.add(x)
        b.add(y)
    print(a)
    print(b)
    if a.intersection(b):
        print("Yes")
    else:
        print("Nahh")
def bai4():
    word_set = set()
    word_freq = {}

    for line in strings:
        words = line.split()
        for word in words:
            word = word.lower()
            word_set.add(word)
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    print("Unique words:")
    print(word_set)
    print("\nWord frequencies:")
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")


strings = [
    "This is a test",
    "This test is simple",
    "Test cases should be simple and clear"
]
def bai5():
    c = {1,2,3,4,5,6}
    d = {2,4,5,6,7,8}
    s2 = c - d
    s1 = d - c
    print(s2)
    print(s1)


def dictest():
     hills_company = {
         "Marketing": {
             "ID 123": "Hieu",
             "ID 345": "Chill Guys"
         },
         "Sales": {
             "ID 555": "Nguoi yeu cu",
             "ID 666": "Cuop ngan hang"
         }
     }


     print(hills_company["Marketing"]["ID 123"])
def dic1a():
    keys =["monkey","panda",]
    value =["eat banana","eat bamboo"]
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = value[i]
    print(dictionary)
def dic1b():
    dict1 = {"Ten" : "Nguyen Huy Hieu" , "Noi sinh" : "Tp.HCM" }
    dict2 = {"Nghe nghiep" : "Sinh vien" , "Noi cong tac" : "UEH"}
    dict1.update(dict2)
    print(dict1)
def dic1c():
    subject_dict = {'math': 90, 'science': 85, 'history': 88}
    history_score = subject_dict.get('history', 'Key not found')
    print("Value of 'history':", history_score)
def dic1d():
    default_dict = dict.fromkeys(['name', 'age', 'country'], 'Unknown')
    print("Dictionary with default values:", default_dict)
def dic1edeng():
    sample_dict = {'name': 'John', 'age': 30, 'city': 'Los Angeles'}
    keys_dict = {key: None for key in sample_dict.keys()}
    print("Dictionary by extracting keys:", keys_dict)

    del_keys = ['name', 'age']
    for key in del_keys:
        if key in sample_dict:
            del sample_dict[key]
    print("Dictionary after deleting keys:", sample_dict)

    value_to_check = 'Los Angeles'
    value_exists = value_to_check in sample_dict.values()
    print(f"Does the value '{value_to_check}' exist in the dictionary?", value_exists)
def dic1h():
    dict_with_rename = {'name': 'Alice', 'age': 30}
    dict_with_rename['full_name'] = dict_with_rename.pop('name')
    print("Dictionary after renaming key:", dict_with_rename)
def dic1i():

    sample_dict_2 = {'a': 10, 'b': 20, 'c': 5}
    min_key = min(sample_dict_2, key=sample_dict_2.get)
    print("Key of minimum value:", min_key)
def dic1j():
    nested_dict = {'student': {'name': 'John', 'age': 18, 'subject': 'Math'}}
    nested_dict['student']['age'] = 19
    print("Nested dictionary after changing value:", nested_dict)
def dic2():
    se = "Python program that counts the number of times characters appear in a text paragraph"
    dct = {}
    for i in se:
        if i not in dct:
            dct[i] = 1
        else:
            dct[i] += 1
    print(dct)


def prime_numbers_dict(N):

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True


    primes = [x for x in range(2, N) if is_prime(x)]
    return {i + 1: primes[i] for i in range(len(primes))}



N = int(input("Enter the value of N: "))
print("Dictionary of prime numbers:", prime_numbers_dict(N))


def restructure_employees(employees):
    dept_employees = {}
    for emp_id, details in employees.items():
        dept = details["department"]
        if dept not in dept_employees:
            dept_employees[dept] = {}
        dept_employees[dept][emp_id] = {"name": details["name"], "salary": details["salary"]}
    return dept_employees

# Input dictionary
employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}

# Calling the function and printing the result
dept_employees = restructure_employees(employees)
print(dept_employees)

if __name__ == '__main__':
    bai1()
    bai3()
    bai5()
    bai4()
    dic1a()
    dic1h()
    dic1i()
    dic1b()
    dic2()
    dic1j()
    dic1edeng()
    dic1d()
    dic1c()
    prime_numbers_dict(N)