# Day 7 - 30DaysOfPython Challenge

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

other_companies = {'Anthropic', 'OpenAI'}
it_companies.update(other_companies)
print(it_companies)

it_companies.pop()
print(it_companies)

print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

print(A.union(B))

print(B.union(A))

print(A.symmetric_difference(B))

del A

del B

ages_set = set(age)
print(len(age))
print(len(ages_set))

quote = 'I am a teacher and I love to inspire and teach people.'
quote_list = quote.split()
print(quote_list)
print(len(quote_list))
quote_set = set(quote_list)
print(quote_set)
print(len(quote_set))