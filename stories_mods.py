"""This is where all of the stories are modified

"""

"This requires a "
class ModifiedStory(object):
    # Put it all in there and then comment out what you don't need.
    def __init__(self,story_dic):
        self.story_id = story_dic['id']
        self.story_type = story_dic['story_type']
        self.labels = story_dic['labels']
        self.iteration_id = story_dic['iteration_id']
        self.estimate = story_dic['estimate']
        self.url = story_dic['app_url']
    def __repr__(self):
        return f"""Story id: {self.story_id}
        Story type: {self.story_type}
        Iteration ID: {self.iteration_id}
        Story estimate: {self.estimate}
        Labels: {self.labels} \n """