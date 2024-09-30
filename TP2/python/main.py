"""
Code for the exercice 1 of TP2 Statistiques Inferentielles Module

"""


import numpy as np
from scipy.stats import norm
# One python equivalent of t.test
import statsmodels.api as sms

# Several display library are possible
# plotly
# seaborn
# matpotlib

import plotly.express as px



def confidence_interval(sample, sigma, alpha):
    """Confidence interval of the mean (MU) of a sample coming from independent identically distributed variables
    :param sample: sample drawn
    :type sample: (N,) ndarray where N is the sample size
    :param sigma:
    :type sigma:
    :param alpha: confidence level (between 0 and 1)
    :type alpha: float
    :return: confidence interval
    :rtype: tuple
    """
    ci = (
        np.mean(normal_sample,axis=1) - (norm.ppf(1 - alpha / 2) * sigma / np.sqrt(sample.shape[1])),
        np.mean(normal_sample,axis=1) + (norm.ppf(1 - alpha / 2) * sigma / np.sqrt(sample.shape[1])),
    )
    return ci


def proportion_in(mean_value, conf_intervals):
    """ Proportion the real mean value is inside the mean confidence interval
    :param mean_value:
    :type mean_value:
    :param conf_intervals:
    :type conf_intervals:
    :return:
    :rtype:
    """
    in_interval = np.logical_and(
        (mean_value >= conf_intervals[0]), (mean_value <= conf_intervals[1])
    )
    proportion_in = len(in_interval[in_interval == True]) / len(conf_intervals[0])
    return proportion_in



if __name__ == "__main__":


    from constants import MU, SIGMA, SAMPLE_SIZE, NB_SAMPLES

    normal_sample = np.random.normal(MU, SIGMA, SAMPLE_SIZE)

    fig = px.histogram(normal_sample,)
    fig.update_layout(bargap=0.2)
    fig.show()

    # # for the second part of the exercise
    # # conf_interval_95 = sms.DescrStatsW(normal_sample).tconfint_mean()
    # # # compute confidence interval 90 percent
    # # conf_interval_90 = sms.DescrStatsW(normal_sample).tconfint_mean(alpha=0.1)
    #
    # # Small trick to broadcast (ease the computing)
    #
    # normal_sample = normal_sample[np.newaxis, ...]
    #
    # # Compute confidence interval using direct formula when SIGMA is known
    # conf_interval_95 = confidence_interval(normal_sample, SIGMA, 0.05)
    # conf_interval_90 = confidence_interval(normal_sample, SIGMA, 0.1)
    #
    # print(conf_interval_95)
    # print(conf_interval_90)
    #
    # normal_samples = np.random.normal(MU, SIGMA, (NB_SAMPLES, SAMPLE_SIZE))
    #
    # conf_intervals_95 = confidence_interval(normal_samples, SIGMA, 0.05)
    # conf_intervals_90 = confidence_interval(normal_samples, SIGMA, 0.1)
    #
    # print(proportion_in(MU, conf_intervals_95))
    # print(proportion_in(MU, conf_intervals_90))







#
# Remark dimensions are reversed to use sms.DescrStatsW()
normal_samples = np.random.normal(MU, SIGMA, (SAMPLE_SIZE, NB_SAMPLES))

prop_095 = proportion_in(MU, normal_samples,alpha=0.05)
prop_090 = proportion_in(MU, normal_samples, alpha=0.1)
print(prop_095)
print(prop_090)