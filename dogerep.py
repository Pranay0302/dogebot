import requests, time, os, sys, json, curses

url = "https://api.wazirx.com/api/v2/tickers"

data = {}

with open("./data.json", "r") as f:
    data = json.loads(f.read())


def get_curr():
    i = 10
    res = requests.get(url, allow_redirects=True)
    r = res.json()
    value = r["dogeinr"]["last"]
    check_and_play(float(value))
    os.system(f'echo `date "+%T"` {value} >> list.txt')
    while True:
        i = i - 1
        amount = float(value) * data["total-coins"]
        stdscr.addstr(0,0,f"\n\t\tCurrent rate in inr : ₹{value} \n\t\tTotal Balance left is {amount}")
        people = data["people"]
        ii=6
        for one in people:
            stdscr.addstr(ii,0,f"\t\t{one['name']} Balance left is {float(value)*one['coins']}")
            ii=ii+1
        stdscr.addstr(ii+1,0,f"\n\t\t{i}s till refresh\n")
        stdscr.refresh()
        try:
            time.sleep(1)
        except:
            print("\n bye bye")
            exit(0)
        if i == 0:
            break


def check_and_play(value):
    if float(value) >= 3:
        os.system("mpg123 ./siren.mp3 &")


def repeat_interval():
    try:
        get_curr()
    except Exception as ex:
        print("\n bye bye")
        exit(0)
    try:
        repeat_interval()
    except:
        pass

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    try:
        repeat_interval()
    except Exception as ex:
        print("\n bye bye")
        exit(0)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
