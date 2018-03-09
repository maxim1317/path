all: clean
	@python3 src/main.py &

clean:
	@python3 &
	@pkill -f python3 