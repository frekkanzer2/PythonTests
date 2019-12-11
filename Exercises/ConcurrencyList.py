import concurrent.futures
import multiprocessing


def worker(item, n: int, position: int) -> list:
    newList = list()
    for x in range(n // 10 ** position):
        newList.append(item)
    return newList


def stampalistaPool(lista: list, n: int, concurrency_number: int):
    resultsList = list()
    with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency_number) as executor:
        for i in range(len(lista)):
            myFuture = executor.submit(worker, lista[i], n, i)
            resultsList.append(myFuture.result())
    for item in resultsList:
        print(item)


def stampalistaProcess(lista: list, n: int):
    resultsQueue = multiprocessing.Queue()
    jobsQueue = multiprocessing.JoinableQueue()
    for i in range(len(lista)):
        jobsQueue.put([lista[i], n, i])
        myProcess = multiprocessing.Process(target=worker_p, args=[jobsQueue, resultsQueue])
        myProcess.start()
    jobsQueue.join()
    while not resultsQueue.empty():
        item = resultsQueue.get()
        print(item)


def worker_p(join_queue, result_queue):
    item, n, position = join_queue.get()
    newList = list()
    for x in range(n // 10 ** position):
        newList.append(item)
    result_queue.put(newList)
    join_queue.task_done()


if __name__ == '__main__':
    stampalistaPool(["Abby", "Carmine", "Roxy"], 100, 4)
    print("************************************************************")
    stampalistaProcess(["Abby", "Carmine", "Roxy"], 100)
