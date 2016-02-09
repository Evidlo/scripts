function out = cart2sph(a)
  % [x y z] -> [r theta phi]
  r = hypot(a(1),a(2),a(3));
  out = [r acos(a(3)/r) atan2(a(2),a(1))];
endfunction
