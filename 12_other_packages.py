### 12_other_packages.py ##
#
# matplotlib - plot the graph for data analysis
# it is part of the scipy module, libraries for math and science
# https://scipy.org/
#
### install matplotlib individually ###
# pipenv install matplotlib
#
#
import time as t
import matplotlib.pyplot as plt
#

#import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [1500, 1200, 1100, 1800]
plt.plot(x, y)
plt.show()
#
# replace x with legend
legend = ["Jan", "Feb", "Mar", "Apr"]
plt.xticks(x, legend)
plt.plot(x, y)
plt.show()
#
# change to bar chart
plt.bar(x, y)
plt.ylabel("Sales in US$")
plt.title("Monthly Sales")
plt.show()
#
### ----- exercise - show typing speed -----###
#import matplotlib.pyplot as plt
#import time as t
times = []
mistakes = 0
print("This programm will help you type faster.")
print("You will have to type the word 'programming' as fast as you can for five times")
input("Press enter to start.")
while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if(word.lower() != 'programming'):
        mistakes += 1

print("You made", mistakes, "mistakes.")
print("Now let's see your evolution")
t.sleep(1)

x = [1, 2, 3, 4, 5]
y = times
plt.plot(x, y)
# use legend, no numbers in between each spot
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempts")
plt.title("Your typing evolution")
plt.show()


# {
#     "response_code": 0,
#     "results": [
#         {
#             "category": "Geography",
#             "type": "multiple",
#             "difficulty": "hard",
#             "question": "Into which basin does the Jordan River flow into?",
#             "correct_answer": "Dead Sea",
#             "incorrect_answers": [
#                 "Aral Sea",
#                 "Caspian Sea",
#                 "Salton Sea"
#             ]
#         }
#     ]
# }

