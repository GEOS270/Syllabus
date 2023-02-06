import pandas as pd
import matplotlib.pyplot as plt


Evals = pd.read_csv("docs/Evaluations/Considering_everything_how_would_you_rate_this_course.csv")

Summary = Evals[['Very Poor','Poor','Neutral','Good','Very Good']].sum()
Response_Rate = Summary.sum()/Evals['N'].sum()
Favorability = Evals[['Good','Very Good']].sum().sum()/Summary.sum()
Terms = Evals['N'].count()

fig,ax = plt.subplots(1,1,figsize=(6,6))
ax.bar(Summary.index,Summary,facecolor='#dec028',edgecolor='k')
ax.set_title('''Considering everything, how would you rate this course?\n
Summary of Dr. June Skeeter's GEOS 270 teaching evaluations
 Favorability ('''+str(int(Favorability*100))+''' %); n = '''+str(Summary.sum())+''' responses''')
ax.grid(axis='y')
plt.tight_layout()
plt.savefig('docs/images/CourseRating.png')
plt.show()
