import pandas as pd
import numpy as np
from scipy import stats # for the cdf and the sf functions (t-distribution and chi2 distribution)


class ParametricTests:
    """
    A class that implements basic statistical tests FROM SCRATCH
    using pandas and basic Python only (no scipy, no statsmodels).
    """

    # =========================================================
    # -------------------- Helper Functions -------------------
    # =========================================================

    def sample_mean(self, data: pd.Series) -> float:
        """Return the sample mean."""
        # TODO.1: implement using pandas
        pass

    def sample_std(self, data: pd.Series) -> float:
        """Return the sample standard deviation (ddof=1)."""
        # TODO.2: implement using pandas(remember the ddof=1 for sample std)
        pass

    # =========================================================
    # ---------------- One-Sample t-Test ----------------------
    # =========================================================

    def one_sample_t_stat(self, data: pd.Series, mu0: float) -> tuple[float, int]:
        """
        Compute the t-statistic for a one-sample t-test.

        t = (x_bar - mu0) / (s / sqrt(n))
        dof
        """
        # TODO.3:
        # 1) compute mean
        # 3) compute standard error
        # 4) return t and dof (degree of freedom)
        pass

    # =========================================================
    # ------------- Two Independent Samples t-Test ------------
    # =========================================================

    def two_sample_t_stat(self, data1: pd.Series, data2: pd.Series) -> tuple[float, int]:
        """
        Compute the t-statistic for two independent samples.

        t = (x1 - x2) / SE
        """
        # TODO.4:
        # 1) compute mean1 and mean2
        # 2) compute std1 and std2
        # 3) compute SE = sqrt( (s1^2/n1) + (s2^2/n2) )
        # 4) return t and dof (degree of freedom)
        pass

    # =========================================================
    # -------------------- Paired t-Test ----------------------
    # =========================================================

    def paired_t_stat(self, before: pd.Series, after: pd.Series) -> tuple[float, int]:
        """
        Compute the t-statistic for a paired t-test.
        """
        # TODO.5:
        # 1) compute difference = after - before
        # 2) run one-sample t-test on the difference with mu0 = 0
        # 3) return t and dof (degree of freedom) of the one-sample t-test
        pass
   
    # =========================================================
    # --------------------- Decision Rule ---------------------
    # =========================================================

    def make_decision(self, t_stat: float, dof: int, tailing:str = "one_tailed", alpha: float = 0.05) -> tuple[float, bool]:
        """
        Return True if we reject H0.
        """
        # TODO.6:
        # use t-stat to get the p_value using the cumulative distribution function (cdf) of the t-distribution with the appropriate dof
        # check the hypothesis based on the tailing and alpha setting
        # return True if p-value < alpha (e.g., 0.05) for each case separately (two_tailed, one-tailed)

        if tailing == "one_tailed":
            pass  # One-tailed test
        else:
            pass # Two-tailed test
        #return p_val, p_val < alpha


        
    # =========================================================
    # -------------------- Goodness of Fit --------------------
    # =========================================================
    def chi_goodness_fit(self, observed: pd.Series, expected: pd.Series) -> tuple[float, int, float]:
        """
        Compute the chi-square statistic for goodness of fit.

        chi2 = sum((observed - expected)**2 / expected)
        dof = k - 1
        p_value = P(Chi2 > chi2_statistic) where Chi2 ~ chi2(dof) , use the 'survival function' (sf) for the distribution lookup.
        return chi2_statistic, dof, p_value
        """
        # TODO.7:
        # 1. Compute chi-square statistic
        # 2. Degrees of Freedom: (Number of categories - 1)
        # 3. P-value: use the 'survival function' (sf) for the distribution lookup.
        # 4. calculate the decision rule based on the p-value and alpha
        #return chi_stat, dof, p_value

        pass

    def chi2_independence(self, feature1: pd.Series, feature2: pd.Series):
        """
        Performs Chi-square test of independence between two categorical variables.
        
        Parameters
        ----------
        feature1 : pandas Series
        feature2 : pandas Series
        alpha : float, optional (default=0.05)
        
        Returns
        -------
        chi2_stat : float
        p_value : float
        dof : int
        expected : DataFrame
        """
        # 1) Contingency table (Observed values)
        observed = pd.crosstab(feature1, feature2)

        # 2) Row totals, column totals, grand total
        row_totals = observed.sum(axis=1)
        col_totals = observed.sum(axis=0)
        grand_total = observed.values.sum()

        # 3) Expected values
        expected = np.outer(row_totals, col_totals) / grand_total
        expected = pd.DataFrame(expected, 
                                index=observed.index, 
                                columns=observed.columns)
        #TODO.8:
        # 4) Chi-square statistic

        # 5) Degrees of freedom

        # 6) p-value

        #return chi2_stat, p_value, dof, expected
        pass