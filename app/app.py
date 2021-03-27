import requests
import time

def main():
    tikers = ['bitcoin', 'ethereum', 'dogecoin']

    while True:
        for tiker in tikers:
            myapi_req = requests.get(f'http://127.0.0.1:8080/myapi/{tiker}').text
            print(myapi_req)

        print('\n')

        time.sleep(5)

main()