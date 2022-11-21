# time-for-socks / Cum Buck Tycoon
A time management program with a twist. Instead of planning what to do, and when to take a break, the program rolls a dice and decides for you.

#### Requirements
* python or python3
* libraries listed in *requirement.txt*

#### Run
To use the program, install libraries with pip, then do ```python main.py```.

#### Problems
* playsound 1.2.2
  * playing sounds async didn't work in newer versions
  * if you don't mind the delay try turning the second parameter in the ```playsound``` function to ```True```
