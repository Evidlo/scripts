% Evan Widloski - 2015-04-16

function fftplot(data)
frequency = 44100; %samples/sec
duration = 8; %sec
bins=length(data);


period_fft = abs(fft(data));
%reflect 2nd half of fft over x=0
mirrored_fft = [period_fft(bins/2 + 1:end);period_fft(1:bins/2)];

fmax=8e3;
bins*(.5 - (fmax/(frequency/2)));
plot(linspace(-fmax,fmax,(fmax/(frequency/2))*bins),mirrored_fft(bins*(.5 - (fmax/frequency))+1:bins*(.5 + (fmax/frequency))))
endfunction
