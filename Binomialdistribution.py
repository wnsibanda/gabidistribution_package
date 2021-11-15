import numpy as np
import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution


class Binomial(Distribution):
    """ Binomial distribution class for calculating and
    visualizing a Binomial distribution.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring

    """

    # You can then calculate the mean and standard deviation with the following formula:
    # mean = p * n
    # standard deviation = sqrt(n * p * (1 - p))

    def __init__(self, prob=0.4, size=30):

        Distribution.__init__(self, mu, sigma)

        self.p = prob
        self.n = size

    def calculate_mean(self):

        """Function to calculate the mean from p and n

        Args:
            None

        Returns:
            float: mean of the data set

        """
        self.mean = self.p * self.n

        return self.mean

    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.

        Args:
            None
        Returns:
            float: standard deviation of the data set

        """
        self.stdev = np.sqrt(self.n * self.p * (1 - self.p))

        return self.stdev

    def replace_stats_with_data(self):

        """Function to calculate p and n from the data set.
           The function updates the p and n variables of the object.

        Args:
            None

        Returns:
            float: the p value
            float: the n value

        """
        # calculate number of trials n
        self.n = len(self.data)

        # calculate probability of positive outcomes
        count = 0
        for outcome in self.data:
            if outcome == 1:
                count = count + 1

        positive_outcome = count
        self.p = positive_outcome / self.n

        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.n, self.p

    def plot_bar(self):

        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.bar(data=self.data)
        plt.xlabel('Outcomes')
        plt.ylabel('Counts')
        plt.title('Bar chart of the outcomes')

    def pdf(self, k):

        """Probability density function calculator for the binomial distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """
        q = 1 - self.p

        parta = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n - k))
        partb = np.power(self.p, k) * np.power(q, (self.n - k))

        return parta * partb

    def plot_binomial_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        x = []
        y = []

        for i in range(len(self.data) + 1):
            x = [i for i in range(len(self.data) + 1)]
            y = [pdf(i) for i in range(len(self.data) + 1)]

        return x, y

        plt.plot(x, y)
        plt.xlabel('Number of trials')
        plt.ylabel('Probability')
        plt.title('Binomial distribution of the data')

    def __add__(self, other):

        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """
        # the try, except statement above will raise an exception if the p values are not equal
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        # Assume that the p values of the two distributions are the same.
        # implement the case for two distributions with equal p.

        result = Binomial()
        result.p = self.p  # When adding two binomial distributions, the p value remains the sam
        result.n = self.n + other.n
        result.mean = self.mean + other.mean
        result.stdev = np.sqrt(np.power(self.stdev, 2) + np.power(other.stdev, 2))

        return result

    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Binomial object

        """

        return f"mean: {self.mean}, standard deviation: {self.stdev}, p: {self.p}, n: {self.n}"
