[![YouTube Badge](https://img.shields.io/badge/YouTube-F00?logo=youtube&logoColor=fff&style=for-the-badge)](https://www.youtube.com/watch?v=X52HK2qkiIE&t=6518s)
[![Google Drive Badge](https://img.shields.io/badge/PDF-4285F4?logo=googledrive&logoColor=fff&style=for-the-badge)](https://drive.google.com/file/d/1nskWHtR1ePmrje76k71gdUc2-fcVWvMH/view)
[![Google Colab Badge](https://img.shields.io/badge/Notebook-F9AB00?logo=googlecolab&logoColor=fff&style=for-the-badge)](https://colab.research.google.com/drive/1Dorc5oX43Uh8CbA71KVd4IwfrC6XMeby?usp=sharing)
[![Doc Badge](https://img.shields.io/badge/Read%20the%20Doc-8CA1AF?logo=readme&logoColor=fff&style=for-the-badge)](http://www.stat.yale.edu/Courses/1997-98/101/confint.htm)

## Z-Procedure (Sigma Known)

This procedure is called as **Sigma Known** because for this procedure you have given the **Population Standard Deviation** by default. Generally, population standard deviation is not given for analysis but to work with Z-Procedure you have already provided with Population Standard Deviation.

### **The assumptions for using the Z-procedure in statistical analysis are:**

1. **Random Sampling:** The data must be collected using a random sampling method to ensure that the sample is representative of the population. This helps to minimize biases and ensures that the results can be generalized to the entire population.

2. **Known population standard deviation:** The population standard deviation (σ) must be known or accurately estimated. In practice, the sample standard deviation (s) is often used as an estimate, but if the sample size is large enough, the sample standard deviation can provide a reasonably accurate approximation.

3. **Normal distribution or large sample size:** The underlying population distribution should be normal. However, if the population distribution is not normal, the Central Limit Theorem can be applied when the sample size is large enough _(usually, n ≥ 30 is considered large enough)_. According to the Central Limit Theorem, the sampling distribution of the sample mean will approach a normal distribution as the sample size increases, regardless of the shape of the population distribution.

$$ \text{CI} = \bar{x} \pm Z\_{\alpha/2} \times \frac{\sigma}{\sqrt{n}} $$

> Where, $\bar{x}$ is the sample mean, σ is the population standard deviation, n is the sample size, and Z is the critical value from the standard normal distribution.

## What is (Z α/2) ?

In the formula you provided, $Z_{\alpha/2}$ refers to the critical value or cut-off value from the standard normal distribution , based on the chosen level of confidence and the corresponding significance level, $\alpha$. The symbol $\alpha$ represents the probability of making a Type I error, which is rejecting the null hypothesis when it is actually true. In contrast, the level of confidence represents the degree of certainty or probability that the true population parameter lies within the calculated interval.

For example, if you choose a 95% confidence level, then the value of $\alpha$ would be 0.05, and $Z_{\alpha/2}$ would represent the standard normal score that contains 95% of the area under the curve, leaving 2.5% in each tail. This value can be looked up in a standard normal distribution table or calculated using statistical software . For a 95% confidence level, the value of $Z_{\alpha/2}$ is approximately 1.96.

So, the formula you provided can be interpreted as follows: the confidence interval for the population mean is equal to the sample mean plus or minus the product of the critical value (based on the chosen level of confidence) and the standard error of the mean (which reflects the precision of the sample mean as an estimate of the population mean).
