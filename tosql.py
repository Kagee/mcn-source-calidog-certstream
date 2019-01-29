#! /usr/bin/env python3
import sqlite3
import fileinput
import time
import sys

conn = sqlite3.connect('domains.sqlite')
conn.execute('''CREATE TABLE IF NOT EXISTS domains (domain text, UNIQUE(domain));''')

start_time = time.time()

# startup-test
try:
    conn.execute("INSERT INTO domains values ('hild1.no');")
except sqlite3.IntegrityError:
    print("skipped hild1.no")

try:
  prev = "s"
  for line in fileinput.input():
    line = line.strip()
    try:
        conn.execute("INSERT INTO domains values ('{}');".format(line))
        if prev == "s":
            print("")
        print("inserted https://{}.".format(line))
        elapsed_time = time.time() - start_time
        if elapsed_time > 120:
            start_time = time.time()
            conn.commit()
        prev = "i"
    except sqlite3.IntegrityError:
        if prev == "i":
            sys.stdout.write("skipped: ")
        sys.stdout.write(".")
        prev = "s"
except KeyboardInterrupt:
  print("cleanup ...")
  conn.commit()
  conn.close()
  print("cleanup done!")
