#!/usr/bin/env python3

import time
import sys


def main():
    try:
        run_time = int(sys.argv[1])
    except IndexError:
        print(
            "Please provide one command line argument which is an integer for minutes that the timer should run."
        )
        return
    except ValueError:
        print(f"Unable to convert argument {sys.argv[1]} to an integer.")

    if run_time < 0:
        print(f"{run_time} for a runtime is invalid. Value must be greater than 0.")
        return

    run_time *= 60
    for remaining in range(run_time, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"{remaining} seconds remaining...")
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rComplete!            \n")
    print("\a")  # beep sound


if __name__ == "__main__":
    main()
