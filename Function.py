import random
from datetime import datetime
from functools import reduce


names = ['John', 'Maria', 'Irina', 'James', 'Ivan', 'Max', 'Mike',
         'Zeus', 'Boris', 'Teresa', 'Vladimir', 'Alexei', 'Olga',
         'Jessica', 'Kate', 'Mulan', 'Alexander', 'Irma', 'Nick', 'David']

def rnames (names_list, N):
    r_names_list = []
    for i in range(0, N):
        r_names_list.append(random.choice(names_list))
    return r_names_list

Random_names = rnames(names, 100)

def mfreq_name (names_list):
    max_counter = 0
    m_freq_names = []
    for i in names:
        current_counter = names_list.count(i)
        if max_counter < current_counter:
            max_counter = current_counter
    for i in names:
        current_counter = names_list.count(i)
        if current_counter == max_counter:
            m_freq_names.append(i)
    m_freq_names_result = reduce(lambda x, y: x + " and " + y, m_freq_names)
    return m_freq_names_result

def mrare_letters(names_list):
    min_counter = len(names_list)
    m_rare_letters = []
    letters = set(map(lambda x: x[0], names))
    all_first_letters = list(map(lambda x: x[0], names_list))
    for i in letters:
        current_counter = all_first_letters.count(i)
        if min_counter > current_counter and current_counter != 0:
            min_counter = current_counter
    for i in letters:
        current_counter = all_first_letters.count(i)
        if current_counter == min_counter:
            m_rare_letters.append(i)
    m_rare_letters_result = reduce(lambda x, y: x + " and " + y, m_rare_letters)
    return m_rare_letters_result

print("Most frequent names:", mfreq_name(Random_names))

print("Most rare first letters:", mrare_letters(Random_names))

log = open('log', 'r', encoding='utf-8')
log.readline()
last_date = 0

for line in log:
    if last_date == 0:
        last_date = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
    current_date = datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")
    if last_date < current_date:
        last_date = current_date

print('The last date is:', last_date)



