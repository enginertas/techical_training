############################ 
#	Monster Game Makefile
#

CFLAGS		= -O2 -Wall -std=c++0x -g
LFLAGS 		=
OBJ			= main.o city.o game.o gamemap.o utils.o monster.o
OBJ_TEST	= test.o city.o game.o gamemap.o utils.o monster.o
OUTPUT 		= game
TEST_OUTPUT	= test

all: $(OBJ)
	g++ $(OBJ) $(CFLAGS) $(LFLAGS) -o $(OUTPUT)

test: $(OBJ_TEST)
	g++ $(OBJ_TEST) $(CFLAGS) $(LFLAGS) -o $(TEST_OUTPUT)

main.o: main.cpp
	g++ $(CFLAGS) -c main.cpp

city.o: city.cpp
	g++ $(CFLAGS) -c city.cpp

game.o: game.cpp
	g++ $(CFLAGS) -c game.cpp

gamemap.o: gamemap.cpp
	g++ $(CFLAGS) -c gamemap.cpp

utils.o: utils.cpp
	g++ $(CFLAGS) -c utils.cpp

monster.o: monster.cpp
	g++ $(CFLAGS) -c monster.cpp

test.o: test.cpp
	g++ $(CFLAGS) -c test.cpp

clean:
	rm -f *.o
	rm -f $(TEST_OUTPUT)
	rm -f $(OUTPUT)

