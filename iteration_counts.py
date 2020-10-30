"""Input a list of story dictionaries, 
return counts for the iteration that will later be used
for display

IN: List of story_classes
OUT: Dictionary of counts
"""



def IterationCounts(iteration_story_list):
    return_dictionary = {
        "Total Stories" : 0,
        "Total Story Points" : 0,
        "Features" : 0,
        "Feature Points" : 0,
        "Bugs" : 0,
        "Bug Points" : 0,
        "Chores" : 0,
        "Chore Points" : 0,
        "Carry Over Stories" : 0,
        "Carry Over Points" : 0,
        "Bonus Stories" : 0,
        "Bonus Points" : 0,
        "Unplanned Stories" : 0,
        "Unplanned Points" : 0,
        "Escalated Stories" : 0,
        "Escalated Points" : 0,
        "Support Stories" : 0,
        "Support Points" : 0,
        "Client Value Stories" : 0,
        "Client Value Points" : 0,
        "Churn Defense Stories" : 0,
        "Churn Defense Points" : 0,
        "Tech Debt Stories" : 0,
        "Tech Debt Points" : 0,
        "Integration Stories" : 0,
        "Integration Points" : 0
        }
    for story_obj in iteration_story_list:
	# Meta, total stories and total points
        return_dictionary["Total Stories"] += 1
        story_points = 0
        if story_obj.estimate != None:
            story_points = int(story_obj.estimate)
            return_dictionary["Total Story Points"] += story_points
            #print("story points:", story_points)
        else:
            print(story_obj.story_id, "has not been estimated!", story_obj.url)
            
            
        
        #breakdown by type of story
        if story_obj.story_type == "feature":
            return_dictionary['Features'] += 1
            return_dictionary['Feature Points'] += story_points
        if story_obj.story_type == "bug":
            return_dictionary['Bugs'] += 1
            return_dictionary['Bug Points'] += story_points
        if story_obj.story_type == "chore":
            return_dictionary['Chores'] += 1
            return_dictionary['Chore Points'] += story_points
labels = {"carryover", "BonusPoints", "unplanned", "escalation", "support"}
for label in labels:
    















        for label in story_obj.labels:
            if label['name'] == "carryover":
                return_dictionary['Carry Over Stories'] += 1
                return_dictionary['Carry Over Points'] += story_points
            # Bonus Points
            if label['name'] == "BonusPoints":
                return_dictionary['Bonus Stories'] += 1
                return_dictionary['Bonus Points'] += story_points
            # Unplanned
            if label['name'] == "unplanned":
                return_dictionary['Unplanned Stories'] += 1
                return_dictionary['Unplanned Points'] += story_points
            # Escalated
            if label['name'] == "escalation":
                return_dictionary['Escalated Stories'] += 1
                return_dictionary['Escalated Points'] += story_points
            # Support
            if label['name'] == "support":
                return_dictionary['Support Stories'] += 1
                return_dictionary['Support Points'] += story_points
            # Client Value
            if label['name'] == "client_value":
                return_dictionary['Client Value Stories'] += 1
                return_dictionary['Client Value Points' ] += story_points
            # Churn Defense
            if label['name'] == "churn_defense":
                return_dictionary['Churn Defense Stories'] += 1
                return_dictionary['Churn Defense Points'] += story_points			
            # Tech Debt
            if label['name'] == "tech_debt":
                return_dictionary['Tech Debt Stories'] += 1
                return_dictionary['Tech Debt Points'] += story_points
                # Which label
            if label['name'] == "integration":
                return_dictionary['Integration Stories'] += 1
                return_dictionary['Integration Points'] += story_points
    return return_dictionary




    """Next Steps 
   for story in story_list:
    for label in label_list_per_story:
        does label exist in my current label list?
            no -> make new instance of label class
            yes -> update
            


   get rid of the big ass FOR loop and make it a loop of labels
    class LabelStats():
    __init__(self, label_name):
    self.label_name = label_name
    self.story_count = 0
    self.point_count = 0
    
    def label_update(self, point_count):
        self.story_count += 1
        self.point_count += point_count

"""