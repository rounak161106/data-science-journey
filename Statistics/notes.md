## Log normal Distribution
A random variable is log normally distributed if its logarithm is normally distributed. The probability density function of a log normal distribution is given by:
$$f(x; \mu, \sigma) = \frac{1}{x\sigma\sqrt{2\pi}} e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}}$$
where $\mu$ and $\sigma$ are the mean and standard deviation of the logarithm of the variable, respectively.
Eg. Wealth distribution, stock prices, size of particles in a sample, etc.

### Properties of Log normal Distribution 
- The mean of a log normal distribution is given by $E[X] = e^{\mu + \frac{\sigma^2}{2}}$.
- The variance of a log normal distribution is given by $Var[X] = (e^{\sigma^2} - 1)e^{2\mu + \sigma^2}$.
- The median of a log normal distribution is given by $Median[X] = e^{\mu}$.
- If a variable is log normally distributed and we take natural logarithm of it, we will get a normal distribution. This is useful in many applications, such as modeling stock prices, where the logarithm of the price is often assumed to be normally distributed.
- Similarly, if we have a normal distribution and we take the exponential of it, we will get a log normal distribution. This is useful in many applications, such as modeling the size of particles in a sample, where the size is often assumed to be log normally distributed. 

---

### Note: 
- we have QQ plot to check if a distribution follows normal distribution.

## Power law distribution
A power law distribution is a type of probability distribution that has the form:
$$f(x) = Cx^{-\alpha}$$
where $C$ is a normalization constant, $\alpha$ is the exponent of the power law, and $x$ is the variable of interest. Power law distributions are often used to model phenomena that exhibit a "heavy tail", meaning that there are a large number of small events and a small number of large events. Examples of phenomena that can be modeled with power law distributions include the distribution of wealth, the size of cities, and the frequency of words in a language.
### Properties of Power law distribution
- The mean of a power law distribution is given by $E[X] = \frac{C}{\alpha - 1}$ for $\alpha > 1$.
- The variance of a power law distribution is given by $Var[X] = \frac{C^2}{(\alpha - 1)^2(\alpha - 2)}$ for $\alpha > 2$.
- The median of a power law distribution is given by $Median[X] = C^{\frac{1}{\alpha}}$.
- Power law distributions are often used to model phenomena that exhibit a "heavy tail", meaning that there are a large number of small events and a small number of large events. This is in contrast to normal distributions, which have a "light tail" and are more symmetric around the mean.
- Power law distributions are often used in the study of complex systems, such as social networks, where the distribution of connections between nodes can follow a power law. This is known as a "scale-free" network, where a small number of nodes have a large number of connections, while the majority of nodes have only a few connections.
- Eg. In ipl, 20% of the players score 80% of the runs, in a city, 20% of the people own 80% of the wealth, 80% of crude oil is with 20% of the nations, etc.