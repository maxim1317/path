all: clean
	@python3 src/main.py &

clean:
	@python3 &
	@pkill -f python3

nx:
	@evince ~/Downloads/networkx_reference.pdf 2>&1 &