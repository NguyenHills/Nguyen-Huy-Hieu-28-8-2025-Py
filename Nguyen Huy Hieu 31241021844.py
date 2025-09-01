import random



def ex1():
    string1 = []
    total = 0
    for i in range(5):
        x = random.randint(1,50)
        string1.append(x)
        total += string1[i]
    print(string1)
    print(total)
def ex2():
    string2 = []
    multi = 1
    for i in range(5):
        x = random.randint(1,50)
        string2.append(x)
        multi *= x
    print(string2)
    print(multi)
def ex3():
    string3 = []
    for i in range(5):
        x = random.randint(1,50)
        string3.append(x)
    largest = string3[0]
    for lg in string3:
        if lg > largest:
            largest = lg
    print(string3)
    print(largest)
def ex4():
    string4 = []
    for i in range(5):
        x = random.randint(1,50)
        string4.append(x)
    smallest = string4[0]
    for lg in string4:
        if lg < smallest:
            smallest = lg
    print(string4)
    print(smallest)
def ex5():
    string5 = ["abc","xyz","bab","ba","aa","aca","1820061"]
    correct_string5 = 0
    for item in string5:
        if len(item) >= 2 and item[0] == item[-1]:
            correct_string5 += 1

    print(correct_string5)
def ex6():
    lst6 = []
    if len(lst6) == 0:
        print("List is empty")
    else:
        print("List is not empty")
def ex7():
    lst7 = [2,3,5,6,2,4,5,6,7,2,4,5,6,7,2,3,4,5,6,7,7,1,1,2,3,4,9,9]
    k = []
    for i in lst7:
        if i not in k:
            k.append(i)
    print(k)
def ex8():
    main_8 = [1,2,3,4,5,6]
    clone = []
    for i in main_8:
        clone.append(i) # dung copy cung duoc
    print(clone)
def ex9():
    lst9 = ["banana","ant","dog","mouse","keyboard"]
    n = int(input("Enter the number of elements: "))
    result = []
    for i in lst9:
        if len(i) > n:
            result.append(i)
    print(result)
def ex10():
    a = {"a","b","c","d","e","f"}
    b = {2, 3, 4, 5, 6}
    c = {"a",2,3,"b","c","d"}
    if a.intersection(b) or a.intersection(c) or b.intersection(c):
        print("True")
    else:
        print("False")
def ex11():
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    del sample_list[5]
    del sample_list[4]
    del sample_list[0]
    print(sample_list)
def ex12():
    ln = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18]
    k = []
    for i in ln:
        if i % 2 == 0:
            k.append(i)
    u = set(ln)
    p = set(k)
    print(f"The results is: {u - p}")
def ex13():
    string13 = ['Red', 'Green', 'White', 'Black', 'Pink']
    random.shuffle(string13)
    print(string13)
def ex14():
    squares =[]
    for i in range(1,31):
        squares.append(i**2)
        res= squares[:5]+squares[-5:]
    print(res)
def ex15():
    l15 =['Red', 'Green', 'Blue']
    for idx in range(len(l15)):
        print(f"{idx} {l15[idx]}")
def ex16():
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    result = "".join(char)
    print(type(result))
    print(result)
def ex17():
    colors = ['Red', 'Green', 'White', 'Black']
    idx = int(input("Enter the index of your choice: "))
    result = colors[idx]
    print(result)
def ex18():
    num = [[1, 2], [3, 4], [5, 6]]
    result = []
    for i in num:
        for k in i:
            result.append(k)
    print(result)
def ex19():
    fl = ["a","b","c","d","e",'f']
    sl = [1,2,3,4,5,6,7,8,9]
    result = fl.__add__(sl)
    print(result)
def ex20():
    color =['Red', 'Green', 'Blue', 'Yellow']
    random.shuffle(color)
    print(f"The random color is : {color[0]}")
def ex21():
    str21 = "www.google.com"
    k = {}
    for i in str21:
        k[i] = k.get(i, 0) + 1
    print(k)
def ex22():
    lst22 = ["a","b","c","d","a","a","c","d","e","e",'f']
    result22 = list(set(lst22))
    print(result22)



def ex23():
    str23 = "Hello Teacher"
    print(id(str23))
def ex24():
    alt = [2, 3, 4, 5, 6, 7]
    blt = [4, 5, 6, 7, 8, 9]
    result = set(alt).intersection(set(blt))
    print(list(result))
def ex25():
    l_25 = [2, 3, 4, 5, 6, 7]
    result25 = int("".join(map(str, l_25)))
    print(result25)
def ex26():
    chuoi = ["green","grey","brown","red","pink","purple"]
    tudien = {}
    for chu in chuoi:
        k = chu[0]
        tudien.setdefault(k, []).append(chu)
    print(tudien)
