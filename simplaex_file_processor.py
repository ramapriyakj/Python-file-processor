import socket
import os
import shutil
import datetime

PORT = 9000
BUFFER = 1000
resultFolder = "./result/"
data = []


# Listen to port
def getConnection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(1)
    conn, addr = s.accept()
    return conn


# Process data
def processData(tabdata):
    filepath = resultFolder + str(datetime.datetime.now()) + ".csv"
    f = open(filepath, "w+")
    user_dic = {}
    sum_5 = 0
    for d in tabdata:
        ds = d.split(",")
        sum_5 += int(ds[4])
        if ds[0] not in user_dic:
            user_dic[ds[0]] = [float(ds[2]), int(ds[3]), 1.0]
        else:
            v = user_dic[ds[0]]
            v[0] += float(ds[2])
            v[1] = int(ds[3])
            v[2] += 1.0
    f.write(str(sum_5) + "\n")
    f.write(str(len(user_dic)) + "\n")
    for key, value in user_dic.items():
        f.write(key + "," + str(value[0] / value[2]) + "," + str(value[1]) + "\n")
    f.close()


def process(str):
    global data
    sp = str.split('\n')
    for rec in sp[:-1]:
        data.append(rec)
        if len(data) == BUFFER:
            processData(data)
            data.clear()
    return sp[-1]


# Read data
def start():
    try:
        conn = getConnection()
        print("Connection established..")
        # create result folder
        shutil.rmtree(resultFolder)
        os.mkdir(resultFolder)

        str = ""
        while True:
            str = str + conn.recv(4096).decode()
            if len(str) >= 10000:
                str = process(str)

    finally:
        conn.close()
        print("Connection closed..")


if __name__ == "__main__":
    start()
