# Day 18  - 30DaysOfPython Challenge
import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_pattern = r'\w+'
lst = re.findall(regex_pattern,paragraph)
counts = {}
for word in lst:
    if not word in counts:
        counts[word] = 1
    else:
        counts[word] += 1
count_lst = list(counts.items())
sorted_lst = sorted(count_lst,key=lambda x:x[1],reverse=True)
print(sorted_lst)
        
sentence = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
regex_pattern = r'-?\d+'
points_str = re.findall(regex_pattern,sentence)
points = []
for item in points_str:
    points.append(int(item))
points.sort()
sorted_points = points
distance = abs(int(sorted_points[0]) - int(sorted_points[-1]))
print(distance)

def is_valid_variable(string: str) -> bool:
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

    if re.match(regex_pattern,string) == None:
        return False
    else:
        return True

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
regex_pattern = r'[^a-zA-Z ]'
cleaned_sentence = re.sub(regex_pattern, '', sentence)
words = cleaned_sentence.split()
print(words)
counts = {}
for word in words:
    if word.lower() in counts:
        counts[word.lower()] += 1
    else:
        counts[word.lower()] = 1
counts_lst = list(counts.items())
sorted_lst = sorted(counts_lst, key = lambda x:x[1], reverse=True)
print(sorted_lst)