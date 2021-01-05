#!/bin/bash
sudo apt-get -y install flex bison libssl-dev python-dev libgmp-dev
wget http://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
tar xf pbc-0.5.14.tar.gz
cd pbc-0.5.14
./configure && make && sudo make install
git clone https://github.com/JHUISI/charm.git
cd charm
./configure.sh && make && sudo make install && sudo ldconfig
rm -rf pbc-0.5.14 pbc-0.5.14.tar.gz charm
