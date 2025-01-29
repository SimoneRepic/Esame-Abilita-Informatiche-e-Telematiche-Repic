import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

# Initialize lists
col0 = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []

# Open data file
with open('file2_Groups_AGN-wWU_500Mpc_Data.txt', 'r') as ppf:

# Skip file header
    header = ppf.readline()

# Read data from file
    for line in ppf:
        line = line.strip()
        columns = line.split()
        col0.append(float(columns[0]))
        col1.append(float(columns[1]))
        col2.append(float(columns[2]))
        col3.append(float(columns[3]))
        col4.append(float(columns[4]))
        col5.append(float(columns[5]))
        col6.append(float(columns[6]))
        col7.append(float(columns[7]))

# Transform data into arrays
total = np.array(col0)
gas = np.array(col1)
dm = np.array(col2)
stellar = np.array(col3)
bh = np.array(col4)
x = np.array(col5)
y = np.array(col6)
z = np.array(col7)

# Question 1

barionic = gas + stellar

# Perform linear fit
coefficients = np.polyfit(barionic, dm, 1)
m, q = coefficients

# Generate fitted line
dm_fit = m * barionic + q

# Plot data and fitted line with legend and labels
plt.scatter(barionic, dm, s=5, label='Data Points')
plt.plot(barionic, dm_fit, color='red', label=f'Linear fit: $y = {m:.3f}x {q:.3f}$')
plt.xlabel('Barionic Mass ($10^{10}M_{\odot}$/h)')
plt.ylabel('Dark Matter Mass ($10^{10}M_{\odot}$/h)')
plt.legend()
plt.title('Question 1')
plt.show()

# Question 2

# Find index of total mass maximum
maxtot = np.argmax(total)

# Create new arrays removing the maxtot-element
newx = np.delete(x, maxtot)
newy = np.delete(y, maxtot)
newz = np.delete(z, maxtot)
newtotal = np.delete(total, maxtot)
newdm = np.delete(dm, maxtot)

# Compute Euclidean distance from most massive structure
r = np.sqrt((newx - x[maxtot])**2 + (newy - y[maxtot])**2 + (newz - z[maxtot])**2)

# Plot data in logarithmic scale
plt.scatter(np.log(r), np.log(newtotal), s=5, label='Data Points')
plt.xlabel('log of Distance from Most Massive Structure (ckpc/h)')
plt.ylabel('log of Total Mass ($10^{10}M_{\odot}$/h)')
plt.legend()
plt.title('Question 2')
plt.show()

# Question 3

# Here the most massive structure is excluded, since it is a stand-alone, far away from all the other data

# Compute mean of dark matter mass distribution
mean = np.sum(newdm)/len(newdm)

# Sort dark matter array in ascending order
sortdm = np.sort(newdm)

# Compute index of median-to-be element (len(newdm) is odd)
n = int((len(newdm) + 1)/2)

# Compute median of dark matter mass distribution
median = sortdm[n]

