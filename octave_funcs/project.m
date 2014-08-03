%Evan Widloski 2014-07-31
%project a vector onto a subspace
%usage - project([vector]', [basis1]', [basis2]', ... , [basisN])

function projection=project(varargin)
	bases = cell2mat(varargin(2:end));
	vector = cell2mat(varargin(1));
	projection = zeros(size(vector));
	for base=bases
		dot(base,vector);
		projection += (dot(base,vector)/(norm(base)^2))*base;
	endfor
