%% instantiate the library
disp('Loading the library...');
lib = lsl_loadlib();

% resolve a stream...
disp('Resolving an Audio stream...');
result = {};
while isempty(result)
    result = lsl_resolve_byprop(lib,'type','Audio'); end

% create a new inlet
disp('Opening an inlet...');
inlet = lsl_inlet(result{1});
%%
disp('Now receiving data...');
while true
    % get data from the inlet
    [vec,ts] = inlet.pull_sample();
    % and display it
    fprintf('%.2f\t',vec);
    fprintf('%.5f\n',ts);
end

%%
tic
plot([1 2],[2 2])
close all
plot([2 3],[2 3])
toc


%% 
tic 
p=plot([1 2],[2 2])
p.XData=[2 3]
p.YData=[2 3]


draw now
toc
