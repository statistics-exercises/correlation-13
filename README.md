# Non-linearly correlated random variables

What you should have seen in the last exercise is that if two random variables X and Y are correlated by some non-linear function ![](https://render.githubusercontent.com/render/math?math=f(x)) this means we can write:

![](https://render.githubusercontent.com/render/math?math=Y=f(X)%2B\delta)

where ![](https://render.githubusercontent.com/render/math?math=\delta) is some random noise term.  In other words, this is a random variable that falls in some range.  Lets consolidate this idea with one final example.  If you press the button you will see two curves appear again.  The equations of these two curves are:

![](https://render.githubusercontent.com/render/math?math=y=sin(4x)-0.1\qquad\textrm{and}y=sin(4x)%2B0.1)

As always your task is to generate 100 random points that lie between these two curves.  And for the final time you should not need to use a conditional (if) statement to complete this task.  You will know how to compute the sine of a quantity using python, however.  The sine of the variable x can be computed using the following command:

````
y = np.sin(x)
````
