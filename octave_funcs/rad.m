%Convert degrees to radians

function out=rad(varargin)
	nums = cell2mat(varargin);
	out = (nums/360)*2*pi;
endfunction
