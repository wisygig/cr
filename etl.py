import json
import requests


def main():
    url = 'https://dl.dropboxusercontent.com/s/iwz112i0bxp2n4a/5e-SRD-Monsters.json'
    data = json.loads(requests.get(url).text)
    monsters = data[:-1]
    ogl = data[-1]
    return monsters

if __name__ == '__main__':
    main()
