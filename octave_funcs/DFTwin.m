#!/bin/octave
## Evan Widloski - 2016-11-08

function [X,w] = DFTwin(x,m,l,N)
  ## window = hamming(l);
  X = fftshift(fft(x(m:m+l-1),N));
  w = linspace(-pi,pi,N);
endfunction
