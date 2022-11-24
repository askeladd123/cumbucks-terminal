# time-for-socks / Cum Buck Tycoon
A time management program with a twist; instead of planning what to do, and when to take a break, the program rolls a dice and decides for you.

## Requirements
* python or python3
* libraries listed in [requirement.txt](requirement.txt)
* ```data.py``` file in format below

## data.py
This is a config file you make yourself. It has all the activities the program can choose from. Feel free to add or remove strings, but keep everything else the same:  

```python
work_hard = ["algebra", "english"]
work_easy = ["geometry", "science", "workout"]
tasks_hard = ["find a job"]
tasks_easy = ["wash clothes"]
rewards_small = ["music", "chips", "break 5 min"]
rewards_big = ["break 30 min", "cake"]
```

## Run
To use the program, install libraries with pip, then do ```python main.py```.

## Potential problems
* playsound 1.2.2
  * playing sounds async didn't work in newer versions
  * if you don't mind the delay try turning the second parameter in the ```playsound``` function to ```True```
