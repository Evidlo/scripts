function out=sph2cart(a)
  % [r theta phi] -> [x y z]
  rho = a(1)*sin(a(2));
  out = [rho*cos(a(3)) rho*sin(a(3)) a(1)*cos(a(2))];
endfunction