def ex27():
    s27 , p27 = [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
    re = s27.__add__(p27)
    print(re)
def ex28():
    chuoi = "Hello my name is Hieu"
    print(f'Result: {chuoi.split()}')
def ex29():
    c1 = [1,2]
    c2 = [3,4]
    c3 = [5,6]
    c4 = [7,8]
    result = [c1,c2,c3,c4]
    print(result)
def ex30():
    lst30 = [1,2,3,4,5]
    for i in lst30:
        print(i)
def ex31():
    num = []
    for i in range(7):
        num.append(random.randint(1,100))
    print(num)
    largest = max(num)
    num.remove(largest)
    second = num[0]
    for l in num:
        if l > second:
            second = l
    print(second)
def ex32():
    num = []
    for i in range(7):
        num.append(random.randint(1, 100))
    print(num)
    small = min(num)
    num.remove(small)
    second = num[0]
    for s in num:
        if s < second:
            second = s
    print(second)
def ex33():
    lst = ["aa","bb","cc","dd"]
    lst.insert(0,"them gi cung duoc")
    print(lst)
def ex34():
    nums = [2,4,13,14,15,17,9,21,23]
    for i in nums[:]:
        if i % 2 == 0:
            nums.remove(i)
    print(nums)
def ex35():
    sample_list =  [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    uniq = []
    for lst in sample_list:
        if lst not in uniq:
            uniq.append(lst)
    print(uniq)
def ex36():
    lst = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
    re = []
    re2 = []
    for i in lst:
        if isinstance(i, list):
            re.append(i)
        else:
            re2.append(i)
    for k in re:
        for n in k:
            re2.append(n)
    print(re2)
def ex37():
    cor1 = ["red", "orange", "green", "blue", "white"]
    cor2 =  ["black", "yellow", "green", "blue"]
    re1 = set(cor1) - set(cor2)
    re2 = set(cor2) - set(cor1)
    print(re1)
    print(re2)
def ex38():
    lst = [1,2,3,4]
    string_38 =  "exp"
    lst2 =[]
    for i in lst:
        new = string_38 + str(i)
        lst2.append(new)
    print(lst2)
def ex39():
    lst = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
    result = []
    for i in lst:
        if i != 0:
            result.append(i)
    for i in lst:
        if i == 0 :
            result.append(i)
    print(result)
def ex40():
    lst1 , lst2 =  [1,2,3], [4,5,6]
    lst1.extend(lst2)
    print(lst1)
def ex41():
    lst = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    print(result)
def ex42():
    ex = [1, 1, 2, 3, 4, 4, 5, 1]
    result = []
    for i in range(3):
        x = random.choice(ex)
        result.append(x)
    print(result)
def ex43():
    ftl = [[1, 3], [5, 7], [9, 11]]
    sel = [[2, 4], [6, 8], [10, 12, 14]]
    zipped =[a + b for a,b in zip(ftl, sel)]
    print(zipped)
def ex44():
    lst =  [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
    min_lst = min(lst , key = len)
    max_lst = max(lst , key = len)
    print(f"List with maximum length of lists: ({len(max_lst)},{max_lst})")
    print(f"List with minimum length of lists: ({len(min_lst)},{min_lst})")
def ex45():
    original_list=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
    k = []
    for i in original_list:
        if i not in k:
            k.append(int(i))
    print(k)
    largest = smallest = k[0]
    for n in k:
        if n > largest:
            largest = n
    print(f"Maximun number: {largest}")
    for m in k:
        if m < smallest:
            smallest = m
    print(f"Minimum number: {smallest}")
    p =sorted(s*5 for s in k)
    print(f"Sorted list: {p}")
def ex46():
    rows, cols = 3, 2
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    print("Multidimensional list:")
    print(matrix)
def ex47():
    # Tạo 3x3 grid với số từ 1 đến 3
    grid = [[j for j in range(1, 4)] for i in range(3)]
    print("3X3 grid with numbers:")
    print(grid)
def ex48():
    original_list = ['red', 'black', 'white', 'green', 'orange']
    alternate_list = original_list[::2]
    print(f"Original list:{original_list}")
    print(f"List with alternate elements:{alternate_list}")
def ex49():
    ls49 = ['Red', 'Green', 'Blue', 'White', 'Black']
    result =[nguoc[::-1] for nguoc in ls49]
    print(result)
def ex50():
    ls50 = [10, 20, 30, 40, 20, 50, 60, 40]
    result = []
    for i in ls50:
        if i not in result:
            result.append(i)
    print(result)
    multy = 1
    for k in result:
        multy *= k
    print(multy)

if __name__ == '__main__':
        ex50()