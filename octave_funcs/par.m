%Adds the reciprocals of elements in a provided list and returns the reciprocal of the sum

function out=par(varargin)
	nums = cell2mat(varargin);
	out = sum(nums.^-1)^-1;
endfunction
