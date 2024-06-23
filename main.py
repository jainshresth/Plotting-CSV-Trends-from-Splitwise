import pandas as pd
import matplotlib.pyplot as plt
import os

output_dir = 'outputs'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.switch_backend('TkAgg')

df = pd.read_csv('Splitwise expenses Jun 22.csv')
date_time = df['Date']
date_time = pd.to_datetime(date_time)
df = df.set_index(date_time)
df = df.drop(df.columns[1:5], axis=1)

dates = df['Date']

ngames, nplayers = df.shape

for m in range(1, nplayers):
    dftemp = df.iloc[:, m]
    dftemp2 = dftemp.copy()

    for i in range(ngames - 1):
        if i != 0:
            dftemp2.iloc[i] += dftemp2.iloc[i - 1]

    person = df.columns[m]
    person = str(person)

    plt.figure(figsize=(10, 7))
    plt.plot_date(dates, dftemp2, linestyle="--", color='g')
    # plt.plot(dftemp2.index, dftemp2, linestyle="--", color='g', marker='o')
    plt.title(person)
    plt.xlabel('Dates of games')
    plt.ylabel(person + "'s output")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.ylim(-250,250)

    filename = os.path.join(output_dir, f"{person}_poker.png")
    plt.savefig(filename)
    # plt.show() #Uncomment if you want to see the plots made one by one
    plt.close()

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

