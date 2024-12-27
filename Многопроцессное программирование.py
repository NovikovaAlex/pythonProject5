from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = datetime.now()
    for filename in filenames:
        data = read_info(filename)
    end_time = datetime.now()
    time1 = end_time - start_time
    print(f"Линейное выполнение: {time1} секунд")


    start_time = datetime.now()
    with Pool() as pool:
        results = pool.map(read_info, filenames)
    end_time = datetime.now()
    time2 = end_time - start_time
    print(f"Многопроцессное выполнение: {time2} секунд")
