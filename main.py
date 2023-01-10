from client.cli import run_client
from permission_service.simple_server import run_server

import multiprocessing

if __name__ == '__main__':

    process_1 = multiprocessing.Process(target=run_server)
    process_2 = multiprocessing.Process(target=run_client)
    process_1.start()
    process_2.start()
