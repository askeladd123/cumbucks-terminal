# time-for-socks / Cum Buck Tycoon
A time management program with a twist; instead of planning what to do, and when to take a break, the program rolls a dice and decides for you! 

This is a terminal program. Check out [time-for-socks-app](https://github.com/askeladd123/time-for-socks-app) for the GUI version.

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

## Tips
To get productive, you have to make a good config file. This is the rule of thumb:
* work hard: 
  * something that takes a long time, and you don't really want to
* work easy:
  * something that takes time, but doesn't feel slow
* tasks hard:
  * something that can be done today, but you don't really want to
* tasks easy:
  * something that can be done now, with low effort
* rewards small:
  * whatever gives you a dopamin refill
* rewards big:
  * something that you look forward to, or that gives your brain some rest

  Remember that it's better to be specific. Doing something hard is easier than deciding on it.
