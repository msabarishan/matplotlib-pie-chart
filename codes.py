import matplotlib.pyplot as plt

# Value of Pie
a=[30,20,15,25,10]

# Label of Pie
b=[]
for i in range(0,5):
    b.append(alpha[i])
    
# Explode view
exp=[0.1,0,0,0,0]

# Ploting Pie chart
plt.pie(a,labels=b,startangle=0,colors=["black", "hotpink", "b", "#4CAF50","yellow"],explode=exp)
plt.title("Pie Chart")
plt.legend(title="legend")
plt.show()
