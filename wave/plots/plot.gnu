set terminal wxt 0 position 0,0 size 1200,600
# set terminal wxt size 600,600 
set multiplot layout 1, 2 title "Potential algorithm" font ",14"
set tmargin 10
#
set title "Isometric"
set xlabel "x"
set ylabel "y"
set zlabel "potential"

set key outside;
set key center bottom;

set auto
set pm3d
set view 5, 315

set xrange [0:500]
set yrange [0:500]
set zrange [0:3]
set cbrange [0:3]

unset hidden3d
set parametric
splot "gens/plot.txt" u 1:2:3 w pm3d, \
      "gens/path.txt" with lines ls 1 lc rgb "green", \
      "gens/shortenedpath.txt" with lines ls 1 lc rgb "red"
#
set title "Map"
set xlabel "x"
set ylabel "y"
set zlabel "potential"
unset key
set auto
set pm3d map
# set view 5, 315
set xrange [0:500]
set yrange [0:500]
set zrange [0:3]
set cbrange [0:3]

set key outside;
set key bottom;

unset hidden3d
set parametric
splot "gens/plot.txt" u 1:2:3 w image, \
      "gens/path.txt" with lines ls 1 lc rgb "green", \
      "gens/shortenedpath.txt" with lines ls 1 lc rgb "red"
#