from random import *
from utils import *
from time import *
from playsound import playsound
from settings import *
from data import *

# variables
CUM_BUCK_INTERVAL = SOCK_COMMON_WAIT_SECS / SOCK_PRICE_COMMON
cum_bucks = 0
activity = choice(work_hard)
start = time()

# branches
def got_continue():
    print(f"You found nothing, go back to {activity}.")

def got_work_easy():
    global activity
    work = choice(work_easy)
    playsound("res/success.mp3", False)
    print(
        f"You found some easy work: {work}. "
        f"\n\tDo this instead of {activity}")
    activity = work

def got_work_hard():
    global activity
    work = choice(work_hard)
    playsound("res/success.mp3", False)
    print(
        f"You found some hard work: {work}"
        f"\n\tDo this instead of {activity}."
    )
    activity = work

def got_task_easy():
    global cum_bucks, start
    task = choice(tasks_easy)
    print(f"You found an easy task: {task}")

    print(f"\tWrite -> done <- when you're done "
          f"to receive {TASK_EASY_REWARD} CumBucks.")
    done = input()
    while done != "done":
        done = input(f"\t\"{done}\" is not done, try again.\n")
    cum_bucks += TASK_EASY_REWARD
    playsound("res/success.mp3", False)
    print(f"Task done, received {TASK_EASY_REWARD} CumBucks, you now have {cum_bucks}.")
    start = time()

def got_task_hard():
    global cum_bucks, start
    task = choice(tasks_hard)
    print(
        f"You found a hard task: {task}"
        f"\n\tWrite -> done <- when you're done "
        f"to receive {TASK_HARD_REWARD} CumBucks."
    )
    done = input()
    while done != "done":
        done = input(f"\t\"{done}\" is not done, try again.\n")
    cum_bucks += TASK_HARD_REWARD
    playsound("res/success.mp3", False)
    print(f"Task done, received {TASK_HARD_REWARD} CumBucks, you now have {cum_bucks}.")
    start = time()

def got_reward_small():
    rew = choice(rewards_small)
    print("Something sticky...")
    sleep(1)
    playsound("res/success.mp3", False)
    print(f"...yeah, a reward! You got: {rew}")

    done = input(f"\tWrite -> done <- when you're done.\n")
    while done != "done":
        done = input(f"\t\"{done}\" is not done, try again.\n")

    print(f"Go back to: {activity}")

def got_reward_big():
    rew = choice(rewards_big)
    print("Something sticky...")
    sleep(1)
    playsound("res/success.mp3", False)
    print(f"...JACKPOT!!! You got: {rew}")

    done = input(f"\tWrite -> done <- when you're done.\n")
    while done != "done":
        done = input(f"\t\"{done}\" is not done, try again.\n")

    print(f"Go back to: {activity}")

class Sock:
    price = 10
    continue_weight = 1
    work_easy_weight = 1
    work_hard_weight = 1
    task_easy_weight = 1
    task_hard_weight = 1
    reward_small_weight = 1
    reward_big_weight = 1

    def twist(self):
        choices(
            (
                got_continue,
                got_work_easy,
                got_work_hard,
                got_task_easy,
                got_task_hard,
                got_reward_small,
                got_reward_big,
            ),
            weights=(
                self.continue_weight,
                self.work_easy_weight,
                self.work_hard_weight,
                self.task_easy_weight,
                self.task_hard_weight,
                self.reward_small_weight,
                self.reward_big_weight,
            )
        )[0]()

# advanced settings
sock_common = Sock()
sock_common.price = SOCK_PRICE_COMMON
sock_common.continue_weight = 40
sock_common.task_hard_weight = 2
sock_common.work_hard_weight = 4

sock_common.work_easy_weight = 8
sock_common.task_easy_weight = 12

sock_common.reward_small_weight = 16
sock_common.reward_big_weight = 8

sock_rare = Sock()
sock_rare.price = SOCK_PRICE_RARE
sock_rare.continue_weight = 40
sock_rare.task_hard_weight = 2
sock_rare.work_hard_weight = 2

sock_rare.work_easy_weight = 10
sock_rare.task_easy_weight = 14

sock_rare.reward_small_weight = 20
sock_rare.reward_big_weight = 12

sock_legend = Sock()
sock_legend.price = SOCK_PRICE_LEGEND
sock_legend.continue_weight = 40
sock_legend.task_hard_weight = 2
sock_legend.work_hard_weight = 2

sock_legend.work_easy_weight = 10
sock_legend.task_easy_weight = 14

sock_legend.reward_small_weight = 24
sock_legend.reward_big_weight = 18

# main loop
input(
    "If you don't like to think while making decisions, this program is for you. \n"
    "To get you started, here's one free sock.\n"
    "Press -> enter <- to twist the sock."
)

loading(times=1)
print(
    f"You got: {activity}!\n"
    f"\tYou work, you get bucks. Let's go!"
)

while True:
    sleep(CUM_BUCK_INTERVAL)
    while time() - start < CUM_BUCK_INTERVAL:
        sleep(0.1)

    profit = int((time() - start) / CUM_BUCK_INTERVAL)
    start = time()
    cum_bucks += profit
    playsound("res/cash_small.mp3", False)
    print(
        f"\tYou received {profit} CumBuck" + ("." if profit == 1 else "s.")
    )

    if not cum_bucks % sock_common.price:
        playsound("res/cash_big.mp3", False)
        i = input(
            " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
            f"Welcome to the Sock Store. You have {cum_bucks} CumBucks.\n"
            f"\tCommon Sock: {sock_common.price} <- press 1\n"
            f"\tRare Sock: {sock_rare.price} <- press 2\n"
            f"\tLegend Sock: {sock_legend.price} <- press 3\n"
            "\t-> press 0 to leave\n"
            " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - \n"
        )

        while True:
            if i == "0":
                print("Leaving sock store without socks.")
                sleep(1.5)
                break

            elif i == "1":
                cum_bucks -= sock_common.price
                print("You bought a Common Sock.")
                input("\tPress -> enter <- to twist the sock.")
                loading(times=1)
                sock_common.twist()
                sleep(1.5)
                break

            elif i == "2":
                if cum_bucks < sock_rare.price:
                    i = input("\tRare Sock too expensive! Try something else.\n")
                else:
                    cum_bucks -= sock_rare.price
                    print("You bought a Rare Sock.")
                    input("\tPress -> enter <- to twist the sock.")
                    loading(times=1)
                    sock_rare.twist()
                    sleep(1.5)
                    break

            elif i == "3":
                if cum_bucks < sock_legend.price:
                    i = input("\tLegend Sock too expensive! Try something else.\n")
                else:
                    cum_bucks -= sock_legend.price
                    print("You bought a Legendary Sock.")
                    input("\tPress -> enter <- to twist the sock.")
                    loading(times=1)
                    sock_legend.twist()
                    sleep(1.5)
                    break

            else:
                i = input(f"\"{i}\", is not a choice. Try again.\n")
