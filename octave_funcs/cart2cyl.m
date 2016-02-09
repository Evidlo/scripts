function out = cart2cyl(a)
  % [x y z] -> [rho phi z]
  out = [hypot(a(1),a(2)) atan2(a(2),a(1)) a(3)];
endfunction
