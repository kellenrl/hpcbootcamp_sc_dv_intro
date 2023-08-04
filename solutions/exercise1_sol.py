celery = [12, 28, 9, 33]
veggies_df['celery'] = celery

new_sum_df = veggies_df.aggregate('sum')
new_sum_df.plot.pie(y='sum',ylabel='veggie proportions', autopct='%1.0f%%')