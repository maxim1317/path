all: prepare
	@python3 src/main.py &

prepare: clean
	@mkdir -p gens

clean:
	@rm -rf gens/
	@ristretto&
	@pkill -f ristretto

nx:
	@evince ~/Downloads/networkx_reference.pdf 2>&1 &

count:
	@find . -name "*.py" -print0 -o -name "Makefile" -print0 -o -name "*.md" -print0 | xargs -0 wc -l	

kill_python:
	# @python3 &
	# @pkill -f python3