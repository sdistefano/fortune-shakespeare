SHELL := /bin/bash

normal:
	strfile sonnets
	cp {sonnets,sonnets.dat} /usr/share/games/fortunes/
