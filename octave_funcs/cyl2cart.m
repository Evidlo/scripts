% adapt coordinate conversion builtins

function out=cyl2cart(a)
  % [rho phi z] -> [x y z]
  out = [a(1)*cos(a(2)) a(1)*sin(a(2)) a(3)];
endfunction

