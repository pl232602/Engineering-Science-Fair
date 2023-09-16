# /usr/bin/bash
sqlite3 -header -csv environmental.db "select * from data;" > data/environmental.csv
sqlite3 -header -csv particle_count.db "select * from data;" > data/particle_count.csv
sqlite3 -header -csv standard.db "select * from data;" > data/standard.csv

