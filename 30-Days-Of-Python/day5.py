# Day 5 - 30DaysOfPython Challenge

lst = []

fiveItemList = ['pear', 'apple', 'mango', 'pineapple', 'cherry']

print(len(fiveItemList))

print(fiveItemList[0])
print(fiveItemList[len(fiveItemList)//2])
print(fiveItemList[len(fiveItemList)-1])

mixed_data_types = ['Patrick', 23, 178, 'Single', 'Bingfield']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0])
print(len(it_companies)//2)
print(len(it_companies)-1)
it_companies.pop()
it_companies.append('Nvidia')
print(it_companies)
it_companies.append('OpenAI')
it_companies.insert((len(it_companies)//2), 'Anthropic')
print(it_companies[0].upper())
print(it_companies)
print(it_companies[0] + '#; ' + it_companies[1] + '#; ' + it_companies[2] + '#; ' + it_companies[3] + '#; ' + it_companies[4] + '#; ')

if 'Facebook' in it_companies:
    print(True)
else:
    print(False)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[3:])
print(it_companies[:-3])

del it_companies[len(it_companies)//2]
print(it_companies)

del it_companies[0]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies = []
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end + back_end)
full_stack = (front_end + back_end).copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
minAge = ages[0]
print(minAge)
maxAge = ages[len(ages)-1]
print(maxAge)
if len(ages) % 2 == 0:
    medianAge = (ages[len(ages)//2] + ages[(len(ages)//2)-1])/2
    print(medianAge)
else:
    medianAge = ages[len(ages)//2]
    print(medianAge)

summation = 0
for i in range(len(ages)):
    summation += ages[i]
meanAge = summation / len(ages)

print(maxAge - minAge)
print(abs(minAge - meanAge))
print(abs(maxAge - meanAge))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

if len(countries) % 2 == 0:
    print(countries[len(countries)//2] + ' and ' + countries[(len(countries)//2)-1])
    firstHalf = countries[:len(countries)//2]
    print(firstHalf)
    secondHalf = countries[len(countries)//2:]
    print(secondHalf)
else:
    print(countries[len(countries)//2])
    print(countries[len(countries)//2] + ' and ' + countries[(len(countries)//2)-1])
    firstHalf = countries[:(len(countries)//2)+1]
    print(firstHalf)
    secondHalf = countries[(len(countries)//2)+1:]
    print(secondHalf)