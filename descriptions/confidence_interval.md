[![YouTube Badge](https://img.shields.io/badge/YouTube-F00?logo=youtube&logoColor=fff&style=for-the-badge)](https://www.youtube.com/watch?v=X52HK2qkiIE&t=6518s)
[![Google Drive Badge](https://img.shields.io/badge/PDF-4285F4?logo=googledrive&logoColor=fff&style=for-the-badge)](https://drive.google.com/file/d/1nskWHtR1ePmrje76k71gdUc2-fcVWvMH/view)
[![Google Colab Badge](https://img.shields.io/badge/Notebook-F9AB00?logo=googlecolab&logoColor=fff&style=for-the-badge)](https://colab.research.google.com/drive/1Dorc5oX43Uh8CbA71KVd4IwfrC6XMeby?usp=sharing)
[![Doc Badge](https://img.shields.io/badge/Read%20the%20Doc-8CA1AF?logo=readme&logoColor=fff&style=for-the-badge)](http://www.stat.yale.edu/Courses/1997-98/101/confint.htm)

# Definitions

**Confidence interval**, _in simple words,_ is a range of values within which we expect a particular
population parameter, like a mean, to fall. It's a way to express the uncertainty around an
estimate obtained from a sample of data.

**Confidence level**, usually expressed as a percentage like 95%, indicates how sure we are that
the true value lies within the interval.

$$ \text{Confidence Interval} = \text{Point Estimate} \pm \text{Margin of Error} $$

# Procedures to calculate Confidence Interval

## Z-Procedure (Sigma Known)

This procedure is called as **Sigma Known** because for this procedure you have given the **Population Standard Deviation** by default. Generally, population standard deviation is not given for analysis but to work with Z-Procedure you have already provided with Population Standard Deviation.

### **The assumptions for using the Z-procedure in statistical analysis are:**

1. **Random Sampling:** The data must be collected using a random sampling method to ensure that the sample is representative of the population. This helps to minimize biases and ensures that the results can be generalized to the entire population.

2. **Known population standard deviation:** The population standard deviation (σ) must be known or accurately estimated. In practice, the sample standard deviation (s) is often used as an estimate, but if the sample size is large enough, the sample standard deviation can provide a reasonably accurate approximation.

3. **Normal distribution or large sample size:** The underlying population distribution should be normal. However, if the population distribution is not normal, the Central Limit Theorem can be applied when the sample size is large enough _(usually, n ≥ 30 is considered large enough)_. According to the Central Limit Theorem, the sampling distribution of the sample mean will approach a normal distribution as the sample size increases, regardless of the shape of the population distribution.

### $$ \text{CI} = \bar{x} \pm Z_{\alpha/2} \times \frac{\sigma}{\sqrt{n}} $$

> Where, $\bar{x}$ is the sample mean, σ is the population standard deviation, n is the sample size, and Z is the critical value from the standard normal distribution.

# Interpreting Confidence Interval

A **confidence interval** is a _range of values within which a population parameter_, such as the population mean, is estimated to lie with a certain level of confidence. The confidence interval provides an indication of the precision and uncertainty associated with the estimate. To interpret the confidence interval values, consider the following points:

- **Confidence level:** The confidence level (commonly set at 90%, 95%, or 99%) represents the probability that the confidence interval will contain the true population parameter if the sampling and estimation process were repeated multiple times. For example, a 95% confidence interval means that if you were to draw 100 different samples from the population and calculate the confidence interval for each, approximately 95 of those intervals would contain the true population parameter.

- **Interval range:** The width of the confidence interval gives an indication of the precision of the estimate. A narrower confidence interval suggests a more precise estimate of the population parameter, while a wider interval indicates greater uncertainty. The width of the interval depends on the sample size, variability in the data, and the desired level of confidence.

- **Interpretation:** To interpret the confidence interval values, you can say that you are "X% confident that the true population parameter lies within the range (lower limit, upper limit)." Keep in mind that this statement is about the interval, not the specific point estimate, and it refers to the confidence level you chose when constructing the interval.
