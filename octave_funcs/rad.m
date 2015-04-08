%Convert degrees to radians
%rad(deg)

function out=rad(varargin)
	nums = cell2mat(varargin);
	out = (nums/360)*2*pi;
endfunction
