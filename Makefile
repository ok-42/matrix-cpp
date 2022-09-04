all:
	g++ -fPIC -shared -o lib.so cpp/main.cpp cpp/vector.cpp
