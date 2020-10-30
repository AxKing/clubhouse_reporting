import pandas as pd
import datetime
import plotly.express as px
import plotly.graph_objects as go

# one slice: name, color, value
# class pichart
# it has an array of slices and has a render function 
# inside the class def pie_chart([slices]):
# Render the slices

def make_graphs(iteration_counts):
    #colors = ['mediumpurple', 'cyan', 'lightgray', 'pink', 'lightgreen']

    df = pd.DataFrame(data=iteration_counts)
    #print(df)
    #Grouped Bar Graph: Sprint vs Bugs,Features, Chores
    sprint_names = ["Just Finished", "Last Sprint", "Two Sprints Ago"]
    fig = go.Figure(data=[
        go.Bar(name='Features', marker_color= 'mediumpurple', x=sprint_names, y=df.Features),
        go.Bar(name='Bugs', marker_color='cyan', x=sprint_names, y=df.Bugs),
        go.Bar(name='Chores', marker_color='lightgray', x=sprint_names, y=df.Chores)
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.update_layout(title_text='Features, Bugs and Chores by Sprint')
    fig.show()



    #print(df.columns)

    #colors = ['mediumpurple', 'cyan', 'lightgray', 'pink', 'lightgreen']
    sprint_names = ["Just Finished", "Last Sprint", "Two Sprints Ago"]
    fig = go.Figure(data=[
        go.Bar(name='Support', marker_color= 'mediumpurple', x=sprint_names, y=df['Support Stories']),
        go.Bar(name='Client Value', marker_color='cyan', x=sprint_names, y=df['Client Value Stories']),
        go.Bar(name='Churn Defense', marker_color='lightgray', x=sprint_names, y=df['Churn Defense Stories']),
        go.Bar(name='Tech Debt', marker_color='pink', x=sprint_names, y=df['Tech Debt Stories']),
        go.Bar(name='Integrations', marker_color='lightgreen', x=sprint_names, y=df['Integration Stories'])
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.update_layout(title_text='Where did we spend our time')
    fig.show()
















    """Each of these below is a pie graph of the stories"""
    """Basic pie chart for displaying data
    each input is a list, except for the title text.
    #Example
    #colors ['mediumpurple', 'cyan', 'lightgray']
    #slice_labels = ['Features', 'Bugs', 'Chores']
    #values = [number_of_features, number_of_bugs, number_of_chores]
    """
    def pie_chart(colors, slice_labels, values, title_text):
        if len(colors) != len(slice_labels) or len(slice_labels) != len(values):
            print("Input lists are of differing lengths")
            return (1)
        else:
            fig = go.Figure(data=[go.Pie(labels=slice_labels, values=values)])
            fig.update_traces(hoverinfo='label+percent', textinfo='label+value+percent', textfont_size=20,
                            marker=dict(colors=colors, line=dict(color='#000000', width=2)))
            fig.update_layout(title_text= title_text)  
            fig.show()

    # Pie Graph of Stories, Bugs and Features by quantity
    colors = ['mediumpurple', 'cyan', 'lightgray']
    slice_labels = ["Features", "Bugs", "Chores"]
    values = [iteration_counts[0]['Features'], iteration_counts[0]['Bugs'], iteration_counts[0]['Chores']]
    title_text = "Features, Bugs, and Chores"
    pie_chart(colors, slice_labels, values, title_text)
    # Pie Graph of Stories, Bugs and Features by point total
    colors = ['mediumpurple', 'cyan', 'lightgray']
    slice_labels = ["Feature Points", "Bug Points", "Chore Points"]
    values = [iteration_counts[0]['Feature Points'], iteration_counts[0]['Bug Points'], iteration_counts[0]['Chore Points']]
    title_text = "Features, Bugs, and Chores by Points"
    pie_chart(colors, slice_labels, values, title_text)

    # planned vs unplanned by quantity
    colors = ['mediumpurple', 'cyan']
    slice_labels = ["Planned Stories", "Unplanned Stories"]
    values = [iteration_counts[0]['Total Stories'] - iteration_counts[0]['Unplanned Stories'], iteration_counts[0]['Unplanned Stories'] ]
    title_text = "Planned vs Unplanned Stories"
    pie_chart(colors, slice_labels, values, title_text)
    # planned vs unplanned by story points
    colors = ['mediumpurple', 'cyan']
    slice_labels = ["Planned Points", "Unplanned Points"]
    values = [iteration_counts[0]['Total Story Points'] - iteration_counts[0]['Unplanned Points'], iteration_counts[0]['Unplanned Points'] ]
    title_text = "Planned vs Unplanned Points"
    pie_chart(colors, slice_labels, values, title_text)

    # Carryover by story
    colors = ['lightgray', 'cyan']
    slice_labels = ["Stories Finished this Sprint", "Carried Over"]
    values = [iteration_counts[0]['Total Stories'] - iteration_counts[0]['Carry Over Stories'], iteration_counts[0]['Carry Over Stories'] ]
    title_text = "Stories Finished this Sprint vs Stories Finished that were Carried Over"
    pie_chart(colors, slice_labels, values, title_text)
    # Carry over by points
    colors = ['lightgray', 'cyan']
    slice_labels = ["Points Finished this Sprint", "Carried Over Points"]
    values = [iteration_counts[0]['Total Story Points'] - iteration_counts[0]['Unplanned Points'], iteration_counts[0]['Unplanned Points'] ]
    title_text = "Points Completed planned for this sprint vs Points planned in previous sprints"
    pie_chart(colors, slice_labels, values, title_text) 

    # Escalations by story
    colors = ['mediumpurple', 'cyan']
    slice_labels = ["Normal Priority Stories", "Escalated Stories"]
    values = [iteration_counts[0]['Total Stories'] - iteration_counts[0]['Escalated Stories'], iteration_counts[0]['Escalated Stories'] ]
    title_text = "Escalated vs Normal Stories"
    pie_chart(colors, slice_labels, values, title_text)
    # Escalations by points
    colors = ['mediumpurple', 'cyan']
    slice_labels = ["Normal Priority Points", "Escalated Points" ]
    values = [iteration_counts[0]['Total Story Points'] - iteration_counts[0]['Escalated Points'], iteration_counts[0]['Escalated Points'] ]
    title_text = "Escalated vs Normal Priority Points"
    pie_chart(colors, slice_labels, values, title_text)

    # bonuspoints by story
    colors = ['mediumpurple', 'lightgray']
    slice_labels = ["Normal Stories", "Bonus Stories"]
    values = [iteration_counts[0]['Total Stories'] - iteration_counts[0]['Bonus Stories'], iteration_counts[0]['Bonus Stories'] ]
    title_text = "Normal Stories vs Extra Stories outside of our Commitment"
    pie_chart(colors, slice_labels, values, title_text)
    # bonuspoints by points
    colors = ['mediumpurple', 'lightgray']
    slice_labels = ["Normal Points", "Bonus Points"]
    values = [iteration_counts[0]['Total Story Points'] - iteration_counts[0]['Bonus Points'], iteration_counts[0]['Bonus Points'] ]
    title_text = "Normal Points vs Bonus Points"
    pie_chart(colors, slice_labels, values, title_text)

    # Where we spent our story points
    colors = ['mediumpurple', 'cyan', 'lightgray', 'pink', 'lightgreen']
    slice_labels = ["Support", "Client Value", "Churn Defense", "Tech Debt", "Integrations"]
    values = [iteration_counts[0]['Support Stories'], iteration_counts[0]['Client Value Stories'], iteration_counts[0]['Churn Defense Stories'], iteration_counts[0]['Tech Debt Stories'], iteration_counts[0]['Integration Stories']]
    title_text = "Where did we plan our stories"
    pie_chart(colors, slice_labels, values, title_text)
    # Where we spent our stories
    colors = ['mediumpurple', 'cyan', 'lightgray', 'pink', 'lightgreen']
    slice_labels = ["Support", "Client Value", "Churn Defense", "Tech Debt", "Integrations"]
    values = [iteration_counts[0]['Support Points'], iteration_counts[0]['Client Value Points'], iteration_counts[0]['Churn Defense Points'], iteration_counts[0]['Tech Debt Points'], iteration_counts[0]['Integration Points']]
    title_text = "Where did we spend our Points"
    pie_chart(colors, slice_labels, values, title_text)
