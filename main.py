import api_calls
from stories_mods import ModifiedStory
from iteration_counts import IterationCounts
from confidence_interval import confidence_interval
import datetime
import graphs
import os

"""The actual script that is run

1. Get a list of iterations
2. Get stories from those iterations
3. Make classes from those stories
4. Calculate stats
5. Graphs/
"""

#adjust inputs
project_id = "project:218"
token = os.getenv("CLUBHOUSE_API_TOKEN")
api_url_base = "https://api.clubhouse.io/api/v3/"





api_call_obj = api_calls.ClubhouseService(project_id, api_url_base, token)
iteration_dic_list = api_call_obj.find_iterations(40)
list_storydics = []
modified_story_dics = []
iteration_counts = []
for iteration in iteration_dic_list:
    list_storydics.append(api_call_obj.list_stories_from_iteration(iteration['id']))
for iteration in list_storydics:
    modified_stories = []
    for storyDic in iteration:
        modified_stories.append(ModifiedStory(storyDic))
    modified_story_dics.append(modified_stories)
for iteration in modified_story_dics:
    iteration_counts.append(IterationCounts(iteration))

#print(iteration_counts[0])




#Sprint Summary
print("Sprint Summary:")
print("Total Cards:", iteration_counts[0]['Total Stories'])
print("Total Points:", iteration_counts[0]['Total Story Points'])
print("Features:",iteration_counts[0]['Features'],"Feature Points:",iteration_counts[0]['Feature Points'])
print("Bugs:", iteration_counts[0]['Bugs'], "Bug Points:",iteration_counts[0]['Bug Points'])
print("Chores:",iteration_counts[0]['Chores'],"Chore Points:",iteration_counts[0]['Chore Points'])
print("Carried Over:", iteration_counts[0]['Carry Over Stories'], "Carry Over Points:", iteration_counts[0]['Carry Over Points'])
print("Bonus:", iteration_counts[0]['Bonus Stories'], "Bonus Points:", iteration_counts[0]['Bonus Points'])
print("Unplanned Stories:", iteration_counts[0]['Unplanned Stories'], "Unplanned Points:", iteration_counts[0]['Unplanned Points'])
print("Escalated Stories:", iteration_counts[0]['Escalated Stories'], "Escalated Points:", iteration_counts[0]['Escalated Points'])

#How many points for next sprint?
print(confidence_interval(api_call_obj, 135, .90))
#print(graphs.make_graphs(iteration_counts))
