# /usr/bin/bash
java -jar client-0.0.5.jar convert --output-format=csv environmental.db /data/environmental-dir
java -jar client-0.0.5.jar convert --output-format=csv standard.db /data/standard-dir
java -jar client-0.0.5.jar convert --output-format=csv particle_count.db /data/particle_count-dir
rm environmental.db
rm particle_count.db
rm standard.db

