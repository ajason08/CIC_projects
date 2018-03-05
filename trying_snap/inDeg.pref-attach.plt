#
# pref-attach. G(3, 3). 0 (0.0000) nodes with in-deg > avg deg (2.0), 0 (0.0000) with >2*avg.deg (Mon Mar 05 11:47:33 2018)
#

set title "pref-attach. G(3, 3). 0 (0.0000) nodes with in-deg > avg deg (2.0), 0 (0.0000) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.pref-attach.png'
plot 	"inDeg.pref-attach.tab" using 1:2 title "" with linespoints pt 6
