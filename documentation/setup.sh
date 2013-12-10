#install grass
sudo apt-get install grass
sudo apt-get install grass-dev

#setup environment variables
export GISBASE="/usr/lib/grass64"
export PATH="$PATH:$GISBASE/bin:$GISBASE/scripts"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$GISBASE/lib"
# for parallel session management, we use process ID (PID) as lock file number:
export GIS_LOCK=$$
# path to GRASS settings file
export GISRC="$HOME/.grassrc6"
export PYTHONPATH="$PYTHONPATH:$GISBASE/etc/python"