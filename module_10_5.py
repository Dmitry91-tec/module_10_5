import datetime
import pprint
import multiprocessing

# time_start2=datetime.datetime.now()
def read_info(name):
    all_data=[]
    # name = 'example1.txt'
    with open(name,encoding='UTF-8') as file:
        for line in file:
            # print(line, end='')
            all_data.append(line)
    # print(all_data)
    return

# filenames = [f'./file {number}.txt' for number in range(1, 5)]
# time_start=datetime.datetime.now()                           #линейный метод
# for name in filenames:
#     read_info(name)
# time_end=datetime.datetime.now()
# res=time_end-time_start2
# print(res)


if __name__ =='__main__':

    with multiprocessing.Pool(processes=4) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        time_start2 = datetime.datetime.now()
        pool.map(read_info, filenames)
        time_end2 = datetime.datetime.now()
        res2=time_end2-time_start2
        print(res2)