x_axis = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];
% Random forest 
precision_random_forest = [0.41, 0.38, 0.32, 0.56, 0.32, 0.23, 0.41, 0.66, 0.21, 0.12, 0.32, 0.21, 0.44];

% Decision Tree classifier
precision_dec_tree = [0, 0.72, 0.34, 0.18, 0, 0, 0, 0, 0.22, 0.15, 0.29, 0, 0.29];
    
%SVM 
precision_SVM = [0.27, 0.35, 0.27, 0.2, 0.12, 0.26, 0.31, 0.33, 0.24, 0.08, 0.35, 0.4, 0.21];

%KNN
precision_KNN = [0, 0.29, 0.33, 0.2, 0, 0, 0, 0, 0.28, 0.44, 0.27, 0, 0];

%Log Regression
precision_log_reg = [0.18, 0.32, 0.26, 0.27, 0.09, 0.16, 0.26, 0.29, 0.31, 0.07, 0.37, 0.25, 0.22];

% Convolutional NN
precision_CNN = [0.17, 0.38, 0.17, 0.17, 0.10, 0.16, 0.29, 0.23, 0.18, 0.16, 0.35, 0.12, 0.3];

% Fully connected NN
precision_FCNN = [0,0,0,0,0,0,0,0,0,0,0.26,0,0];

scatter(x_axis, precision_random_forest)
hold on
scatter(x_axis, precision_dec_tree, 'o')
scatter(x_axis, precision_SVM, '*')
scatter(x_axis, precision_KNN, 'x')
scatter(x_axis, precision_log_reg, '+')
scatter(x_axis, precision_CNN, 's')
scatter(x_axis, precision_FCNN,'d')

xticks ([1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
xticklabels({'Anger', 'Sad', 'Shame', 'Disgust', 'Anxiety', 'Fear', 'Surprise', 'Contempt', 'Satisfaction', 'WarmHeart', 'Happiness', 'Love', 'Neutral'})
xtickangle(45)