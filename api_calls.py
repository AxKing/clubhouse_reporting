import os
import sys
import requests
import plotly.graph_objects as go
from pprint import pprint
import numpy as np
import scipy.stats
import datetime

"""
This file includes only the Clubhouse API calls
Each Function will have it's inputs and outputs noted



35 days will grab 3 sprints

135 days is 10 sprints 
"""
class ClubhouseService(object):
    def __init__(self, project_id, api_url_base, token):
        self.clubhouse_api_token = "?token=" + token
        self.project_id = project_id
        self.api_url_base = api_url_base

    def list_stories_from_iteration(self, iteration_id):
        query = {'includes_description' : 'true'}
        try:
            url = self.api_url_base + 'iterations/' + str(iteration_id) + '/stories' + self.clubhouse_api_token 
            response = requests.get(url, params = query)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        return response.json()



    def find_iterations(self, lookback_days):
        query = {'query': self.project_id}
        try:
            url = self.api_url_base + "iterations" + self.clubhouse_api_token
            response = requests.get(url, params=query)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)
        search_results = response.json()
        started_iteration = None

        #find current iteration
        for iteration in search_results:
            if iteration['status'] == 'started':
                started_iteration = iteration        
        list_of_iterations = [started_iteration]

        #Set a lookback delta
        current_iteration_time = datetime.datetime.strptime(started_iteration['end_date'], '%Y-%m-%d')
        lookback_delta = datetime.timedelta(days=lookback_days)
        zero_day_delta = datetime.timedelta(days= 0)
        for iteration in search_results:
            other_iterations_time = datetime.datetime.strptime(iteration['end_date'], '%Y-%m-%d')
            iteration_time_difference = current_iteration_time - other_iterations_time
            if (iteration_time_difference <= lookback_delta and iteration_time_difference > zero_day_delta):
                list_of_iterations.append(iteration)
                
        if started_iteration is None:
            raise Exception("Iteration Not Found...")
        else:
            return list_of_iterations
    
