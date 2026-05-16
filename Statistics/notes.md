## Log normal Distribution
A random variable is log normally distributed if its logarithm is normally distributed. The probability density function of a log normal distribution is given by:
$$f(x; \mu, \sigma) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}$$
where $\mu$ and $\sigma$ are the mean and standard deviation of the logarithm of the variable, respectively.

### Properties of Log normal Distribution 
- The mean of a log normal distribution is given by $E[X] = e^{\mu + \frac{\sigma^2}{2}}$.
- The variance of a log normal distribution is given by $Var[X] = (e^{\sigma^2} - 1)e^{2\mu + \sigma^2}$.
- The median of a log normal distribution is given by $Median[X] = e^{\mu}$.
- If a variable is log normally distributed and we take natural logarithm of it, we will get a normal distribution. This is useful in many applications, such as modeling stock prices, where the logarithm of the price is often assumed to be normally distributed.