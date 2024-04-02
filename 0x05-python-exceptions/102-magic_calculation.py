#!/usr/bin/python3

def magic_calculation(a, b):
    Result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                Result += a ** b / i
        except Exception:
            Result = b + a
            break
    return Result
