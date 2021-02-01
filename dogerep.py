import requests, time, os, sys, json

url = "https://api.wazirx.com/api/v2/tickers"

data = {}

with open("./data.json") as f:
    data = json.load(f)


def get_curr():
    i = 10
    res = requests.get(url, allow_redirects=True)
    r = res.json()
    value = r["dogeinr"]["last"]
    os.system(f'echo `date "+%T"` {value} >> list.txt')
    while True:
        i = i - 1
        amount = float(value) * data["total-coins"]
        sys.stdout.write(
            f"\n\t\tCurrent rate in inr : ₹{value} \n\t\tTotal Balance left is {amount}"
        )
        people = data["people"]
        for one in people:
            sys.stdout.write(
                f"\n\t\t{one['name']} Balance left is {float(value)*one['coins']}"
            )
        sys.stdout.write(f"\n\t\t{i}s till refresh\n")
        time.sleep(1)
        os.system("clear")
        if i == 0:
            break


def repeat_interval():
    try:
        get_curr()
    except:
        print("\n bye bye")
        exit(0)
    repeat_interval()
