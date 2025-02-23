from datetime import datetime

if __name__ == '__main__':
    time = 1740319316542 / 1000
    #      1740319874723
    ts = datetime.fromtimestamp(time)
    print(ts.strftime('%Y-%m-%d %H:%M:%S'))

    now = datetime.now()
    print(int(now.timestamp()*1000))