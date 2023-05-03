[![YouTube Badge](https://img.shields.io/badge/YouTube-F00?logo=youtube&logoColor=fff&style=for-the-badge)](https://www.youtube.com/watch?v=X52HK2qkiIE&t=6518s)
[![Google Drive Badge](https://img.shields.io/badge/PDF-4285F4?logo=googledrive&logoColor=fff&style=for-the-badge)](https://drive.google.com/file/d/1nskWHtR1ePmrje76k71gdUc2-fcVWvMH/view)
[![Google Colab Badge](https://img.shields.io/badge/Notebook-F9AB00?logo=googlecolab&logoColor=fff&style=for-the-badge)](https://colab.research.google.com/drive/1Dorc5oX43Uh8CbA71KVd4IwfrC6XMeby?usp=sharing)
[![Doc Badge](https://img.shields.io/badge/T%20Table-8CA1AF?logo=readme&logoColor=fff&style=for-the-badge)](https://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf)
[![Doc Badge](https://img.shields.io/badge/Read%20the%20Doc-8CA1AF?logo=readme&logoColor=fff&style=for-the-badge)](http://www.stat.yale.edu/Courses/1997-98/101/confint.htm)

## Definition & Intuition

- The **t-distribution** is a probability distribution that is used when estimating the mean of a normally distributed population, but the sample size (n) is small and the population standard deviation (σ) is unknown.
- The t-distribution was introduced by 'William Sealy Gosset', who published under the pseudonym "Student".
- It has heavier tails than the normal distribution and is determined by degrees of freedom, which are closely related to the sample size.
- As the degrees of freedom increase, the t-distribution approaches the normal distribution.
- In hypothesis testing and confidence interval estimation, the t-distribution is used in place of the normal distribution when the sample size (n) is small and the population standard deviation (σ) is unknown.
- Critical t-values are looked up from a t-distribution table to calculate confidence intervals or perform hypothesis tests.

### **The assumptions for using the T-test in statistical analysis are:**

- **Random sampling:** The data must be collected using a random sampling method to ensure that the sample is representative of the population. This helps to minimize biases and ensures that the results can be generalized to the entire population.

- **Sample standard deviation:** The population standard deviation (σ) is unknown, and the sample standard deviation (s) is used as an estimate. The t-distribution is specifically designed to account for the additional uncertainty introduced by using the sample standard deviation instead of the population standard deviation.

- **Approximately normal distribution:** The t-procedure assumes that the underlying population is approximately normally distributed, or the sample size is large enough for the Central Limit Theorem to apply. If the population distribution is heavily skewed or has extreme outliers, the t-procedure may not be accurate, and non-parametric methods should be considered.

- **Independent observations:** The observations in the sample should be independent of each other. In other words, the value of one observation should not influence the value of another observation. This is particularly important when working with time series data or data with inherent dependencies.

$$ \text{CI} = \bar{x} \pm t\_{\alpha/2} \times \frac{s}{\sqrt{n}} $$

## Calculate CI using t-statistic

To calculate Confidence Interval for the population mean (μ) when the sample size (n) is small and the population standard deviation (σ) is unknown is:

$$ t = \frac{\bar{x} - \bar{\mu}}{s/\sqrt{n}} $$

**Where:**

- $\bar{x}$ is the sample mean.
- $\bar{\mu}$ is the hypothesized population mean.
- $s$ is the sample standard deviation.
- $n$ is the sample size.

The t-statistic is used along with the critical t-value obtained from the t-distribution table to calculate the confidence interval for the population mean. The formula for the confidence interval is:

$$ \text{CI} = \bar{x} \pm t \times \frac{s}{\sqrt{n}} $$

**Where:**

- CI is the confidence interval.
- $\bar{x}$ is the sample mean.
- t is the critical t-value obtained from the [t-distribution table](https://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf) for the desired level of confidence.
- s is the sample standard deviation.
- n is the sample size.
