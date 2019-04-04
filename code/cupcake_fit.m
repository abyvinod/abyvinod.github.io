clear;close all;clc;cvx_clear;

R_platter = 16;
r_cupcake = 2.5;

%% Check for a particular arrangement
    verbose = 1;
    n_cupcake = 30;
    [feas_flag, opt_locations] = cupcake_fit_dc(R_platter, r_cupcake,...
        n_cupcake, verbose);

%% Bisection
%     verbose = 0;
%     n_cupcake_ub = 40;
%     n_cupcake_lb = 0;
% 
%     while n_cupcake_ub > n_cupcake_lb
%         n_cupcake = round((n_cupcake_ub + n_cupcake_lb)/2);
%         fprintf('LB: %2d | UB: %2d\n', n_cupcake_lb, n_cupcake_ub);
%         [feas_flag, opt_locations] = cupcake_fit_dc(R_platter, r_cupcake,...
%           n_cupcake, verbose);
%         if feas_flag
%             % Feasible
%             n_cupcake_lb = n_cupcake;
%             feas_str = '  Feasible';
%             feas_locations = opt_locations;
%         else
%             % Infeasible
%             n_cupcake_ub = n_cupcake-1;
%             feas_str = 'Infeasible';
%         end
%         if verbose
%             fprintf('%4d: %s\n\n\n', n_cupcake, feas_str);
%         else
%             fprintf('\b | Tested: %2d | %s\n', n_cupcake, feas_str);
%         end
%     end
%     fprintf('Found feasible cupcake arrangement with %d cupcakes.\n',n_cupcake_lb);
%     cupcake_fit_dc(R_platter, r_cupcake, n_cupcake_lb, 1);

%% Arrangment via difference of convex programming    
function [feas_flag, opt_locations] = cupcake_fit_dc(R_platter, r_cupcake,...
    n_cupcake, verbose)

    %% Range of theta values for drawing circles
    theta_vec_plot = linspace(0, 2*pi, 100);
    theta_vec = theta_vec_plot(round(linspace(1, 100, n_cupcake)));
    %% Initial guess: Randomly place cupcakes within the plate
    x_iter = (R_platter - r_cupcake)*rand(1,n_cupcake).* [cos(theta_vec);
                                                          sin(theta_vec)];
    %% Difference of convex approach
    continue_condition = 1;
    slack_tol = 1e-8;
    cost_prev = Inf;
    cost_tol = 1e-5;
    tau_iter = 1;
    scaling_tau = 1.1;
    tau_max = 1e4;
    max_iter = 20;
    iter_count = 1;
    
    if verbose
        figure();
    end
    %% Till the convergence condition is met
    while continue_condition
        slack_indx = 1;
        if verbose
            fprintf('%2d. Setting up the CVX problem...\n', iter_count);
        end
        cvx_begin quiet
            variable x(2, n_cupcake);
            variable slack_var(n_cupcake * (n_cupcake-1)/2, 1);
            minimize (tau_iter * sum(slack_var));
            subject to
                slack_var >= 0;
                norm(x(:, 1)) <= R_platter - r_cupcake;
                for cup_indx_1 = 2:n_cupcake
                    norm(x(:, cup_indx_1)) <= R_platter - r_cupcake;
                    if verbose
                        fprintf(' %2d |',cup_indx_1);
                        if abs(cup_indx_1-round(n_cupcake/2))<1e-6
                            fprintf('\n');
                        end
                    end
                    for cup_indx_2 = 1:cup_indx_1-1
                        (x_iter(:, cup_indx_1) - x_iter(:, cup_indx_2))'*...
                           (x_iter(:, cup_indx_1) - x_iter(:, cup_indx_2)) + ...
                           2*[x_iter(:, cup_indx_1)-x_iter(:, cup_indx_2);
                            -(x_iter(:, cup_indx_1)-x_iter(:, cup_indx_2))]'*...
                           [x(:,cup_indx_1) - x_iter(:,cup_indx_1);
                            x(:,cup_indx_2) - x_iter(:,cup_indx_2)] +...
                           slack_var(slack_indx) >= 4 * (r_cupcake)^2;                        
                        slack_indx = slack_indx + 1;                    
                    end
                end
        if verbose
            fprintf('\nSolving the CVX problem...');
            cvx_end
            disp('done');
        else
            cvx_end
        end
        if any(contains({'Solved','Inaccurate/Solved'},cvx_status))
            if verbose
                fprintf(['Status: %s | Sum of slack: %1.3e (should be ~0) | ',...
                    'Change in sum of slack: %1.3e\n'],...
                    cvx_status, sum(slack_var),abs(sum(slack_var) - cost_prev));
                violate_count = zeros(n_cupcake,n_cupcake);
                slack_indx = 1;
                for cup_indx_1 = 2:n_cupcake
                    for cup_indx_2 = 1:cup_indx_1-1
                        %if norm(x(:, cup_indx_1) - x(:, cup_indx_2)) <=...
                            %2 * r_cupcake
                        if slack_var(slack_indx) >= 1e-6
                            violate_count(cup_indx_1, cup_indx_2) = 1;
                            violate_count(cup_indx_2, cup_indx_1) = 1;
                        end
                        slack_indx = slack_indx + 1;
                    end
                end
                clf;
                subplot(1,2,1);spy(violate_count);
                title('Cupcake collision indices');
                subplot(1,2,2);
                plot(R_platter * cos(theta_vec_plot), R_platter * sin(theta_vec_plot));
                hold on;
                for cup_indx = 1:n_cupcake
                    plot(x(1, cup_indx) +r_cupcake*cos(theta_vec_plot),...
                         x(2, cup_indx) +r_cupcake*sin(theta_vec_plot));
                end
                title(sprintf(['Iteration: %d/%d | No. of cupcakes to ',...
                    'fit: %d'], iter_count, max_iter, n_cupcake));
                axis square;drawnow;
            end            
            x_iter = x;
            % STOP if (slack small enough or slack converged) OR max iterations
            % CONTINUE if not of above with ORs replaced with AND
            continue_condition = (sum(slack_var) > slack_tol) &&...
                (abs(sum(slack_var) - cost_prev) > cost_tol) && ...
                (iter_count < max_iter);         
            cost_prev = sum(slack_var);
            iter_count = iter_count + 1;            
        else
            % Impossible to reach here since we are using slack variables
            keyboard;
        end
        tau_iter = min(tau_iter * scaling_tau, tau_max);    
        if verbose
            disp(' ');
        end
    end
    if iter_count > max_iter || (sum(slack_var) > slack_tol) ||...
            (abs(sum(slack_var) - cost_prev) > cost_tol)
        % Reached the maximum iteration but slack still not within
        % tolerance
        feas_flag = 0;
        opt_locations = nan(2, n_cupcake);
    else
        feas_flag = 1;
        opt_locations = x;
    end
end