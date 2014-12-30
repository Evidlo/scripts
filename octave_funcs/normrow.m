%normalized a 2d matrix row by row

function out=normrow(varargin)
	out = [];
	nums = cell2mat(varargin);
	for row = 1:size(nums,1)
		out = [out;norm(nums(row,:))];
	endfor
endfunction
