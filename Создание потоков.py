import time
from time import sleep
import threading



def wite_words(word_count, file_name):

    for word_count in range(1, word_count +1):
        with open(file_name, 'a', encoding='utf-8') as file:
            time.sleep(0.1)
            file.write(f"Какое-то слово № {word_count} \n")
    print(f"Завершилась запись в файл {file_name}")



start = time.time()
a = wite_words(10, 'example1.txt')
b = wite_words(30, 'example2.txt')
c = wite_words(200, 'example3.txt')
d = wite_words(100, 'example4.txt')
end = time.time()
all_time = end - start
hours = int(all_time // 3600)
minutes = int((all_time % 3600) // 60)
seconds = float(all_time % 60)
print(f'Работа потоков {hours}:{minutes}:{seconds}')
start2 = time.time()
thread = threading.Thread(target= wite_words(10, 'example5.txt'))
thread2 = threading.Thread(target= wite_words(30, 'example6.txt'))
thread3 = threading.Thread(target= wite_words(200, 'example7.txt'))
thread4 = threading.Thread(target= wite_words(100, 'example8.txt'))
thread.start()
thread.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()
end2 = time.time()
all_time2 = end2 - start2
hours2 = int(all_time // 3600)
minutes2 = int((all_time % 3600) // 60)
seconds2 = float(all_time % 60)
print(f'Работа потоков {hours2}:{minutes2}:{seconds2}')