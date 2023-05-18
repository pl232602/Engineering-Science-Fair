
import serial 
import sqlite3
from datetime import datetime



def print_serial(name):
    serial_port = serial.Serial(name,115200)
    print(f"The Port name is {serial_port.name}")
    um03=0
    um05=0
    um1=0
    um25=0
    um5=0
    um10=0
    x=0
    while x==0:
        try:
            now=str(datetime.now())
            lines = serial_port.readline()
            lines=str(lines)
            if "(environmental)PM" in lines:
                print(lines)
                line=lines
                index1=line.index("1.0:")+5
                index2=line.index(r"\t\tPM 2.5")
                envpm1=line[index1:index2]
                print(envpm1)
                index3=line.index("2.5:")+5
                index4=line.index(r"\t\tPM 10")
                envpm25=line[index3:index4]
                print(envpm25)
                index5=line.index("10:")+4
                index6=line.index(r"\r\n")
                envpm10=line[index5:index6]
                print(envpm10)
                con1=sqlite3.connect("environmental.db")
                cur=con1.cursor()
                try:
                    cur.execute("CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, datetime varchar(255), pm1 varchar(255), pm2_5 varchar(255), pm10 varchar(255))")
                    print("table created")
                except Exception as error:
                    print(error)
                    print("table exists")
                cur.execute("""INSERT INTO data (datetime,pm1,pm2_5,pm10) VALUES 

                (?,?,?,?)

                """, (now,envpm1,envpm25,envpm10))
                con1.commit()
            elif "(standard)PM" in lines:
                print(lines)
                line=lines
                index1=line.index("1.0:")+5
                index2=line.index(r"\t\tPM 2.5")
                stdnpm1=line[index1:index2]
                print(stdnpm1)
                index3=line.index("2.5:")+5
                index4=line.index(r"\t\tPM 10")
                stdnpm25=line[index3:index4]
                print(stdnpm25)
                index5=line.index("10:")+4
                index6=line.index(r"\r\n")
                stdnpm10=line[index5:index6]
                print(stdnpm10)
                con2=sqlite3.connect("standard.db")
                cur=con2.cursor()
                try:
                    cur.execute("CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, datetime varchar(255), pm1 varchar(255), pm2_5 varchar(255), pm10 varchar(255))")
                    print("table created")
                except Exception as error:
                    print(error)
                    print("table exists")
                cur.execute("""INSERT INTO data (datetime,pm1,pm2_5,pm10) VALUES 

                (?,?,?,?)

                """, (now,stdnpm1,stdnpm25,stdnpm10))
                con2.commit()
            elif "0.3um" in lines:
                line=lines
                index1=line.index("air:")+4
                index2=line.index(r"\r\n")
                um03=line[index1:index2]
                print(um03)
                
            elif "0.5um" in lines:
                line=lines
                index1=line.index("air:")+4
                index2=line.index(r"\r\n")
                um05=line[index1:index2]
                print(um05)
                
            elif "1.0um" in lines:
                line=lines
                index1=line.index("air:")+4
                index2=line.index(r"\r\n")
                um1=line[index1:index2]
                print(um1)
                con=sqlite3.connect("particle_count.db")
                cur
            elif "2.5um" in lines:
                line=lines
                index1=line.index("air:")+4
                index2=line.index(r"\r\n")
                um25=line[index1:index2]
                print(um25)
                
            elif "5.0um" in lines:
                line=lines
                index1=line.index("air:")+4
                index2=line.index(r"\r\n")
                um5=line[index1:index2]
                print(um5)
                
            elif "10.0 um" in lines:
                line=lines
                index1=line.index("air:")+4
                index2=line.index(r"\r\n")
                um10=line[index1:index2]
                print()
                con=sqlite3.connect("particle_count.db")
                cur=con.cursor()
                try:
                    cur.execute("CREATE TABLE data(id INTEGER PRIMARY KEY AUTOINCREMENT, datetime varchar(255), pm0_3 varchar(255), pm0_5 varchar(255), pm1 varchar(255), pm2_5 varchar(255), pm5 varchar(255), pm10 varchar(255))")
                    print("table created")
                except Exception as error:
                    print(error)
                    print("table exists")
                cur.execute("""INSERT INTO data (datetime,pm0_3,pm0_5,pm1,pm2_5,pm5,pm10) VALUES 

                (?,?,?,?,?,?,?)

                """, (now,um03,um05,um1,um25,um5,um10))
                con.commit()
        except TypeError as p:
            print(p)
            pass

print_serial("/dev/ttyACM0")
