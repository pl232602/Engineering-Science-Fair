# /usr/bin/bash
java -jar client-0.0.5.jar convert --output-format=csv environmental.db environmental-dir
java -jar client-0.0.5.jar convert --output-format=csv standard.db standard-dir
java -jar client-0.0.5.jar convert --output-format=csv particle_count.db particle_count-dir


