import api_calls
import numpy as np
import scipy.stats
"""
This is how you would call find_iteration_ids from the api_calls.py file.
api_calls.find_iteration_ids(35)

"""
#print(api_calls.find_iteration_ids(14))

"""This will take an input of .90 and return an interval with
90% confidence of points for the next iteration

Example call print(confidence_interval(135, .95))
135 day lookback, 95% confidence.
"""

def confidence_interval(api_call_obj, lookback_days, confidence):
    #ClubhouseService().find_iteration_ids(lookback_days)
    list_of_iterations = api_call_obj.find_iterations(lookback_days)
    iteration_points_list = []
    for iteration in list_of_iterations:
        iteration_points_list.append(iteration['stats']['num_points_done'])
    a = 1.0 * np.array(iteration_points_list)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    #output_level = confidence * 100
    return_string = "For " + str(confidence) + " the number of points should be between %d and %d " % (m-h, m+h)
    return return_string

