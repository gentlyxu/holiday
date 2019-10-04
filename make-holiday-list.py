import requests
import datetime
import os


def main():
    date_begin = datetime.date(2019, 10, 1)
    date_end = datetime.date(2020, 2, 1)

    delta = datetime.timedelta(days=1)
    d = date_begin
    while d < date_end:
        f1 = d.strftime("%Y-%m-%d")
        f2 = d.strftime("%Y/%m/%d.json")
        os.makedirs(os.path.dirname(f2), 0o777, True)
        result = requests.get("http://timor.tech/api/holiday/info/{}".format(f1))
        if result.content[8] == 48:
            fp = open(f2, "wb", 0)
            fp.write(result.content)
            fp.close()
        else:
            print(result.content)

        d += delta


if __name__ == '__main__':
    main()
