import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while file.readline() != '':
        line = file.readline()
        all_data.append(line)
    file.close()


filenames = [f'./file_{number}.txt' for number in range(1, 5)]

start_1 = datetime.datetime.now()

for i in filenames:
    read_info(i)

end_1 = datetime.datetime.now()

result_1 = (end_1 - start_1)

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start_2 = datetime.datetime.now()
        pool.map(read_info, filenames)
    end_2 = datetime.datetime.now()
    result_2 = (end_2 - start_2)
    print(f'Резуьтат номер 2: {result_2}')
    print(f'Резуьтат номер 1: {result_1}')

# Видимо я сделал что-то не правильно так как когда выполняю линейным подходом то
# многопроцессный подход требует больше времени если сравнить выполнение без линейного подход и с ним
