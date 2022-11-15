from random import *
from utils import *
from time import *
from sys import exit
from playsound import playsound

work_hard = ["fysikk", "algoritmer", "software"]
work_easy = ["ai", "skjær"]
tasks_hard = ["timeliste", "meta-analyse"]
tasks_easy = [
    "finne eske til Q35",
    "finne høytaler",
    "push-ups, 50",
    "pull-ups, 24",
    "zalando, 20 min"
    "oppdater plan"
]
rewards_small = [
    "piano",
    "gitar",
    "mw2, 1 runde",
    "paranoid android",
    "snacks",
    "pause 10 min",
    "weird fishes",
    "youtube, 1 video"
]
rewards_big = [
    "better call saul, 1ep",
    "mw2, 3 runder",
    "pause 30 min",
    "pause 20 min"
]

SOCK_PRICE_COMMON = 10
SOCK_COMMON_BORING_WEIGHT = 14
SOCK_COMMON_UPLIFTING_WEIGHT = 3
SOCK_COMMON_SWITCH_WEIGHT = 2
SOCK_COMMON_HAPPY_WEIGHT = 7

SOCK_PRICE_RARE = 50
SOCK_PRICE_LEGEND = 200

TASK_HARD_REWARD = 40
TASK_EASY_REWARD = 5

# SOCK_COMMON_WAIT_SECS = 60 * 15
SOCK_COMMON_WAIT_SECS = 3
CUM_BUCK_INTERVAL = SOCK_COMMON_WAIT_SECS / SOCK_PRICE_COMMON
cum_bucks = 0

input(
    "If you don't like to think while making decisions, this program is for you. \n"
    "To get you started, here's one free sock.\n"
    "Press -> enter <- to twist the sock."
)

activity = choice(work_hard)

loading(times=1)
print(
    f"You got: {activity}!\n"
    f"\tYou work, you get bucks. Let's go!"
)

start = time()
while True:
    sleep(CUM_BUCK_INTERVAL)
    while time() - start < CUM_BUCK_INTERVAL:
        sleep(0.1)

    profit = int((time() - start) / CUM_BUCK_INTERVAL)
    start = time()
    cum_bucks += profit
    playsound("cash_small.mp3", False)
    print(
        f"\tYou received {profit} CumBuck" + ("." if profit == 1 else "s.")
    )

    if not cum_bucks % SOCK_PRICE_COMMON:
        playsound("cash_big.mp3", False)
        i = input(
            " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
            f"Welcome to the Sock Store. You have {cum_bucks} CumBucks.\n"
            f"\tCommon Sock: {SOCK_PRICE_COMMON} <- press 1\n"
            f"\tRare Sock: {SOCK_PRICE_RARE} <- press 2\n"
            f"\tLegend Sock: {SOCK_PRICE_LEGEND} <- press 3\n"
            "\t-> press 0 to leave\n"
            " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
        )

        while True:
            if i == "0":
                print("Leaving sock store without socks.")
                break

            if i == "1":
                cum_bucks -= SOCK_PRICE_COMMON
                print("You bought a Common Sock.")
                input("\tPress -> enter <- to twist the sock.")
                loading(times=1)
                BORING, UPLIFTING, SWITCH, HAPPY = 1, 2, 3, 4

                c = choices(
                    (
                        BORING,
                        UPLIFTING,
                        SWITCH,
                        HAPPY
                    ),
                    weights=(
                        SOCK_COMMON_BORING_WEIGHT,
                        SOCK_COMMON_UPLIFTING_WEIGHT,
                        SOCK_COMMON_SWITCH_WEIGHT,
                        SOCK_COMMON_HAPPY_WEIGHT
                    )
                )[0]

                if c == BORING:
                    print(f"You found a boring old cum stain, go back to {activity}.")
                    break

                if c == UPLIFTING:
                    print(f"\tYou found a nice patch of cum;")
                    input("\t\tPress -> enter <- to go deeper")
                    loading(times=1)
                    if choices((True, False), weights=(len(tasks_easy), len(work_easy)))[0]:

                        task = choice(tasks_easy)
                        print(f"\t\tYou found a sticky task: {task}")

                        print(f"\t\t\tWrite -> done <- when you're done "
                              f"to receive {TASK_EASY_REWARD} CumBucks.")
                        done = input()
                        while done != "done":
                            done = input(f"\t\t\t{done} is not done")
                        cum_bucks += TASK_EASY_REWARD
                        playsound("success.mp3", False)
                        print(f"Task done, received {TASK_EASY_REWARD} CumBucks, you now have {cum_bucks}.")
                        start = time()
                        break

                    else:

                        activity = choice(work_easy)
                        playsound("success.mp3", False)
                        print(f"You found some sticky work: {activity}. Let's go!")
                        break

                if c == SWITCH:
                    print(f"\tYou found something you can live with. ")
                    input("\t\tPress -> enter <- to go deeper")
                    loading(times=1)

                    if choices((True, False), weights=(len(tasks_hard), len(work_hard)))[0]:

                        task = choice(tasks_hard)
                        print(
                            f"\t\tYou found a hard task: {task}"
                            f"\n\t\t\tWrite -> done <- when you're done "
                            f"to receive {TASK_HARD_REWARD} CumBucks."
                        )
                        done = input()
                        while done != "done":
                            done = input(f"\t\t\t{done} is not done")
                        cum_bucks += TASK_HARD_REWARD
                        playsound("success.mp3", False)
                        print(f"Task done, received {TASK_HARD_REWARD} CumBucks, you now have {cum_bucks}.")
                        start = time()
                        break

                    else:
                        work = choice(work_hard)
                        playsound("success.mp3", False)
                        print(
                            f"\t\tYou found some hard work: {work}"
                            f"\nStart doing: {work} instead of {activity}."
                        )
                        activity = work
                        break

                if c == HAPPY:
                    print("not implemented")
                    break

                else:
                    print("wrong input")
                    exit()

            if i == "2":
                print("\tnot implemented")
                break

            if i == "3":
                print("\tnot implemented")
                break

            i = input(f"{i}, is not a choice. Try again.")
