import requests

response = requests.get('https://playground.learnqa.ru/api/hello')

print(response.text)

if __name__ == '__main__':
    name = 'Maks'
    print(f"hello from {name}!")
