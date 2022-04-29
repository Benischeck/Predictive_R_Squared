def pred_r_sq(y_test, y_pred, X):
    """
    Calculates Predictive R-Squared.
    
    Required Arguments: (y_train, y_test, y_pred, X)
    
    y_train - A pandas series derived from the scikitlearn train_test_split module.
    
    y_test - A pandas series derived from the scikitlearn train_test_split module.
    
    y_pred - A pandas series derived from statsmodels predict function
    
    X - A pandas dataframe of independent variables BEFORE they are split using
        the train_test_split module. This function will subset for the indices
        in y_test and y_pred. This may not be necessary, and will be reviewed
        in future editions.
        
        
    This function calculates the Predictive R-Squared value in a number of steps.
    First, it calculates the 'ordinary residuals' by subtracting y_test from y_pred.
    Second, it calculates the diagonal of the hat matrix of X and subsets this to
    the indices of y_test and y_pred. These ordinary residuals and hat matrix are
    used to calculate the 'deleted residuals', which saves us from having to re-fit
    the model for each value in the test set **[1]**.

    The deleted residuals enter the PRESS formula **[2]**. Each value in the series
    is squared, and then the sum of the series is taken to return a scalar, PRESS.

    Next up is the calculation of Sum of Squares Total (SST), which is calculated 
    as the summation of (y_pred - y_train_mean)**2. This is used in the final 
    formula for calculating Predictive R-Squared.
    
    Finally, Predictive R-Squared is calculated as 1-(PRESS/SST). This program
    leaves the output as a decimal rather than percentage form.
    
    **[1]** - Applied Linear Regression Models - Fourth Ed. - Kutner, Nachtsheim,
                Neter (pages 360-361, 395)
                
    **[2]** - https://rpubs.com/RatherBit/102428

    
    Additional Resources:
        - https://blog.minitab.com/en/adventures-in-statistics-2/multiple-regession-analysis-use-adjusted-r-squared-and-predicted-r-squared-to-include-the-correct-number-of-variables
        - https://online.stat.psu.edu/stat501/lesson/10/10.5
        - https://stackoverflow.com/questions/23926496/computing-the-trace-of-a-hat-matrix-from-and-independent-variable-matrix-with-a
        - https://stats.stackexchange.com/questions/208242/hat-matrix-and-leverages-in-classical-multiple-regression
    
    """
    
    #Import pandas and numpy modules
    from pandas import DataFrame
    from pandas import Series
    from numpy import linalg
    from numpy import diagonal
    
    #Calculate the ordinary residuals. These will feed forward into deleted
    #  residuals.
    ordinary_residuals = DataFrame()
    ordinary_residuals = y_pred - y_test
    
    #Calculate the diagonal of the hat matrix. This will feed forward into the 
    #   deleted residuals.
    hat = X.dot(linalg.inv(X.T.dot(X)).dot(X.T))
    hat_diag = diagonal(hat)
    #Subset hat matrix to indices from test set
    hat_diag_df = Series(hat_diag)
    indices = y_pred.index.values.tolist()
    hat_diag_df = hat_diag_df.take(indices = indices)
    
    #Calculate the deleted residuals. These will feed forward into the PRESS
    #  formula
    deleted_residuals = ordinary_residuals / (1 - hat_diag_df)
    
    #Calculate PRESS. This will feed forward into the Predictive R-Squared
    #   formula.
    deleted_residuals_df = DataFrame(deleted_residuals, columns = ['deleted_residuals'])
    PRESS = deleted_residuals_df['deleted_residuals']**2
    PRESS = sum(PRESS)
    
    #Calculate SST. This will feed forward into the Predictive R-Squared formula.
    y_train_mean = sum(y_train) / len(y_train)
    SST = sum((y_test - y_train_mean)**2)
    
    # Calculate Predictive R-Squared
    PRS = ((1-(PRESS/SST)))

    return("Predictive R-Squared: " + str(PRS))
  
