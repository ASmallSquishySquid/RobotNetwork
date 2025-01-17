import joblib
import matplotlib.pyplot as plt
import numpy as np
import random

# # plot 10 random ones from each file
# for f in range(10, 16):
# 	with open("Tracking Data Check/Run {f}/pos{f}t5.pkl".format(f = f), "rb") as file:
# 		data = joblib.load(file)

# 	for i in range(10):
# 		img = random.randrange(729)
# 		check = np.array(data["default"][img])
# 		x, y = check.T

# 		plt.plot(x, y)
# 		plt.axis("equal")
# 		plt.gca().invert_yaxis()
# 		# only 12 and 15 are numbered properly
# 		plt.savefig("Tracking Data Check/Run {f}/check{img}.png".format(img = img if (f != 12 and f != 15) else img + 1, f = f))
# 		plt.cla()

# check for forks
# f = 15
# with open("Tracking Data Check/Run {f}/pos{f}t5.pkl".format(f = f), "rb") as file:
# 	data = joblib.load(file)

# for img in range(1, 8, 2):
# 	check = np.array(data["default"][img])
# 	x, y = check.T
# 	plt.scatter(x, y, s = 2)


# plt.axis("equal")
# plt.gca().invert_yaxis()
# plt.legend(["2", "4", "6", "8"])
# plt.savefig("Tracking Data Check/Forks/check.png")

# plot over background
# f = 15
# with open("Tracking Data Check/Run {f}/pos{f}t5.pkl".format(f = f), "rb") as file:
# 	data = joblib.load(file)

# for img in [71, 114, 140, 371, 482, 498, 532, 544, 665, 715]:
# 	check = np.array(data["default"][img - 1])
# 	x, y = check.T
# 	plt.scatter(x, y, s = 0.05)
# 	back = plt.imread("Tracking Data Check\Run {f}\pat{img}t=5.bmp".format(f = f, img = img))
# 	plt.imshow(back)
# 	plt.savefig("Tracking Data Check\Run {f}\overlay_{img}.png".format(f = f, img = img))
# 	plt.cla()

# check new run
with open("Spring 2022\Tracking Data Check\Rerun\pos.pkl", "rb") as file:
	data = joblib.load(file)

for img in range(620, 623):
	check = np.array(data["default"][img])
	x, y = check.T

	plt.plot(x, y)
	plt.axis("equal")
	plt.gca().invert_yaxis()
	# only 12 and 15 are numbered properly
	plt.savefig("Spring 2022\Tracking Data Check\Rerun\check{img}.png".format(img = img + 1))
	plt.cla()