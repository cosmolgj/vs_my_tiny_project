import logging

logging.basicConfig(filename="mylog.txt", level=logging.INFO)

def hap(a, b):
    ret = a + b
    logging.info("input: {a} {b}, output={ret}")
    return ret

result = hap(3, 4)