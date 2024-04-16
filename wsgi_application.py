import subprocess
import mysql.connector as s
from flask import Flask

wsgi = Flask(__name__)

passkey = input("Enter SQL Password.....")


def db_setup():

    mycon = s.connect(host='localhost', user='root', passwd=passkey)

    try:
        cursor = mycon.cursor()
        a = "CREATE DATABASE IF NOT EXISTS mc1"
        
        b = "USE mc1"
        
        c = """create table if not exists userdat 
        (id int(11),
        name varchar(50),
        email varchar(100),
        password varchar(255),
        contact varchar(50),
        address varchar(255),
        postal varchar(20),
        state varchar(255))"""

        d = """create table if not exists product
        (pid int(11),
        pname varchar(255),
        rate int(11),
        qty int(11))"""

        e = """create table if not exists cart (
        pid int(11),
        pname varchar(255),
        qty int(11),
        rate int(11),
        price int(11))"""

        f = """create table if not exists orders (
        orderid int(11),
        pids varchar(500),
        uid int(11),
        qty int(11),
        amount int(11),
        date timestamp default current_timestamp)"""

        g = """insert into product (pid, pname, rate, qty)
        values (%s, %s, %s, %s)"""
        cursor.execute(a)

        cursor.execute(b)

        cursor.execute(c)

        cursor.execute(d)

        cursor.execute(e)

        cursor.execute(f)
        st = "select count(*) from product"
        cursor.execute(st)
        data = cursor.fetchone()
        if data[0] == 0:
            cursor.executemany(g, [
                (5539974, 'Adulting', 568, 1943),
                (5855669, 'A Game Of Thrones', 1400, 1974),
                (3433340, 'Nobody killed her', 782, 1976),
                (9723435, 'Koi good news?', 1200, 1978),
                (7934123, 'Belated Batchelor Party', 657, 1981),
                (9905984, 'The Swap', 1115, 1985),
                (9740419, 'Serious Men', 899, 1987),
                (9534068, 'Selection Day', 1299, 2000),
                (9879483, 'White Tiger', 1099, 2000),
                (6125232, 'Indias Most Hunted', 1599, 2000),
                (8985180, 'Cuckold', 599, 2000),
                (7556269, 'Dopehri', 900, 2000),
                (8988083, 'Rumi', 999, 2000),
                (5508137, 'The Forest Enchantments', 1111, 2000),
                (2039368, 'The twentieth wife', 399, 2000),
                (2103901, 'Daura', 799, 2000),
                (6112906, 'The gypsy goddess', 699, 2000),
                (4893843, 'Jorasanko', 979, 2000),
                (6496320, 'The radiance of a thousand suns', 789, 2000),
                (7368334, 'Baaz', 500, 2000),
                (2735922, 'Bhaunri', 349, 2000),
                (8640629, 'Unlikely Adventure of Shergill Sisters', 899, 2000),
                (1258320, 'The far field', 549, 2000),
                (2874756, 'Paper Moon', 790, 2000)])

        mycon.commit()
        print("DATABASE CHECKED")

    except s.Error as fr:
        print(fr)

    finally:
        if mycon.is_connected():
            cursor.close()
            mycon.close()


@wsgi.route('/')
def index():
    return 'STARTED'


if __name__ == '__main__':
    db_setup() 

    runner = subprocess.Popen(['python', 'bridge_main.py'])



    try:
        runner.wait()
    except KeyboardInterrupt:
        runner.terminate()


# This Code has been Written by ss301.
