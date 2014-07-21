#!/usr/bin/octave
%Evan Widloski 2014 - Row Reduced Echelon Form (RREF) calculator
%My first go at an rref calculator.  bad implementation, but it works

function out = mrref(matrix)
	rows = size(matrix)(1);
	cols = size(matrix)(2);
	domain_rows = [1:rows];
	domain_cols = [1:cols];

	for col = domain_cols
		matrix
		nonzero = find(matrix(domain_rows,col) ~= 0);
		if nonzero
			matrix([domain_rows(1) domain_rows(nonzero(1))],:) = matrix([domain_rows(nonzero(1)) domain_rows(1)],:);
			matrix(domain_rows(1),:) ./= matrix(domain_rows(1),col);
			if domain_rows(1) > 1
				matrix(1:domain_rows(1)-1,:) -= matrix(domain_rows(1),:).*matrix(1:domain_rows(1)-1,col);
			end
			if length(nonzero) > 1
				matrix(domain_rows(nonzero(2:end)),:) -= matrix(domain_rows(1),:).*matrix(domain_rows(nonzero(2:end)),col);
			end
			domain_rows = domain_rows(2:end);
		end
	end
	out = matrix;
endfunction
