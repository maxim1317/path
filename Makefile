all: clean
	@python3 src/main.py &

clean:
	@python3 &
	@pkill -f python3

nx:
	@evince ~/Downloads/networkx_reference.pdf 2>&1 &

count:
	@find . -name "*.py" -print0 -o -name "Makefile" -print0 -o -name "*.md" -print0 | xargs -0 wc -l	