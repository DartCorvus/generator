# This is random generator of insults

import random

name = input("Print the name: ")

for_resp_1 = ['коррупція', 'зрада', 'зубожіння', 'кумівство', 'анархія', 'крадіжництво', 'олігархія', 'здирництво',
           'душогубство', 'рейдерство']

for_resp_2 = ['жадібності', 'байдужості', 'лицемірства', 'брехні', 'нахабності', 'зневаги']


def generate(item):
    insult = random.choice(item)
    return insult


response = f"При твоїй владі, {name}, у нас чекає тільки {generate(for_resp_1)}, {generate(for_resp_1)} та " \
    f"{generate(for_resp_1)}!"
response2 = f"Ганьба тобі, {name}. Пенсіонери потерпаюсть від твоєї {generate(for_resp_2)}, а діти від " \
    f"{generate(for_resp_2)}!"

list_final = [response, response2]


def generate_final():
    result = random.choice(list_final)
    return result


print(generate_final())
