import time, os, sys, json, curses, psutil, inspect, requests

url = "https://api.wazirx.com/api/v2/tickers"

data = {}

with open("./data.json", "r") as f:
    data = json.loads(f.read())


def get_curr():
    res = requests.get(url)
    if res.status_code == 200:
        r = res.json()
        value = r["dogeinr"]["last"]
        check_and_play(float(value))
        os.system(f'echo `date "+%T"` {value} >> list.txt')
        amount = float(value) * data["total-coins"]
        stdscr.addstr(3, 5, f"Current rate in inr : ₹{value} \n", curses.A_BOLD)
        stdscr.addstr(4, 5, f"Total Balance left is {amount}", curses.A_BOLD)
        people = data["people"]
        ii = 6
        for one in people:
            balance = float(value) * one["coins"]
            stdscr.addstr(ii, 5, f"{one['name']}'s Balance left is {balance}")
            amountinvested = float(one["bought-at"])
            state = "gain 📈 " if amountinvested < balance else "loss 📉"
            difference = abs(balance - amountinvested)
            stdscr.addstr(ii + 1, 5, f"{state} of {difference}", curses.A_STANDOUT)
            ii = ii + 3
        time.sleep(10)
        stdscr.refresh()
    else:
        os.system(
            f'echo "url returned {res.status_code} at `date` retrying in 30 seconds" >> run.log'
        )
        time.sleep(30)


def check_and_play(value):
    if float(value) >= 5:
        isRunning = False
        for process in psutil.process_iter():
            if process.name() == "mpg123":
                isRunning = True
                break
        if not isRunning:
            os.system("mpg123 ./siren.mp3 &> /dev/null  &")


def repeat_interval():
    try:
        get_curr()
    except Exception as ex:
        os.system(f'echo "{ex}" >> run.log')
        os.system(
            f'echo "exited from line {inspect.currentframe().f_lineno} at `date`">>run.log'
        )
        exit(0)
    try:
        repeat_interval()
    except Exception as ex:
        os.system(f'echo "{ex}" >> run.log')
        os.system(
            f'echo "exited from line {inspect.currentframe().f_lineno} at `date`">>run.log'
        )


if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.border(0)
    try:
        repeat_interval()
    except Exception as ex:
        # print(ex)
        os.system(
            f'echo "exited from line {inspect.currentframe().f_lineno} at `date`">>run.log'
        )
        exit(0)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
