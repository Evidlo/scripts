#!/usr/bin/octave
%Octave script to graph input from usagelog_parser.py
%Evan Widloski - 2014-06-28


function mins(file)
	hours = [0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23];
	mins = dlmread(file,'\t');
	mins = mins'

	plot(hours,mins,'ro-')
	title('Evan''s Laptop Usage')
	axis([0 23 0 60])
	xlabel('Hour of day')
	ylabel('Average minutes logged in')
	set(gca,'XTick',0:23)
	set(gca,'FontSize',8)
	print -dpng "-S720,640" laptopusage.png
endfunction

function mins3(file)
	data = dlmread(file,' ') ;
	mins = data(:,1:end-1);
	%get every 10th date
	dates = data(1:10:end,end);

	mins_avg = [];
	%rolling average window size
	window = 1;
	%calculate rolling average
	for i = 1:size(mins)(1)-window
		mins_avg = [mins_avg;mean(mins(i:i+window,:))];
	endfor
	xx = 1:size(mins_avg)(2);
	yy = 1:size(mins_avg)(1);

	surf(xx,yy,mins_avg);
	title("Evan's Laptop Usage\n (rolling average)");
	axis([0 length(xx) 0 length(yy) 0 length(mins)]);
	xlabel('Hour of day');
	ylabel('Day');
	colorb = colorbar('eastoutside');
	set(colorb,'Title','Minutes Used');
	caxis([0 60]);
	view(2);
	set(gca,'XTick',0:5:23)
	set(gca,'FontSize',6);
	print -dpng "-S640,720" laptopusage.png -F:6
endfunction

function days(file)
	format={' r',' y','g','c','b','m','k'}
	data = dlmread(file,' ')(:,1:24)
	hour = 1:24;
	length(data)
	length(hour)
	plot(hour,data,format)
	legend('sunday','monday','tuesday','wednesday','thursday','friday','saturday')
	print -dpng "-S640,720" laptopusage.png -F:6
endfunction
	
	

args = argv();
file = args{2};
if strcmp(args{1},'mins')
	mins(file)
endif
if strcmp(args{1},'mins3')
	mins3(file)
endif
if strcmp(args{1},'days')
	days(file)
endif
