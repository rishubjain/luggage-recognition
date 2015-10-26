# luggage-recognition

During my senior year of high school, I created a luggage recognition system meant to solve the problem of lost luggage in airports. If you give it a picture of your piece of luggage, it would find which city, airport, and terminal it would most likely be in, giving you a list of similar pictures you can choose from. It works by giving each piece of luggage two characteristics: its dimensions and its dominant colors. The dimensions are calculated by generating an outline of the image using Canny edge detection and calculating the first and last pixels of the outline in both X and Y directions. Then, I calculated the number of dominant colors, and what those colors are, by using a k-means clustering and finding the optimal value of k. I found that these two characteristics were the most important, and matched the input image with an image in the database of luggage images using these two values, and gave the user the most likely matches. This was all done in Python from scratch.

kmeans.py - Finds the number of distinct colors in each image

outline.py - Finds the dimensions of each image

Senior Research Paper.pdf - My Research Paper

Senior Research Presentation.pptx - My Research Presentation
