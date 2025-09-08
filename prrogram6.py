import random
import matplotlib.pyplot as plt

#generate 50 random ages between 10 and 80
ages = [random.randint(10,80) for _ in range(50)]

#create histogram
plt.figure(figsize=(10,5))
plt.hist(ages,bins=range(10,80,5),edgecolor="black",color="red")

#add labels and title
plt.title("Histogram of ages")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.show()