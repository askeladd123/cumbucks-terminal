def loading(times=3, delta_secs=0.5):
    from time import sleep

    for i in range(times):
        print("\r", end=" ")
        sleep(delta_secs)
        print("\r.", end=" ")
        sleep(delta_secs)
        print("\r..", end=" ")
        sleep(delta_secs)
        print("\r...", end=" ")
        sleep(delta_secs)
    print()