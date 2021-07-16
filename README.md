# Predictive_R_Squared
A pythonic solution for calculating predictive r-squared

# TL;DR

This function will calculate the value of Predictive R-Squared. It is used as a means of evaluating the R-Squared/Adj-R-Squared value of the training model, by providing evidence suggestive of model under/overfitting. 


# How it works

In an [RPubs blog post] (https://rpubs.com/RatherBit/102428), Predictive R-Squared is discussed in terms of h ow it was implemented by Tom Hopper. This program uses the following general formula from that post to calculate Predictive R-Squared:

      `predictive R-squared = [1 - (PRESS / SST)] * 100`

This formula requires the calculation of the Predicted Residual Error Sum of Squares (PRESS) statistic, and the Sum of Squares Total (SST). The function first calculates the PRESS statistic. According to *Kutner et al*, the formula for PRESS is as follows:

      ![PRESS](https://github.com/Benischeck/images-formulas/blob/main/PRESS%20formula.JPG?raw=true)





I plan to update this with a more bibliographic-style reference guide, as well as the generic formulas I reference in the description of the function. 

I would love any comments/feedback about the function, particularly as they pertain to the accuracy of my interpretation of the formulas used herein. 



Citations:

Kutner, Michael H., et al. Applied Linear Regression Models. Fourth, McGraw-Hill Irwin, pp. 360, 361, 395.
