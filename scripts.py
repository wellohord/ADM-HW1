# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 != 0:
        print("Weird")
    else:
        if 2 <= n <= 5: print("Not Weird")
        elif 6 <= n <= 20: print("Weird")
        else: print ("Not Weird")

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    
    if n >= 0:
        for y in range(n): print(y**2)

# Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        if not (year % 100 == 0 and year % 400 != 0):
            leap = True
        
    
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    output_string = ""
    
    for y in range(n):
        output_string += str(y+1)
    
    print(output_string)

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    perm1 = [i for i in range(x+1)]
    perm2 = [j for j in range(y+1)]
    perm3 = [k for k in range(z+1)]
    permutations = [[i,j,k] for i in perm1 for j in perm2 for k in perm3 if i+j+k != n]
       
    print(permutations)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    
    print(arr[arr.index(max(arr))-1])

# Nested Lists
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])   
    
    lowest_grade = 100
    for student in records:
        if student[1] <lowest_grade:
            lowest_grade = student[1]
    
    records = sorted([student for student in records if student[1] != lowest_grade], key=lambda student: student[1])
    
    lowest_grade = records[0][1]
    
    students_with_second_lowest = sorted([student for student in records if student[1] == lowest_grade])
    
    for student in students_with_second_lowest:
        print(student[0])

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    result = sum(student_marks[query_name])/len(student_marks[query_name])
    
    print(f"{result:.2f}")

# Lists
if __name__ == '__main__':
    N = int(input())
    
    output_list = []
    
    for iteration in range(N):
        command = input().split()
        
        if command[0] == "insert":
            output_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(output_list)
        elif command[0] == "remove":
            output_list.remove(int(command[1]))
        elif command[0] == "append":
            output_list.append(int(command[1]))
        elif command[0] == "sort":
            output_list.sort()
        elif command[0] == "pop":
            output_list.pop()
        elif command[0] == "reverse":
            output_list.reverse()
        else:
            print("NONO")

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    tuple_work = tuple(integer_list)
    
    hashed_output = hash(tuple_work)
    
    print(hashed_output)

# sWAP cASE
def swap_case(s):
    return s.swapcase()

# String Split and Join

def split_and_join(line):
    return "-".join(line.split())
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#
def print_full_name(first, last):
    # Write your code here
    print("Hello {0}! You just delved into python.".format(first + " " + last))

# Mutations
def mutate_string(string, position, character):
    placeholder = list(string)
    placeholder[position] = character
    return "".join(placeholder)

# Find a string
def count_substring(string, sub_string):
    counter = 0
    for sub in range(0, len(string)):
       if (string[sub:sub+len(sub_string)] == sub_string): counter += 1
    return counter

# String Validators
if __name__ == '__main__':
    
    def hasalphanum(s):
        for char in s:
            if char.isalnum():
                return True
        return False
    
    def hasalpha(s):
        for char in s:
            if char.isalpha():
                return True
        return False
    def hasdigits(s):
        for char in s:
            if char.isdigit():
                return True
        return False
    def haslowercase(s):
        for char in s:
            if char.islower():
                return True
        return False
    def hasuppercase(s):
        for char in s:
            if char.isupper():
                return True
        return False
    s = input()
    print(hasalphanum(s))
    print(hasalpha(s))
    print(hasdigits(s))
    print(haslowercase(s))
    print(hasuppercase(s))

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Text Wrap

def wrap(string, max_width):
    text = ""
    for c in range(0, len(string), max_width):
        text += string[c:c+max_width] + '\n'
    return text

