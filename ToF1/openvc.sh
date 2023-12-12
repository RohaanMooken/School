#!/bin/bash

git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git

mkdir ~/opencv/build

cd ~/opencv/build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
Row 5 - Cell 0	-D CMAKE_INSTALL_PREFIX=/usr/local \
Row 6 - Cell 0	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
Row 7 - Cell 0	-D ENABLE_NEON=ON \
Row 8 - Cell 0	-D ENABLE_VFPV3=ON \
Row 9 - Cell 0	-D BUILD_TESTS=OFF \
Row 10 - Cell 0	-D INSTALL_PYTHON_EXAMPLES=OFF \
Row 11 - Cell 0	-D OPENCV_ENABLE_NONFREE=ON \
Row 12 - Cell 0	-D CMAKE_SHARED_LINKER_FLAGS=-latomic \
Row 13 - Cell 0	-D BUILD_EXAMPLES=OFF ..

make -j$(nproc)

sudo make install

sudo ldconfig
