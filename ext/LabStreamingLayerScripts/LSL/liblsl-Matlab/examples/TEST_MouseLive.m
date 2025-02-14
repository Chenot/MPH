%% instantiate the library
disp('Loading the library...');
lib = lsl_loadlib();

% resolve a stream...
disp('Resolving an EEG stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'type','Position'); end

% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});
%%
disp('Now receiving data...');
p=plot(1,'ok');
 set(gca,'xlim', [1  1920 ],'Ylim',[ 1        1080])
%set(gca,'Ylim',[ 1        1080])
drawnow
while true
    % get data from the inlet
    [vec,ts] = inlet.pull_sample();
    % and display it
    fprintf('%.2f\t',vec);
    fprintf('%.5f\n',ts);
    
    p.XData=vec(1);
    p.YData=vec(2);
    
    drawnow;
end
