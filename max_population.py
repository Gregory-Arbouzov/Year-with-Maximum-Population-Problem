import matplotlib.pyplot as plt

alive_per_year = [0]*101
people = {'jack': [1902,1969], 'tom': [1930,1991], 'george': [1919,1943], 'glen': [1950,1973], 'sam': [1976,2000],'scott': [1904,1987], "gerald": [1920,1980], "kevin": [1940,1996], "mark": [1921,1953], "calvin": [1930,1991], "nancy": [1911,1988],"stacy": [1940,1999],"kim": [1970,1971],"grace": [1932,1980], "katherine": [1901,1979], "kay": [1950,2000], "bailey": [1948,2000], "madison": [1922,1998], "maya": [1913,1966], "elizabeth": [1929,1984]}

for person in people:
    for year in range(people[person][0]-1900,people[person][1]-1900):
        alive_per_year[year] += 1

max_years = []
max_year = 0

for i in range(100):
    if alive_per_year[i] > max_year:
        max_year = alive_per_year[i]
for j in range(100):
    if alive_per_year[j] == max_year:
        max_years.append(1900 + j)
        
print("The year/years with the most people alive are:",max_years)

x1 = [year for year in range(1900,2001)]
y1 = alive_per_year
plt.ylim(0,18)
plt.xlabel('Year',fontsize = 16)
plt.ylabel('Number of People Alive',fontsize = 16)
plt.title('Number of People Alive by Year',fontsize = 20)
fig_size = plt.rcParams["figure.figsize"]
plt.plot(x1, y1)
plt.show()