# Plot histogram of dark matter mass together with mean and median
plt.hist(dm, bins=50, range=(0,1.4), label='Data')
plt.xlabel('Dark Matter Mass ($10^{10}M_{\odot}$/h)')
plt.ylabel('Frequency')
plt.axvline(x = mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean = ${mean:.2f}$')
plt.axvline(x = median, color='orange', linestyle='dashed', linewidth=1, label=f'Median = ${median:.2f}$')
plt.legend()
plt.title('Question 3')
plt.show()

# Question 4

# Create figure with 4 frames
fig, axs = plt.subplots(2, 2)

# Plot using variable-dependent dot size and colour
sc = axs[0, 0].scatter(x, y, s=200*stellar, c=gas, cmap='jet', label = 'Data Points')
axs[0, 0].set_xlabel('x (ckpc/h)')
axs[0, 0].set_ylabel('y (ckpc/h)')
axs[0, 0].legend(markerscale = 0.15, fontsize = 6, handletextpad = 0.05)
axs[0, 1].scatter(z, y, s=200*stellar, c=gas, cmap='jet', label = 'Data Points')
axs[0, 1].set_xlabel('z (ckpc/h)')
axs[0, 1].set_ylabel('y (ckpc/h)')
axs[0, 1].legend(markerscale = 0.15, fontsize = 6, handletextpad = 0.05)
axs[1, 0].scatter(x, z, s=200*stellar, c=gas, cmap='jet', label = 'Data Points')
axs[1, 0].set_xlabel('x (ckpc/h)')
axs[1, 0].set_ylabel('z (ckpc/h)')
axs[1, 0].legend(markerscale = 0.15, fontsize = 6, handletextpad = 0.05, loc = 'center left')

# Colourbar settings
cbar = fig.colorbar(axs[1, 0].scatter(x, y, s=stellar, c=gas, cmap='jet'), ax=axs[1, 1])
cbar.set_label('Gas Mass ($10^{10}M_{\odot}$/h)')

# Delete bottom right frame
plt.delaxes(axs[1,1])

# Set space between each frame
plt.tight_layout(pad=1.0)

fig.suptitle('Question 4', y=1.05)

# Legend settings
plt.legend(*sc.legend_elements("sizes", num=5), labelspacing = 2, borderpad = 1.3, handletextpad = 1, title='Stellar Mass ($10^{10}M_{\odot}$/h) ', frameon = False, bbox_to_anchor=(0, 1.2))

plt.show()

# Question 5

# Select black holes and stellar masses
selbh = bh[bh > 8*10**(-5)]
selstellar = stellar[(bh > 8*10**(-5))]

# Perform linear fit
coeff = np.polyfit(selstellar, selbh, 1)
a, b = coeff

# Generate fitted line
selbh_fit = a * selstellar + b

# Plot data and fitted line with legend and labels
plt.scatter(selstellar, selbh, s=5, label='Data Points')
plt.plot(selstellar, selbh_fit, color='red', label=f'Linear fit: $y = {a:.1f}x {b:.1f}$')
plt.xlabel('Stellar Mass ($10^{10}M_{\odot}$/h)')
plt.ylabel('Black Hole Mass ($10^{10}M_{\odot}$/h)')
plt.legend()
plt.title('Question 5')
plt.show()

# Question 6

# Select total masses and respective positions
seltotal = total[total > 0.307]
selx = x[(total > 0.307)]
sely = y[(total > 0.307)]
selz = z[(total > 0.307)]

# Initialize list
distlist = []

# Number of selected masses
c = int(len(seltotal))

# Compute distance of each halo from other haloes
for i in range(0, c, 1):
  for j in range(0, c, 1):
    item = np.sqrt((selx[j] - selx[i])**2 + (sely[j] - sely[i])**2 + (selz[j] - selz[i])**2)
    distlist.append(item)

# Transform list into array
dist = np.array(distlist)

# Shape array as a matrix
shape = (c, c)
distances = dist.reshape(shape)

# Get indices of selected haloes
selindices = np.where(seltotal > 0.307)[0]

# Define bins for total masses and distances
totalbins = np.linspace(0.307, seltotal.max(), 100)
distancebins = np.linspace(0, distances.max(), 100)

# Initialize cumulative histogram
cumhisto = np.zeros((len(totalbins) - 1, len(distancebins) - 1))

# Calculate histograms
for i in selindices:

# Select distances from others haloes for i-indexed halo
    currentdistances = distances[i]

# Create 2D histogram for i-indexed halo
    hist, xedges, yedges = np.histogram2d(seltotal, currentdistances, bins=[totalbins, distancebins])

# Add it to cumulative histogram
    cumhisto += hist

# Plot cumulative 2D histogram with labels
plt.figure()
plt.imshow(cumhisto.T, origin='lower', aspect='auto', extent=[totalbins[0], totalbins[-1], distancebins[0], distancebins[-1]], cmap='jet')
plt.colorbar(label='Number of Haloes')
plt.xlabel('Total Mass ($10^{10} M_\odot/h$)')
plt.ylabel('Distance (ckpc/h)')
plt.title('Question 6')
plt.show()
