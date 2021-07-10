import random
import os

def build_corpus():
    title_list = {}
    family_name_list = []
    female_name_list = []
    male_name_list = []
    base_dir = os.path.dirname(__file__)
    with open(os.path.join(base_dir, 'data/thai_name/train_label.txt'), 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            txt = line.strip('\n').split('\t')[-1]
            title = txt.split(' ')[0]
            if title not in title_list:
                title_list[title] = 1
            else:
                title_list[title] += 1

    with open(os.path.join(base_dir, 'data/thai_name/family_names.txt'), 'r' , encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            name = line.strip('\n')
            family_name_list.append(name)

    with open(os.path.join(base_dir, 'data/thai_name/male_names.txt'), 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            name = line.strip('\n')
            male_name_list.append(name)

    with open(os.path.join(base_dir, 'data/thai_name/female_names.txt'), 'r', encoding='utf-8') as f:
        for i, line in enumerate(f.readlines()):
            name = line.strip('\n')
            female_name_list.append(name)
    name_list = (family_name_list, male_name_list, female_name_list)

    # filter titles with small frequency
    title_list = [k for k, _ in sorted(title_list.items(), key=lambda x:x[1], reverse=True)][:3]

    return name_list, title_list

def generate_name(titles, name_list):
    family, male, female = name_list
    name_cbn = []
    title = random.choice(titles)
    family_name = random.choice(family)
    name_cbn.append(title); name_cbn.append(family_name)
    if title == 'นาย':
        name_cbn.append(random.choice(male))
    else:
        name_cbn.append(random.choice(female))
    return ' '.join(name_cbn)


def generate_address(isFirst):
    with open("/Users/fenlai/Desktop/SRNet/SRNet-Datagen/Synthtext/data/thai_address/address_corpus.txt", 'r') as f:

        lines = f.readlines().copy()
        firstLines = [lines[i].strip("\n").split("\t")[-1] for i in range(len(lines)) if i % 2 == 0]
        secondLines = [lines[i].strip("\n").split("\t")[-1] for i in range(len(lines)) if i % 2 == 1]

    if isFirst:
        address = random.choice(firstLines)
    else:
        address = random.choice(secondLines)

    return address

def generate_number(digit):
    numbers = [str(random.randint(0, 9)) for i in range(digit)]
    numbers.insert(12, ' '); numbers.insert(10, ' '); numbers.insert(5, ' '); numbers.insert(1, ' ')
    numbers = ''.join(numbers)
    return numbers

def generate_eng_name():
    title_list = ['Mr. ', 'Miss ', 'Mrs. ']
    length = random.randint(6, 15)
    eng_name = random.choices(title_list)
    for i in range(length):
        if i == 0:
            eng_name += chr(random.choices(range(65, 91))[0])
        else:
            eng_name += chr(random.choices(range(97, 123))[0])
    return ''.join(eng_name)


name_list, title_list = build_corpus()

name = generate_name(title_list, name_list)
