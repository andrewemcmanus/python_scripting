hello_file = open("hello.txt", "w")
# enable overwriting with W
ga_intro = "Hello to all of my GA family!"
hello_file.write(ga_intro)
# text_list = hello_file.read()
# print(text_list)

hello_file.close()

car_file = open("cars.txt", 'w')
new_car_list = 'Tesla Model S\nMercedes C300\nToyota Camry'
car_file.write(new_car_list)
car_file.close()

#  create a new file:
my_new_file = open('person.txt', 'w')
my_new_file.write('Andrew McManus')
my_new_file.close()

# person_file = open('person.txt')
# print(person_file.read())
# person_file.close()

with open('person.txt', 'w') as person_file:
    person_file.write('Pete Macaluso')

# "a" for Append:
with open('person.txt', 'a') as person_file:
    person_file.write('\nMike\nDexter')

# with open('person.txt', 'r+') as person_file:
#     print(person_file.read())
#     person_file.write('\nYvonne')
#     print(person_file.read())

with open('person.txt') as people:
    people_list = people.readlines()
    for each_person in people_list:
        print(each_person)

with open('prime_numbers.txt') as primes:
    string = primes.read()
    list = string.split('\n')
    nums = []
    for i in range(len(list)):
        if list[i] == '':
            nums.pop()
        else:
            integer = int(list[i])
            number = integer * 2
            nums.append(number)
    print(nums)

with open('textnums.txt') as textnums:
    string = textnums.read()
    list = string.split('\n')
    written_nums = []
    for i in range(len(list)):
        item = list[i]
        if 'Five' in item:
            written_nums.append(list[i])
        elif 'Fifteen' in item:
            written_nums.append(list[i])

    print(written_nums)
