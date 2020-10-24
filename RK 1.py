from operator import itemgetter

# Дирижёр
class Conductor(): 
    def __init__(self, id, name, lastname, midname, date_of_birth, id_orcester):
        self.id = id
        self.name = name
        self.lastname = lastname
        self.midname = midname
        self.date_of_birth = date_of_birth
        self.id_orcester = id_orcester

# Окестр
class Orchestra():
    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

# Связующая таблица
class CO():
    def __init__(self, cond_id, orc_id):
        self.cond_id = cond_id
        self.orc_id = orc_id

conductors = [
    Conductor(1,"Валерий","Гергиев","Абисалович","02.05.1953",1),
    Conductor(2,"Владимир","Спиваков","Теадорович","12.09.1944",2),
    Conductor(3,"Юрий","Башмед","Абрамович","24.01.1953",1),
    Conductor(4,"Юрий","Темерканов","Хатуевич","10.12.1938",3),
    Conductor(5,"Альгис","Жюрайтис","Марцелович","27.07.1928",2),
    Conductor(6,"Дмитрий","Кобалевский","Борисович","19.12.1904",2)
]

orcestras = [
    Orchestra(1,"Сибирь","Барнаул"),
    Orchestra(2,"Виртуозы Кубани","Краснодар"),
    Orchestra(3,"Русский Сувенир","Сочи")
]

cond_orc = [
    CO(1,1),
    CO(2,2),
    CO(3,1),
    CO(4,3),
    CO(5,2),
    CO(6,2)
]

def main():
        # Соединение данных один-ко-многим 

    #one_to_many = [(c.name, c.lastname, o.name) 
     #   for o in orcestras
      #  for c in conductors
      #  if c.id_orcester == o.id]

    one_to_many=[]
    for c in conductors: 
        for o in orcestras:
            if c.id_orcester == o.id:
                one_to_many.append((c.name, c.lastname, o.name)) 

    print()
    print('Задание Б1')
    print(sorted(one_to_many, key=itemgetter(1)))
    
    # Соединение данных один-ко-многим 
    one_to_many_2 = set()

    for i in orcestras:
        arr = ['', 0]
        for j in conductors:
            if j.id_orcester == i.id:
                if arr[0] == '':
                    arr[0] = i.name
                    arr[1] += 1
                else:
                    arr[1] += 1
                   # continue
        one_to_many_2.add((arr[0], arr[1]))

    print()
    print('Задание Б2')
    print(sorted(one_to_many_2, key=itemgetter(1)))

    many_to_many = {}

    for i in cond_orc:
        length = len(conductors[i.cond_id-1].lastname)
       # print(conductors[i.cond_id-1].lastname[length-1])
        if orcestras[i.orc_id-1].name in many_to_many.keys():
            if conductors[i.cond_id-1].lastname[length-1] == 'в' and conductors[i.cond_id-1].lastname[length-2] == 'о':
                many_to_many[orcestras[i.orc_id-1].name].add((conductors[i.cond_id-1].name, conductors[i.cond_id-1].lastname, conductors[i.cond_id-1].midname))
        else:
            if conductors[i.cond_id-1].lastname[length-1] == 'в' and conductors[i.cond_id-1].lastname[length-2] == 'о':
                many_to_many[orcestras[i.orc_id-1].name] = set()
                many_to_many[orcestras[i.orc_id-1].name].add((conductors[i.cond_id-1].name, conductors[i.cond_id-1].lastname, conductors[i.cond_id-1].midname))

    print()
    print('Задание Б3')
    print(many_to_many)
if __name__ == '__main__':
    main()