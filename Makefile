wave: prepare close
	@python3 wave/main.py
	@gnuplot --persist wave/plots/plot.gnu& > /dev/null 2>&1

graph: prepare
	@python3 graph/main.py &

prepare: clean
	@mkdir -p gens

clean: kill
	@rm -rf gens/
	@ristretto&
	@pkill -f ristretto

nx:
	@evince ~/Downloads/networkx_reference.pdf 2>&1 &

log:
	@git log --all --graph --oneline --decorate 

count:
	@find . -name "*.py" -print0 -o -name "Makefile" -print0 -o -name "*.md" -print0 | xargs -0 wc -l

kill:
	@python3 &
	@pkill -f python3

close:
	@gnuplot&
	@pkill -f gnuplot	