# set term wxt position 0,0 size 955,540
# set pm3d
set rmargin 5
set title "Approximate"
set xlabel "x"
set ylabel "y"
set zlabel "potential"
# set autoscale
# splot "gens/plot.txt" u 1:2:3 with lines
# set mapping cartesian
# set style data lines
set auto
# set dgrid3d 50,50 
# set isosamples 500, 500
set pm3d map
# set view 1, 45      

unset hidden3d
set parametric
splot "gens/plot.txt" u 1:2:3 w pm3d, \
      "gens/path.txt" with lines ls 1 lc rgb "green", \
      "gens/shortenedpath.txt" with lines ls 1 lc rgb "red", \
      "gens/circlelist.gen" u 1:2:3:(13.0) with circles lw 2 lc rgb "black"
