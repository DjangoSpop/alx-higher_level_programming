#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        return a + b
    else:
        result = 0
        for i in range(4, 6):
            result += a ** i
        return result

if __name__ == "__main__":
    import dis
    dis.dis(magic_calculation)
