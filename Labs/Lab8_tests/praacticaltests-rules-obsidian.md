# CMPS - Data Science
## Lab 8


<div style="page-break-after: always;"></div>
# 0. Review concepts: how do we test

| **Concept**            | **Definition**                                                             | **The Rule"**                                                                                                                               |
| ---------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **P-value**            | Probability of seeing your result _if $H_0$ were true_. Measures surprise. | Small P-value = Big Surprise.                                                                                                               |
| **$\alpha$ (alpha)**   | Your strict decision threshold (default = 0.05).                           |                                                                                                                                             |
| **Core Decision Rule** |                                                                            | **If P-value $\le \alpha$:** Reject $H_0$. Statistically Significant. <br>**If P-value $> \alpha$:** Fail to reject $H_0$. NOT Significant. |

<div style="page-break-after: always;"></div>
# 1. T-test family (Numerical):
| **Use Case Description**                                                                                                    | **Visual Scenario**                     | **T Formula**                                        |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------- |
| **Compare ONE Sample Mean to a Target Value** <br>(e.g., Do these bottles average exactly 500ml?)                           | Sample $\leftrightarrow$ Fixed Target   | $t = \frac{\bar{x} - \mu_0}{(s / \sqrt{n})}$         |
| **Compare means of TWO INDEPENDENT Groups** <br>(e.g., Campaign A Sales $\leftrightarrow$ Campaign B Sales)                 | Group A $\leftrightarrow$ Group B       | $t = \frac{\bar{X}_1 - \bar{X}_2}{SE_{\text{diff}}}$ |
| **Compare scores for the SAME GROUP (DEPENDENT)** <br>(e.g., Test Scores: Before Training $\leftrightarrow$ After Training) | Group $T_1 \leftrightarrow$ Group $T_2$ | $t = \frac{\bar{d} - 0}{(s_d / \sqrt{n})}$           |


<div style="page-break-after: always;"></div>
## Review: T-Distribution

| **Concept**                 | **Definition**                                                                                                                                                                   | **The Rule**                                                                          |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **T-Distribution**          | Similar to normal distribution but with "fatter tails" for smaller sample sizes. Used when standard deviation is unknown. As $n \to \infty$, it becomes the Normal distribution. | It adapts. The larger your $n$, the closer the test gets to a standard normal Z-test. |
| **Degrees of Freedom (df)** | A parameter used to define the specific shape of the test distribution (T, $\chi^2$, F). It’s generally related to sample size ($n$) and the number of groups compared.          | Using code or T-Tables                                                                |

<div style="page-break-after: always;"></div>
![[Pasted image 20260327160232.png]]

<div style="page-break-after: always;"></div>
# 2. Chi Square (Categorical)

| **Use Case Description**                                                                                                                | **Null Hypothesis (H0​) Visual Concept**                             | **The Math Rule (χ2 Formula)**                          |
| --------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------- |
| **Chi-Square Goodness of Fit:**%%  Do observed frequencies match an expected distribution? (e.g., Is traffic equal across all days?) %% | Observed Distribution $\leftrightarrow$ Expected/Target Distribution | $\chi^2 = \sum \frac{(O - E)^2}{E}$                     |
| **Chi-Square Test of Independence:** <br>Are two categorical variables associated or linked? (e.g., Is Plan Type linked to Churn?)      | Variable 1 $\nleftrightarrow$ Variable 2                             | $\chi^2 = \sum \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$ |

<div style="page-break-after: always;"></div>
# 3. ANOVA: One-Way ANOVA (3+ Means)


**When to Use:**
You want to compare the means of three or more independent groups simultaneously. (e.g., Are average conversion rates different across 4 Ad Strategies?)
**Why Not Multiple T-Tests?**
Each t-test has a 5% error rate. Doing 3 t-tests multiplies that risk (Family-Wise Error Rate). ANOVA maintains the overall alpha at your set level (e.g., 0.05).

<div style="page-break-after: always;"></div>
**The Core Mathematical Rule:**
$$F = \frac{MS_{\text{Between}}}{MS_{\text{Within}}}$$
**The Signal / Noise Ratio:**
- **$MS_{\text{Between}}$ (Signal)**: Variation caused by differences between group means. How far are the group averages spread out from the grand average?
- **$MS_{\text{Within}}$ (Noise)**: Variation caused by random scatter within individual groups. How much does the data scatter around its own group mean?
A significant P-value (P $\le \alpha$) means at least one group mean is different. We must follow up with a **Post-Hoc test (like Tukey’s HSD)** to find out exactly which groups differ.

<div style="page-break-after: always;"></div>
# Non- Parametric tests:

| **Parametric Test (Preferred if assumptions met)** | **Non-Parametric Alternative (Use if assumptions violated)** | **Specific Use Case**                  |
| -------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------- |
| Independent t-test                                 | **Mann-Whitney U test**                                      | Compare 2 _independent_ groups         |
| Paired t-test                                      | **Wilcoxon Signed-Rank test**                                | Compare 2 _paired (dependent)_ groups  |
| One-way ANOVA                                      | **Kruskal-Wallis test**                                      | Compare 3+ _independent_ groups        |
| Repeated measures ANOVA                            | **Friedman test**                                            | Compare 3+ _paired (dependent)_ groups |
| Pearson correlation                                | **Spearman correlation**                                     | Measure numerical association          |


<div style="page-break-after: always;"></div>
# Python helpers:

| **Statistical Task / Test Type**          | **Function (scipy.stats)**                        |
| ----------------------------------------- | ------------------------------------------------- |
| **One-Sample T-test**                     | `ttest_1samp(data, target)`                       |
| **Independent T-test**                    | `ttest_ind(data_a, data_b)`                       |
| **Paired T-test**                         | `ttest_rel(before, after)`                        |
| **One-Way ANOVA (F)**                     | `f_oneway(gp1, gp2, gp3, ...)`                    |
| **Chi-Square Goodness of Fit ($\chi^2$)** | `chisquare(obs_counts, exp_counts)`               |
| **Chi-Square Independence ($\chi^2$)**    | `chi2_contingency(cont_table)`                    |
| **Tukey’s HSD (ANOVA Post-hoc)**          | `statsmodels.stats.multicomp.pairwise_tukeyhsd()` |
| **Shapiro-Wilk Test**                     | `shapiro(data)`                                   |
| **Levene’s Test**                         | `levene(gp1, gp2, ...)`                           |
