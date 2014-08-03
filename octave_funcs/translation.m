%Evan Widloski 2014-08-01
%Convert an augmented matrix into the form X = [translation] + [spanning1] + [spanning2] ... + [spanningN]

function translate=translation(v)
	
	%
	[x,y] = find(v');
	pivot_cols = [1; x(find(diff(x)<0) + 1)];
	translation = v;
	%delete pivot cols from matrix
	translation(:,pivot_cols')=[];
	translation = -1.*translation(:,1:end);


endfunction