# Designer Door Mat
# Enter your code here. Read input from STDIN. Print output to STDOUT
def designmat(n,m):
    c = '.|.'
    msg = 'WELCOME'
    mat = ''
    
    def upperandbottomdesign(counter):
        return ((c*counter).rjust((m-len(c))//2,'-')+c+(c*counter).ljust((m-len(c))//2, '-'))
    
    for u in range(int(n/2)): mat += upperandbottomdesign(u) +'\n'
    mat += (msg.center(m,'-')) + '\n'
    for b in range (int(n/2)-1, -1, -1): mat += upperandbottomdesign(b) +'\n'
    
    return mat.rstrip()
if __name__ == '__main__':
    n, m = input().split()
    print(designmat(int(n),int(m)))

# String Formatting
def print_formatted(number):
    # your code goes here
    padding = len(bin(number)[2:])
    for j in range(1,number+1):
        decimal = str(j).rjust(padding, ' ')
        octal = str(oct(j)[2:]).rjust(padding, ' ')
        hexa = str(hex(j)[2:]).rjust(padding, ' ').upper()
        binary = str(bin(j)[2:]).rjust(padding, ' ')
        print(f'{decimal} {octal} {hexa} {binary}')
        

# Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    nth_letter = alphabet[size-1]
    reversed_sub_alphabet = alphabet[:size][::-1]
    max_string_size = len('-'.join([x for x in (reversed_sub_alphabet + alphabet[1:size])]))
    
    temp_substring = ''
    final_substring = ''
    
    for line in range(size):
        if line == 0:
            final_substring += (nth_letter.center(max_string_size,'-') +'\n')
        else:
            temp_substring += reversed_sub_alphabet[line-1] +'-'
            final_substring += (temp_substring + alphabet[size-line-1]+temp_substring[::-1]).center(max_string_size,'-')+'\n'
    
    temp_substring = final_substring.split('\n')
    temp_substring.reverse()
    temp_substring.pop(0)
    for item in range(1, len(temp_substring)):
        final_substring += temp_substring[item] +'\n'
    
    
    print(final_substring)

# Capitalize!

# Complete the solve function below.
def solve(s):
    name_parts = s.split(' ')
    result = ''
    
    for part in name_parts:
        result += str(part.capitalize()) + ' '
    
    return(result.strip())

# The Minion Game
def minion_game(string):
    # your code goes here
    vowels = 'aeiou'
    stuart_points = 0 #Sarting with consonants
    kevin_points = 0 #Starting with vowels
    
    #Creating the words for stuart then kevin
    string_length = len(string)
    for letter in range(string_length):
        if string[letter].lower() not in vowels:
            stuart_points += string_length - letter
        else:
            kevin_points += string_length - letter
    
    #Who's the winner?
    if stuart_points == kevin_points:
        print("Draw")
    elif stuart_points > kevin_points:
        print('Stuart ' + str(stuart_points))
    else:
        print('Kevin ' + str(kevin_points))
        

# Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    #Splitting into substrings
    substring_number = len(string)//k
    substring_list = []
    for counter in range(0, len(string), k):
        substring_list.append(string[counter:counter+k])
    
    #Removing dupicates
    for substring in substring_list:
        print(''.join(set(substring)))

# Introduction to Sets
def average(array):
    # your code goes here
    sum_numbers = sum(set(array))
    
    return(sum_numbers / len(set(array)))
    

# Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
m_list = input().split()
n = input()
n_list = input().split()
m_not_n = set(m_list).difference(set(n_list))
n_not_m = set(n_list).difference(set(m_list))
final_list = list(m_not_n.union(n_not_m))
final_list = [int(x) for x in final_list]
final_list = sorted(final_list)
for x in final_list:
    print(x)

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
happiness = 0
n_m = input().split()
second_line = input().split()
third_line = input().split()
fourth_line = input().split()
third_line = set(third_line)
fourth_line = set(fourth_line)
for element in second_line:
    if element in third_line:
        happiness += 1
    elif element in fourth_line:
        happiness -= 1
        
print(happiness)

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
number_of_stamps = input()
stamps = []
for counter in range(int(number_of_stamps)):
    stamps.append(input())
print(len(set(stamps)))

# Set .discard(), .remove() & .pop()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = reversed([int(x) for x in input().split()])
s = set(s)
number_of_commands = int(input())
for counter in range(number_of_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove' and int(command[1]) in s:
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
subscriptions = 0
english_total = int(input())
english_roll = set([int(x) for x in input().split()])
french_total = int(input())
french_roll = set([int(x) for x in input().split()])
print(len(english_roll|french_roll))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
total_english = int(input())
english_subscribers = set([int(x) for x in input().split()])
total_french = int(input())
french_subscribers = set([int(x) for x in input().split()])
print(len(english_subscribers & french_subscribers))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
english_total = int(input())
english_subscribers = set([int(x) for x in input().split()])
french_total = int(input())
french_subscribers = set([int(x) for x in input().split()])
print(len(english_subscribers - french_subscribers))

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
english_total = int(input())
english_subscribers = set([int(x) for x in input().split()])
french_total = int(input())
french_subscribers = set([int(x) for x in input().split()])
print(len(english_subscribers ^ french_subscribers))

# Set Mutations
# Enter your code here. Read input from STDIN. Print output to STDOUT
number_elements_a = int(input())
set_a = set([int(x) for x in input().split()])
number_of_comparing_sets = int(input())
for counter in range(number_of_comparing_sets):
    command = input().split()
    set_to_compare = set([int(x) for x in input().split()])
    if command[0] == 'update':
        set_a.update(set_to_compare)
    elif command[0] == 'intersection_update':
        set_a.intersection_update(set_to_compare)
    elif command[0] == 'difference_update':
        set_a.difference_update(set_to_compare)
    elif command[0] == 'symmetric_difference_update':
        set_a.symmetric_difference_update(set_to_compare)
    
print(sum(set_a))

# The Captain's Room
# Enter your code here. Read input from STDIN. Print output to STDOUT
#K members per group
#One room per group
k = int(input())
unordered_room_list = [int(x) for x in input().split()]
set_1 = set(unordered_room_list[0:(len(unordered_room_list)//2)])
set_2 = set(unordered_room_list[(len(unordered_room_list)//2):len(unordered_room_list)])
set_1.symmetric_difference_update(set_2)
print(set_1.pop())

# Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT
cases_number = int(input())
for counter in range(cases_number):
    set_a_length = int(input())
    set_a = set([int(x) for x in input().split()])
    set_b_length = int(input())
    set_b = set([int(x) for x in input().split()])
    
    print(set_a.issubset(set_b))
    

# Check Strict Superset
# Enter your code here. Read input from STDIN. Print output to STDOUT
set_a = set([int(x) for x in input().split()])
sets_number = int(input())
sets_list = []
for counter in range(sets_number):
    sets_list.append(set([int(x) for x in input().split()]))
    
for sett in range(len(sets_list)):
    sets_list[sett] = set_a.issuperset(sets_list[sett])
sets_list = set(sets_list)
if len(sets_list) > 1 or sets_list.pop() == 'False':
    print('False')
else:
    print('True')

# collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
number_of_shoes = int(input())
shoe_sizes = [int(x) for x in input().split()]
customers_number = int(input())
shoe_sizes = Counter(shoe_sizes)
total_amount = 0
for count in range(customers_number):
    desired_shoe = input().split()
    if int(desired_shoe[0]) in shoe_sizes.keys() and shoe_sizes[int(desired_shoe[0])] > 0:
       shoe_sizes[int(desired_shoe[0])] -= 1
       total_amount += int(desired_shoe[1]) 
print(total_amount)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
n, m = input().split()
d = defaultdict(list)
for x in range(int(n)+int(m)):
    if x < int(n):
        d['A'].append(input())
    else:
        d['B'].append(input())
d1 = defaultdict(list)
for i, v in enumerate(d['A']):
    d1[v].append(str(i+1))
for word in d['B']:
    if word in d['A']:
        string_to_print = ' '.join(d1[word])
        print(string_to_print)
    else:
        print(-1)

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

students_number = int(input())
Student = namedtuple('Student', input())
all_marks_sum = 0
for student in range(students_number):
    inp = input().split()
    stud = Student(inp[0], inp[1], inp[2], inp[3])
    all_marks_sum += int(stud.MARKS)
print(all_marks_sum / students_number)

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
supermarket = OrderedDict()
items_number = int(input())
for item in range(items_number):
    inp = input().split()
    item_price = inp[-1]
    inp.pop()
    item_name = ' '.join(inp)
    if item_name.strip() not in supermarket.keys():
        supermarket[item_name.strip()] = int(item_price)
    else:
        supermarket[item_name.strip()] += int(item_price)

for v in supermarket.keys():
    print(v + ' ' + str(supermarket.get(v)))

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
ordered_input = OrderedDict()
n = int(input())
for counter in range(n):
    inpu = input()
    if inpu in ordered_input.keys():
        ordered_input[inpu] += 1
    else:
        ordered_input[inpu] = 1
print(len(ordered_input.keys()))
print(' '.join([str(x) for x in ordered_input.values()]))

# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
operations_number = int(input())
q = deque() 
for x in range(operations_number):
    operation = input().split()
    if operation[0] == 'append':
        q.append(operation[1])
    if operation[0]== 'pop':
        q.pop()
    if operation[0] == 'popleft':
        q.popleft()
    if operation[0] == 'appendleft':
        q.appendleft(operation[1])
print(' '.join(q))

# Piling Up!
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
def cube_stacker(horiz_cubes):
    left = 0
    right = len(horiz_cubes)-1
    bottom_cube = float('inf')
    
    while left <= right:
        if horiz_cubes[-1] >= horiz_cubes[0] and horiz_cubes[-1] <= bottom_cube:
            bottom_cube = horiz_cubes.pop()
            right -= 1
        elif horiz_cubes[0] >= horiz_cubes[-1] and horiz_cubes[0] <= bottom_cube:
            bottom_cube = horiz_cubes.popleft()
            left += 1
        else:
            return("No")
    return("Yes")
test_cases = int(input())
for counter in range(test_cases):
    cubes_number = int(input())
    horiz_cubes = deque(map(int,input().split()))
    print(cube_stacker(horiz_cubes))

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = sorted(input())
    cnt = Counter(list(s)).most_common(3)
    
    for item in cnt:
        print (item[0] + ' ' + str(item[1]))

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
mdy = [int(x) for x in input().split()]
days = [x.upper() for x in list(calendar.day_name)]
print(days[calendar.weekday(mdy[2], mdy[0], mdy[1])])

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime
from datetime import timedelta
# Complete the time_delta function below.
def time_delta(t1, t2):
    date = '%a %d %b %Y %H:%M:%S %z'
    
    t1 = datetime.strptime(t1, date)
    t2 = datetime.strptime(t2, date)
    
    delta = abs((t1-t2).total_seconds())
    
    return str((int(delta)))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
cases_number = int(input())
for x in range(cases_number):
    try:
        values = [int(x) for x in input().split()]
        print(values[0] // values[1])
    except ZeroDivisionError as zde:
        print("Error Code:", zde)
    except ValueError as ve:
        print("Error Code:", ve)

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
students = [int(x) for x in input().split()]
students_id = [x for x in range(students[0])]
students_dict = dict()
for subj in range(students[1]):
    zipped = zip(input().split(), students_id)
    for grade in zipped:
        if grade[1] in students_dict.keys():
            students_dict[grade[1]] += float(grade[0])
        else:
            students_dict[grade[1]] = float(grade[0])
for ids in students_id:
    print(students_dict.get(ids) / students[1])

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input().strip())
    
    arr_final = sorted(arr, key=lambda x: x[k])
    
    for arr in arr_final:
        print(' '.join(map(str,arr)))

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
to_sort = list(input())
sorted_string_dict = {'upper':[], 'lower':[], 'number':[]}
for char in to_sort:
    if char.isupper():
        sorted_string_dict['upper'].append(char)
    elif char.islower():
        sorted_string_dict['lower'].append(char)
    else:
        sorted_string_dict['number'].append(int(char))
        
for k in sorted_string_dict.keys():
    sorted_string_dict[k] = sorted(sorted_string_dict.get(k))
sorted_string_dict['number'] = sorted(sorted_string_dict.get('number'), key=lambda x: (x%2==0))
final_string = ''.join(sorted_string_dict.get('lower'))+''.join(sorted_string_dict.get('upper'))+''.join(map(str, sorted_string_dict.get('number')))
print(final_string)

# Map and Lambda Function
cube = lambda x: x**3# complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    fibonacci_list = [0,1]
    i=2
    while i < n:
        fibonacci_list.append(fibonacci_list[-2]+fibonacci_list[-1])
        i+=1
    return fibonacci_list

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
iters = int(input())
pattern = re.compile(r'^[-+]?(\d*.\d+)$')
def pattern_checker(s):
    to_check = s
    
    if not pattern.match(to_check):
        return(False)
        
    try:
        float(to_check)
        return(True)
    except ValueError as ve:
        return(False)
for _ in range(iters):
    result = pattern_checker(input())
    print(result)

# Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = re.compile(r'([a-zA-Z0-9])\1')
inp = input()
m = pattern.search(inp)
if m:
    print(m.group(1))
else:
    print(-1)

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
pattern = re.compile(r'(?=([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][aeiouAEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]))')
find = pattern.finditer(s)
entered=0
for f in find:
    print(f.group(1)[1:-1])
    entered = 1
if entered == 0:
    print(-1)

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
k = input()
pattern = re.compile(fr'(?=({k}))')
m = pattern.finditer(s)
entered = 0
for elem in m:
    print((elem.start(1), elem.end(1)-1))
    entered = 1
if entered == 0:
    print((-1, -1))

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = int(input())
text = ''
#pattern = re.compile(r'([&&])([||])')
for _ in range(lines):
    text += input() + '\n'
    
text = re.sub(r"(?<= )&&(?= )", "and", text)
text = re.sub(r'(?<= )\|\|(?= )', 'or', text)
print(text)

# Validating Roman Numerals
regex_pattern = r"^[M]{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
numbers = int(input())
pattern = re.compile(r'(^[789])([0-9]{9})')
for _ in range(numbers):
    inp = input()
    m = pattern.search(inp)
    if m == None or len(inp) > 10:
        print('NO')
    else:
        print('YES')

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = int(input())
pattern = re.compile(r'(^[a-z][a-zA-Z0-9-_.]+)@{1}([a-z]+)[.]([a-z]{0,3}$)')
for _ in range(lines):
    inp = input().split()
    m = pattern.match(inp[1][1:-1])
    
    if m != None:
        print(' '.join(inp))

# Hex Color Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = int(input())
css_block = re.compile(r'({.*?})', re.DOTALL)
valid_css = re.compile(r'(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})')
text = ''
for _ in range(lines):
    text += input() +'\n'
css_validator = css_block.findall(text)
for css_block in css_validator:
    m = valid_css.findall(css_block)
    if m != None:
        [print(x) for x in m]

# HTML Parser - Part 1
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = int(input())
text = ''
parser = re.compile(r'<\s*(/?)([a-zA-Z][a-zA-Z0-9]*)\s*([^>]*?)\s*(/?)>')
parse_attrs = re.compile(r'([a-zA-Z-]+)(?:\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^>\s]+)))?')
comment_remover = re.compile(r'<!--.*?-->', re.DOTALL)
for _ in range(lines):
    inp = input()
    text += inp + '\n'
text = comment_remover.sub('', text) 
matches = parser.finditer(text)
for match in matches:
    closing_tag, tag, attrs, self_close = match.groups()
    if closing_tag:
        print('End   : ' + tag)
    elif self_close:
        print('Empty : ' + tag)
        for attr in parse_attrs.findall(attrs):
            name = attr[0]
            value = None
            for val in attr[1:]:
                if val: value = val
            print(f"-> {name} > {value}")
    else:
        print('Start : ' + tag)
        for attr in parse_attrs.findall(attrs):
            name = attr[0]
            value = None
            for val in attr[1:]:
                if val: value = val
            print(f"-> {name} > {value}")
            
        

# HTML Parser - Part 2
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import re
class Parser(HTMLParser):
    def handle_comment(self, data):
        out = data.strip()
        if '\n' in data:
            print(">>> Multi-line Comment")
            print(out)
        else:
            print(">>> Single-line Comment")
            print(out)
            
    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)
lines = int(input())
text = ''
for _ in range(lines):
    text += input() + '\n'
    
comment = Parser()
comment.feed(text)
    

# Detect HTML Tags, Attributes and Attribute Values
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import re
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for att in attrs:
                print('-> ' + att[0] + ' > ' + att[1])
lines = int(input())
text = ''
for _ in range(lines):
    text += input() + '\n'
parser = MyHTMLParser()
parser.feed(text)

# Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
cases = int(input())
validator = re.compile(r'(?=(?:.*[A-Z]){2,})(?=(?:.*\d){3,})(?!.*(.).*\1)[A-Za-z0-9]{10}$')
for _ in range(cases):
    inp = input()
    if validator.match(inp):
        print('Valid')
    else:
        print('Invalid')

# XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    score = len(node.attrib.keys())
    for eleme in node:
        if len(eleme) > 0:
            for gc in eleme:
                score += len(gc.attrib.keys())
        score += len(eleme.attrib.keys())
    return score

# XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    level += 1
    if level > maxdepth:
        maxdepth = level
    for attrib in elem: 
        depth(attrib, level)
    

# Standardize Mobile Number Using Decorators
import re
def wrapper(f):
    def fun(l):
        # complete the function
        parser = re.compile(r'(\+?.{0,2})([0-9]{5})([0-9]{5})')
        formatted = []
        for number in l:
            numb = parser.findall(number)
            formatted.append('+91 ' + numb[0][1] + ' ' + numb[0][2])
        return f(formatted)
    return fun

# Decorators 2 - Name Directory

def person_lister(f):
    def inner(people):
        # complete the function
        sorted_people = sorted(people, key=lambda x: int(x[2]))
        return [f(person) for person in sorted_people]
    return inner

# Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(arr[::-1], float)

# Shape and Reshape
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
my_list = [int(x) for x in input().strip().split()]
nparr = numpy.array(my_list)
print(numpy.reshape(nparr, (3, 3)))

# Transpose and Flatten
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
rows, colums = map(lambda x: int(x), input().split())
my_list = []
for row in range(rows):
    my_list.append([int(x) for x in input().strip().split()])
nparr = numpy.array(my_list)
print(numpy.transpose(nparr))
print(nparr.flatten())

# Concatenate
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m, p = map(lambda x: int(x), input().strip().split())
arr_1 = [[int(y) for y in input().strip().split()] for x in range(n)]
arr_2 = [[int(y) for y in input().strip().split()] for x in range(m)]
nparr1 = numpy.array(arr_1)
nparr2 = numpy.array(arr_2)
print(numpy.concatenate((nparr1, nparr2), axis=0))

# Zeros and Ones
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
x = [int(x) for x in input().strip().split()]
print(numpy.zeros(x, dtype = numpy.int))
print(numpy.ones(x, dtype = numpy.int))

# Eye and Identity
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
n, m = map(lambda x: int(x), input().strip().split())
if n == m:
    print(numpy.identity(n))
else:
    print(numpy.eye(n, m))

# Array Mathematics
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m = map(lambda x: int(x), input().strip().split())
a = []
tmp = []
for _ in range(n):
    tmp.append([int(x) for x in input().strip().split()])
a = numpy.array(tmp)
tmp = []
for _ in range(n):
    tmp.append([int(x) for x in input().strip().split()])
b = numpy.array(tmp)
print (numpy.add(a,b))
print (numpy.subtract(a,b))
print (numpy.multiply(a,b))
print (numpy.floor_divide(a,b))
print (numpy.mod(a,b))
print (numpy.power(a,b))

# Floor, Ceil and Rint
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
nparr = numpy.array([float(x) for x in input().strip().split()])
print(numpy.floor(nparr))
print(numpy.ceil(nparr))
print(numpy.rint(nparr))

# Sum and Prod
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m = map(lambda x: int(x), input().strip().split())
tmp = []
for _ in range(n):
    tmp.append([int(x) for x in input().strip().split()])
nparr = numpy.array(tmp)
result = numpy.sum(nparr, axis = 0)
print(numpy.prod(result))

# Min and Max
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n, m = map(lambda x: int(x), input().strip().split())
tmp = []
for _ in range(n):
    tmp.append([int(x) for x in input().strip().split()])
    
res = numpy.min(numpy.array(tmp), axis=1)
print(numpy.max(res))

# Mean, Var, and Std
import numpy
n, m = map(lambda x: int(x), input().strip().split())
tmp = []
for _ in range(n):
    tmp.append([float(x) for x in input().strip().split()])
nparr = numpy.array(tmp)
print(numpy.mean(nparr, axis = 1))
print(numpy.var(nparr, axis = 0))
print(round(numpy.std(nparr, axis = None), 11))

# Dot and Cross
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = int(input())
tmp = []
for _ in range(n):
    tmp.append([int(x) for x in input().strip().split()])
nparr = numpy.array(tmp)
tmp = []
for _ in range(n):
    tmp.append([int(x) for x in input().strip().split()])
nparrb = numpy.array(tmp)
print(numpy.dot(nparr, nparrb))

# Inner and Outer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
a = numpy.array([int(x) for x  in input().strip().split()])
b = numpy.array([int(x) for x in input().strip().split()])
print(numpy.inner(a, b))
print(numpy.outer(a, b))

# Polynomials
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
poly = numpy.array([float(x) for x in input().strip().split()])
x = int(input())
print(numpy.polyval(poly, x))

# Linear Algebra
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = int(input())
tmp = []
for _ in range(n):
    tmp.append([float(x) for x in input().strip().split()])
    
nparr = numpy.array(tmp)
print(round(numpy.linalg.det(nparr), 2))

# Validating Credit Card Numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
ccn = []
parser = re.compile(r'^(?!.*(\d)(-?\1){3})[456]\d{3}(-?\d{4}){3}$')
for _ in range(n):
    ccn.append(input())
for number in ccn:
    if parser.match(number):
        print('Valid')
    else:
        print('Invalid')

# Validating Postal Codes
regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"	# Do not delete 'r'.

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    # Write your code here
    mx = max(candles)
    count = 0
    for candle in candles:
        if candle == mx:
            count += 1
    return(count)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x1 > x2 and (v1 > v2 or v1 == v2)) or (x2 > x1 and (v2 > v1 or v1 == v2)):
        return ('NO')
    elif (x1 < x2):
        while(x1 < x2):
            x1 += v1
            x2 += v2
    elif (x2 < x1):
        while(x2 < x1):
            x2 += v2
            x1 += v1
    if x1 == x2:
        return('YES')
    else: return ('NO')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    # Write your code here
    total = 0
    people_reached = 5
    
    for day in range(n):
        total += (people_reached // 2)
        people_reached = (people_reached//2)*3
    
    return total
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    if len(n) == 1:
        return n
    else:
        su = sum([int(x) for x in n])*k
        return(superDigit(str(su), 1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    # Write your code here
    oord = arr[n-1]
    i = n-1
    while i >= 0:
        if i == 0:
            arr[i] = oord
            print(' '.join([str(x) for x in arr]))
            return
        if arr[i-1] < oord:
            arr[i] = oord
            print(' '.join([str(x) for x in arr]))
            return
        else:
            arr[i] = arr[i-1]
            print(' '.join([str(x) for x in arr]))
            i -= 1
            
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    # Write your code here
    for p in range(1, n):
        n = arr[p]
        r = p - 1
        while r >= 0 and n < arr[r]:
            arr[r+1] = arr[r]
            r -= 1
        arr[r+1] = n
        
        print(' '.join([str(x) for x in arr]))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

