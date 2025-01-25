from queue import Queue
queue = Queue()

def generate_request(number_of_requests):
    for i in range(number_of_requests):
        queue.put(f'Client - {i}')
        print(f'Client - {i} has been added to the queue')
    return queue    

generate_request(10)

def process_request(queue):
    while not queue.empty():
        request = queue.get()
        print(f'{request} has been processed')
    # return queue

process_request(queue)